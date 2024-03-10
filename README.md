# Django cbvCourses Management System

The Django cbvCourses Management System is a web application designed to facilitate the management of course details efficiently. Built using Django's **class-based views**, it offers a comprehensive solution for handling course information, including creation, viewing, updating, and deletion of course records.

## Prerequisites

Ensure you have the following installed:

- Python (3.x recommended)
- Django (5.0.2 used in this project)
- Django REST framework
- PostgreSQL (or any other database you prefer, with respective settings adjustments)

## Setup and Installation

Follow these steps to set up and install the cbvCourses Management System:

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd cbvCourses
    ```

2. **Install required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the database:**

    Edit the `settings.py` file to update your database settings under the `DATABASES` configuration.

    Example for PostgreSQL:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'yourdatabasename',
            'USER': 'postgres',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': 'yourportnumber',
        }
    }
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Creating a Superuser:**

    To access the Django admin panel and perform administrative tasks, you need to create a superuser account. Run the following command:

    ```bash
    python manage.py createsuperuser
    ```

6. **Running the Server:**

    To start the development server and run the application locally, navigate to the project directory and execute the following command:

    ```bash
    python manage.py runserver
    ```

7. **Accessing the Application:**

     After launching the server, navigate to [http://localhost:8000/](http://localhost:8000/) in your preferred web browser. From there, you'll be able to create, read, update, and delete passenger details using the provided class-based views.

## Testing with Postman

You can also test the API endpoints using Postman:

1. Open Postman and create a new request.
2. Set the request type (GET, POST, PUT, DELETE) and enter the appropriate endpoint URL.
3. Add any necessary headers or request body parameters.
4. Send the request and inspect the response.

## Admin Interface

Access the Django admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) to perform administrative tasks, such as managing users and course data.

## API Endpoints

The cbvCourses Management System offers the following API endpoints for interaction with course data:

- **List Courses**: `/courses/` (GET)
- **Create Course**: `/courses/` (POST)
- **Retrieve Course**: `/courses/<course_id>/` (GET)
- **Update Course**: `/courses/<course_id>/` (PUT, PATCH)
- **Delete Course**: `/courses/<course_id>/` (DELETE)

Replace `<course_id>` with the ID of the course you want to retrieve, update, or delete.

## SQL Queries and Sample Data

To help you get started with testing or exploring the database structure, I've provided a SQL file (`Course_info.sql`) with sample queries and data.

