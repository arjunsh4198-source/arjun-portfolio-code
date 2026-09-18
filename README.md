# Arjun Sharma — Computer Science Portfolio

A responsive portfolio showcasing my computer science studies and practical projects. The website is built with HTML, CSS and JavaScript and includes an animated SVG illustration, project filters, mobile navigation, education details and a LaTeX CV.

## Portfolio contents

- `index.html` — website structure and content
- `css/style.css` — layout, colours and responsive styling
- `js/main.js` — mobile navigation and project filtering
- `assets/illustrations/developer.svg` — animated illustration
- `projects/expense-tracker/expense_tracker.py` — Python expense tracker
- `projects/library-database/library.sql` — MySQL library database exercise
- `cv/arjun-sharma-cv.tex` — LaTeX CV source
- `cv/` — compiled CV in PDF format

## View the website

The portfolio is published through GitHub Pages. Open the published website using the GitHub Pages link associated with this repository.

To preview it locally, download the repository and open `index.html` in a browser. The website uses relative file paths, so its pages and assets also work when hosted through GitHub Pages.

## Projects

### Personal portfolio

The website presents my education, technical skills, projects and CV. Its project filters allow visitors to display all projects or focus on the Web, Python or Database categories. The layout adapts to desktop and narrower screens.

**Technologies:** HTML, CSS, JavaScript and SVG.

### Expense tracker

A command-line Python program for recording expenses in a CSV file. It can display saved entries, summarise spending by category using pandas and generate a chart using matplotlib. Input checks help prevent invalid records from being saved.

**Technologies:** Python, CSV, pandas and matplotlib.

To run it, install Python and the required libraries:

```bash
python -m pip install pandas matplotlib
python projects/expense-tracker/expense_tracker.py
```

Follow the on-screen menu to add an expense and explore the available summaries and chart output. On Windows, `py` can be used instead of `python` if that is how Python is installed.

### Library database

A MySQL exercise containing related tables for books, members and loans. The SQL file includes sample records and queries that demonstrate how the tables work together.

**Technologies:** SQL and MySQL.

To explore it, open `projects/library-database/library.sql` in MySQL Workbench or another MySQL client, select a suitable database and execute the statements. The project is provided as a SQL exercise; the portfolio website does not require a running database.

## CV

The `cv` directory contains the finished PDF CV and its editable LaTeX source. The website provides actions to view the PDF and download the source file.

## Testing

The published website was checked at desktop and narrower screen widths. Navigation, project filters, project source links and CV actions were tested through the published site. The expense tracker was also tested by saving an example entry, reading it back, producing a category summary and generating a chart.