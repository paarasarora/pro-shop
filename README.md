# Pro Shop Backend

A Django-based REST API backend for the Pro Shop e-commerce platform.

## Overview

This backend provides a RESTful API for the Pro Shop e-commerce application, handling product management, user authentication, order processing, and more. It's built with Django and Django REST Framework.

## Technology Stack

- **Python 3.x**
- **Django**: Web framework
- **Django REST Framework**: API development
- **SQLite**: Database (for development)

## Project Structure

- `backend/`: Django project configuration
- `base/`: Main application module
  - `models.py`: Data models for products, orders, users, etc.
  - `serializer.py`: JSON serializers for API responses
  - `views.py`: API endpoints and business logic
  - `urls.py`: URL routing for API endpoints

## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pro-shop
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers pillow
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- `/api/products/`: List all products
- `/api/products/:id/`: Get product details
- `/api/users/`: User management
- `/api/users/login/`: User authentication
- `/api/orders/`: Order management

## Development

### Adding New Features

1. Create/modify models in `base/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Update serializers in `base/serializer.py`
5. Create/modify views in `base/views.py`
6. Update URL routes in `base/urls.py`

## Deployment

For production deployment:

1. Set `DEBUG=False` in `backend/settings.py`
2. Configure a production database (PostgreSQL recommended)
3. Set up proper environment variables for sensitive information
4. Configure static files serving
5. Use a production-ready web server (Gunicorn, uWSGI)

## License

[MIT License](LICENSE)
