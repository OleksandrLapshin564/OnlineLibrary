# Online Library 📚

**Online Library** is a web application that allows users to search, read, and discuss books online. It includes both a user-facing interface and an admin panel for managing books and users. The project is built with **Django** and runs inside **Docker** containers.

---

## Features

### User Section
- **User Registration**: Sign up with full name, city, country, email, nickname, and password.
- **Book Search**: Search books by title, author, or genre with filtering and sorting.
- **Read Online**: Read books directly in the browser, with reading progress saved.
- **Discussion**: Leave comments and participate in book discussions.

### Admin Section
- **Add Books**: Admin can add books with title, author, genre, description, and text file.
- **Edit Books**: Admin can update book information and text files.
- **Block Users**: Admin can block users violating rules.
- **Delete Comments**: Admin can remove inappropriate comments.

---

## Installation and Docker Setup

1. Clone the repository:
```bash
git clone https://github.com/YourUsername/OnlineLibrary.git
cd OnlineLibrary
2. Build and start Docker containers:
docker-compose up -d --build
3. Check running containers:
docker ps
You should see containers onlinelibrary-web-1 (port 8080) and onlinelibrary-db-1 (port 5433).
4. Open your browser at: http://localhost:8080
URLs / Endpoints
Page / Endpoint	URL	Description
Home	/	Homepage or landing page
Catalog of Books	/books/	List of all published books
Book Details	/books/<id>/	Detailed view of a specific book by ID
Admin Panel	/admin/	Django admin panel
User Login	/users/login/	Login page for registered users
User Logout	/users/logout/	Logout page
Media Files	/media/<path>	Access uploaded book covers or text files

Note: Use trailing slashes (/books/) to avoid 404 errors.
Development
Make sure you have Python 3.9+, Docker, and Docker Compose installed.
Activate virtual environment for local scripts:
python -m venv .venv
source .venv/Scripts/activate  # Windows
install dependencies:
pip install -r requirements.txt
Run Django development server (inside Docker container):
docker exec -it onlinelibrary-web-1 bash
python manage.py runserver 0.0.0.0:8000
Database

PostgreSQL is used as the database (container onlinelibrary-db-1 on port 5433).

Media files (book covers and text files) are stored in /media/.
Authors

Robin Nixon – Web developer and educator.

Paul McFedries – Technical writer.

David McFarland – Web developer, teacher, author.

Chris Minnick, Eva Holland, Oleg Zelenyak, Aymen El Amri, David Sklar, Ed Tittel, Oleg Vasilev, John Paul Mueller, Nikolai Poleshchuk, Rubén Alba, Oliver Villar, Fabio Staiano, Alexander Gorelik, Roger "Buzz" King – Contributors of example book content.
Notes

Ensure all containers are running before accessing the site.

Use /books/ to access the catalog.

Admin credentials can be created via:
docker exec -it onlinelibrary-web-1 bash
python manage.py createsuperuser
This project is intended for educational purposes and follows the final exam requirements for Python-37 course.
License

This project is for academic purposes. All book content is sample data.


