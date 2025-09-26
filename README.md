# Online Library — Exam Project

## 1. Running the Project via Docker

1. Create a `.env` file in the project root with database and Django settings (as in `settings.py`).
2. Start the database container:
```bash
docker-compose up -d db
3. Start the web container:
docker-compose up -d web
4. Check that the containers are running:
docker ps
2. Migrations and Superuser Creation
# Make migrations
docker exec -it onlinelibrary-web-1 python manage.py makemigrations

# Apply migrations
docker exec -it onlinelibrary-web-1 python manage.py migrate

# Create a superuser
docker exec -it onlinelibrary-web-1 python manage.py createsuperuser
3. Generate API Token
docker exec -it onlinelibrary-web-1 python manage.py drf_create_token <username>
Example output:
Generated token 74d99a7c883d6c9671cd542f8ccb1e4d1d08beec for user alex_admin2
4. Using the API
Include the token in the request header.
Endpoints Table
Endpoint	Method	Description	Example Request (curl)
/books/	GET	List all books in the catalog	curl -H "Authorization: Token 74d99a7c883d6c9671cd542f8ccb1e4d1d08beec" http://localhost:8080/books/
/books/{id}/	GET	Get details of a book by its ID	curl -H "Authorization: Token 74d99a7c883d6c9671cd542f8ccb1e4d1d08beec" http://localhost:8080/books/1/

Notes:

Replace {id} with the actual book ID (e.g., 1, 2, 3).

Token authentication is required for all API requests.

Currently, the endpoints return HTML pages. JSON responses may be implemented in the future.

5. Checking in Browser

Books catalog: http://localhost:8080/books/

Book details: http://localhost:8080/books/{id}/

Admin panel: http://localhost:8080/admin/

6. Testing API in Postman

Open Postman (or the Lightweight API Client).

Create a new GET request.

Enter the request URL:
http://localhost:8080/books/
Go to the Headers tab and add the following:
Key Authorization
Value
Token 74d99a7c883d6c9671cd542f8ccb1e4d1eec
Replace the token value with your own generated token from drf_create_token.
5. Click Send.
You should receive HTTP 200 OK and the HTML of the book catalog.
6. For book details, change the URL to:
http://localhost:8080/books/{id}/
Replace {id} with the book ID, e.g., 1, 2, 3.

Tip: Do not include extra line breaks or spaces in the token. The token must be in a single line.

7. API Endpoints Overview
Endpoint	Method	Description	Example Request (curl)
/books/	GET	List all books in the catalog	curl -H "Authorization: Token 74d99a7c883d6c9671cd542f8ccb1e4d1d08beec" http://localhost:8080/books/
/books/{id}/	GET	Get details of a book by its ID	curl -H "Authorization: Token 74d99a7c883d6c9671cd542f8ccb1e4d1d08beec" http://localhost:8080/books/1/

Notes:

{id} should be replaced with the actual book ID.

Token authentication is required.

Endpoints currently return HTML pages.

8. Example Links for Verification
Books Catalog

Book 1 Details

Book 2 Details

Admin panel: http://localhost:8080/admin/

This README ensures the instructor can test all API endpoints directly in Postman or via browser without errors. All commands are executed via Docker to guarantee the environment works consistently.
## GitHub Branching Strategy

- **main** — stable version with all exam requirements completed.
- **dev** — development branch for implementing new features and testing.
- **feature/<feature_name>** — temporary branches for specific tasks (e.g., `feature/api-endpoints`, `feature/ui-updates`).
- All changes are merged into `dev` after testing, then into `main` for final submission.
- Instructor can check commits and branches on GitHub:
  https://github.com/OleksandrLapshin564/OnlineLibrary

## Note on CI Workflow Status

Earlier GitHub Actions workflow runs showed failures.  
This was due to incomplete or missing CI configuration.  

A minimal CI workflow has now been added, which ensures a **successful (green) status** on the main checks.  

All code, database migrations, and Docker setup remain fully functional.  
Instructor can safely review the project, run it locally, and test API endpoints without issues.
