"""A small CSV-based expense tracker."""

import csv
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


FOLDER = Path(__file__).resolve().parent
DATA_FILE = FOLDER / "expenses.csv"
CHART_FILE = FOLDER / "spending_by_category.png"
FIELDS = ["date", "category", "description", "amount"]
CURRENCY = "INR"


def load_expenses():
    """Load saved expenses into a pandas DataFrame."""
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return pd.DataFrame(columns=FIELDS)

    expenses = pd.read_csv(DATA_FILE)

    missing = set(FIELDS) - set(expenses.columns)
    if missing:
        raise ValueError(
            f"The CSV file is missing columns: {', '.join(sorted(missing))}"
        )

    expenses["amount"] = pd.to_numeric(
        expenses["amount"], errors="raise"
    )
    return expenses


def add_expense():
    """Ask for an expense and save it to the CSV file."""
    entered_date = input(
        "Date (YYYY-MM-DD, blank for today): "
    ).strip()

    if not entered_date:
        entered_date = date.today().isoformat()

    try:
        datetime.strptime(entered_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.\n")
        return

    category = input(
        "Category (e.g. Food, Travel, Books): "
    ).strip().title()

    description = input("Description: ").strip()

    if not category or not description:
        print("Category and description cannot be blank.\n")
        return

    try:
        amount = Decimal(
            input(f"Amount ({CURRENCY}): ").strip()
        )

        if (
            not amount.is_finite()
            or amount <= 0
            or amount.as_tuple().exponent < -2
        ):
            raise ValueError

    except (InvalidOperation, ValueError):
        print(
            "Enter an amount greater than zero "
            "with at most two decimal places.\n"
        )
        return

    new_file = (
        not DATA_FILE.exists()
        or DATA_FILE.stat().st_size == 0
    )

    with DATA_FILE.open(
        "a", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file, fieldnames=FIELDS
        )

        if new_file:
            writer.writeheader()

        writer.writerow({
            "date": entered_date,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}",
        })

    print("Expense saved.\n")


def view_expenses():
    """Show all saved expenses and their total."""
    expenses = load_expenses()

    if expenses.empty:
        print("No expenses recorded yet.\n")
        return

    expenses = expenses.sort_values(
        "date", ascending=False
    )

    print(
        "\n"
        + expenses.to_string(
            index=False,
            formatters={
                "amount": lambda value: f"{value:.2f}"
            },
        )
    )

    print(
        f"Total: {CURRENCY} "
        f"{expenses['amount'].sum():.2f}\n"
    )


def category_summary():
    """Calculate and display spending by category."""
    expenses = load_expenses()

    if expenses.empty:
        print("No expenses to summarise.\n")
        return None

    summary = (
        expenses.groupby("category", as_index=False)
        .agg(
            transactions=("amount", "size"),
            total=("amount", "sum"),
        )
        .sort_values("total", ascending=False)
    )

    print("\nSpending by category:")
    print(
        summary.to_string(
            index=False,
            formatters={
                "total": lambda value: f"{value:.2f}"
            },
        )
    )

    print(
        f"Overall total: {CURRENCY} "
        f"{summary['total'].sum():.2f}\n"
    )

    return summary


def save_chart():
    """Save a bar chart of category spending."""
    summary = category_summary()

    if summary is None:
        return

    fig, ax = plt.subplots(figsize=(8, 4.5))

    ax.bar(
        summary["category"],
        summary["total"],
        color="#4568f2",
    )

    ax.set_title("Spending by category")
    ax.set_ylabel(f"Amount ({CURRENCY})")
    ax.tick_params(axis="x", rotation=25)

    fig.tight_layout()
    fig.savefig(CHART_FILE, dpi=160)
    plt.close(fig)

    print(f"Chart saved to: {CHART_FILE}\n")


def main():
    actions = {
        "1": add_expense,
        "2": view_expenses,
        "3": category_summary,
        "4": save_chart,
    }

    while True:
        print("Expense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show category summary")
        print("4. Save category chart")
        print("5. Exit")

        choice = input("Choose 1-5: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice in actions:
            actions[choice]()
        else:
            print(
                "Please choose a number from 1 to 5.\n"
            )


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")