# Foodie - Food Sharing Platform

Foodie is a Django-based web application that allows users to share and discover food items. Users can post food items with images, descriptions, and prices, creating a community-driven platform for food enthusiasts.

## Features

- User authentication and authorization
- Post food items with images
- View detailed food listings
- Responsive design with Bootstrap
- Image upload and storage
- Price and description management

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd django-projects
```

2. Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install django
pip install pillow  # for image handling
```

4. Set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin account):

```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:

```bash
python manage.py runserver
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:8000/
```

## Project Structure

- `mysite/` - Main project directory
  - `foodie/` - Main application directory
    - `templates/` - HTML templates
    - `static/` - Static files (CSS, JS, images)
  - `media/` - User-uploaded media files
  - `users/` - User management app
  - `manage.py` - Django management script

## Notes

This is a learning repo, the idea behind it is to apply what I've studying.
