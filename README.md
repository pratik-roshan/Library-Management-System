# Library Management System

## Setup Instructions

### Prerequisites

- Python 3.6+
- MySQL database server
- Virtual environment

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/library-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd library-management-system
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Configure the database:

    - Create a MySQL database.
    - Update the `DATABASES` settings in `library_management_system/settings.py` with your database credentials.

5. Apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

The project should now be running at `http://localhost:8000/`.

## API Documentation

### User APIs

#### Create a New User

- **Endpoint:** `/lib/users/create/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "Name": "John Doe",
        "Email": "john@example.com",
        "MembershipDate": "2022-02-01"
    }
    ```
- **Response:**
    ```json
    {
        "UserID": 1,
        "Name": "John Doe",
        "Email": "john@example.com",
        "MembershipDate": "2022-02-01"
    }
    ```

#### List All Users

- **Endpoint:** `/lib/users/list/`
- **Method:** `GET`
- **Response:**
    ```json
    [
        {
            "UserID": 1,
            "Name": "John Doe",
            "Email": "john@example.com",
            "MembershipDate": "2022-02-01"
        },
        // ... other users
    ]
    ```

#### Get User by ID

- **Endpoint:** `/lib/users/{user_id}/`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "UserID": 1,
        "Name": "John Doe",
        "Email": "john@example.com",
        "MembershipDate": "2022-02-01"
    }
    ```

### Book APIs

#### Add a New Book

- **Endpoint:** `/lib/books/add/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "Title": "The Catcher in the Rye",
        "ISBN": "978-0-316-76948-0",
        "PublishedDate": "1951-07-16",
        "Genre": "Fiction"
    }
    ```
- **Response:**
    ```json
    {
        "BookID": 1,
        "Title": "The Catcher in the Rye",
        "ISBN": "978-0-316-76948-0",
        "PublishedDate": "1951-07-16",
        "Genre": "Fiction"
    }
    ```
