-- A small MySQL library database with three related tables.

CREATE DATABASE IF NOT EXISTS arjun_library;
USE arjun_library;

DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publication_year INT,
    available_copies INT NOT NULL DEFAULT 1
);

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    joined_on DATE NOT NULL
);

CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

INSERT INTO books (title, author, publication_year, available_copies) VALUES
('Introduction to Algorithms', 'Thomas H. Cormen', 2009, 2),
('Clean Code', 'Robert C. Martin', 2008, 1),
('Python Crash Course', 'Eric Matthes', 2019, 3);

INSERT INTO members (full_name, email, joined_on) VALUES
('Sample Member One', 'member1@example.com', '2026-09-01'),
('Sample Member Two', 'member2@example.com', '2026-09-03');

INSERT INTO loans (book_id, member_id, loan_date, return_date) VALUES
(1, 1, '2026-09-05', NULL),
(2, 2, '2026-09-06', '2026-09-12');

-- Show all books.
SELECT title, author, available_copies
FROM books
ORDER BY title;

-- Show books that have not yet been returned.
SELECT b.title, m.full_name, l.loan_date
FROM loans AS l
JOIN books AS b ON l.book_id = b.book_id
JOIN members AS m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;

-- Count the number of loans recorded for each book.
SELECT b.title, COUNT(l.loan_id) AS number_of_loans
FROM books AS b
LEFT JOIN loans AS l ON b.book_id = l.book_id
GROUP BY b.book_id, b.title
ORDER BY number_of_loans DESC;