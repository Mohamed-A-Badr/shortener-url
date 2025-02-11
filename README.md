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
   https://github.com/Mohamed-A-Badr/shortener-url.git
   cd shortener-url
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

4. Update the `.env-example` file and fill it with the required environment variables.

5. Run Docker engine or Docker Desktop

6. Build and start the containers:

   ```sh
   docker-compose up --build
   ```

## Usage

- Access the admin interface at `/admin/` to manage URLs.
- Use the API to shorten URLs and redirect to the original URLs.
- Access the API documentation at `/docs/swagger/`.

## API Endpoints

- `POST /api/v1/shortener/`: Shorten a URL.
- `GET /api/v1/<short_code>/`: Redirect to the original URL.
- The application will be available at `http://localhost:8000`.
