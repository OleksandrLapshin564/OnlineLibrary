# HISTORY.md

## Online Library – Exam Project (Python-37)

### Branch: `exam_stage_books`

---

### 2025-09-21
- Created Django project `OnlineLibrary`.
- Configured Docker and `docker-compose` for web server and PostgreSQL.
- Added basic `settings.py` settings and folder structure.
- Connected Bootstrap via CDN for templates.

---

### 2025-09-22
- Created `books` application.
- Added `Book`, `Author`, `Genre` models.
- Implemented admin panel for managing books, authors and genres.
- Added uploading book covers and text files.
- Developed templates:
- `book_list.html` – displays book catalog.
- `book_detail.html` – detailed view of the book.
- Added routes to `urls.py` for the list and details of the book.

---

### 2025-09-23
- Added handling of missing covers and descriptions in templates.
- Fixed `truncatechars` for book descriptions.
- Added displaying author biographies in templates (`book_list.html`, `book_detail.html`).
- Checked the project's operation in Docker on port 8080.
- Fixed errors with URLs (`404` on `/book/` → replaced with `/books/`).

---

### 2025-09-24
- Added commands to create a superuser and start the server in README.md.
- Fixed templates for better adaptability and appearance.
- Prepared a detailed **README.md** with a description of the functionality, Docker instructions and a list of endpoints.
- Checked the operation of media files (covers, text files) in the browser.
- Tested and clarified the biographies of the authors.

---

### 2025-09-25
- Prepared README.md and HISTORY.md for the teacher.
- Commits were made on the `exam_stage_books` branch.
- All changes are saved on GitHub on the `exam_stage_books` branch.

---

**Note**: Further stages include:
- User registration and authentication.
- Book search with filtering and sorting.
- Online reading of books with progress.
- Comments and discussion of books.
- Full implementation of the REST API for the frontend and testing via Postman.