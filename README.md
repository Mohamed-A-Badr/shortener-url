# URL Shortener Service

This is a URL Shortener service built with Django. It allows users to shorten long URLs and redirect to the original URLs using the shortened codes.

## Features

- Shorten long URLs
- Redirect to original URLs using shortened codes
- Admin interface to manage URLs
- API documentation with Swagger
- Caching with Redis
- Error tracking with Sentry

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a file based on the file and fill in the required environment variables.

5. Apply the migrations:

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage

- Access the admin interface at `/admin/` to manage URLs.
- Use the API to shorten URLs and redirect to the original URLs.
- Access the API documentation at `/docs/swagger/`.

## API Endpoints

- `POST /api/v1/shortener/`: Shorten a URL.
- `GET /api/v1/<short_code>/`: Redirect to the original URL.

## Docker

To run the project with Docker, use the following commands:

1. Build and start the containers:

   ```sh
   docker-compose up --build
   ```

2. The application will be available at `http://localhost:8000`.
