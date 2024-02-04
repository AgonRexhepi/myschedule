# My Schedule APP

A simple web application built on the Django framework with the Django Rest Framework for managing events. This application provides functionality to create, view, edit, and delete basic events through a user-friendly interface.

## Features

- **Event Operations:**
  - Create new events with details such as title, description, start date, and end date.
  - View a calendar displaying existing events for a month.
  - Edit existing events to update their information.
  - Delete events to remove them from the system.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Python](https://www.python.org/downloads/) (version X.X.X)
- [Pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) (Optional but recommended)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/AgonRexhepi/myschedule.git
    ```

2. Navigate to the project directory:

    ```bash
    cd myschedule_app
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

2. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

### Running the Server

Start the development server:

```bash
python manage.py runserver
```

Access the application at http://127.0.0.1:8000/.

Access the Django admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials.

Running Tests
To run the tests, execute the following command:

```bash
python manage.py test
```

# API Endpoints

## All Events

- **Endpoint:** `/events/`
- **Method:** GET

## Create Event

- **Endpoint:** `/events/create/`
- **Method:** POST

## Retrieve Event

- **Endpoint:** `/events/<int:pk>/`
- **Method:** GET

## Update Event

- **Endpoint:** `/events/<int:pk>/`
- **Method:** PUT

## Delete Event

- **Endpoint:** `/events/<int:pk>/`
- **Method:** DELETE


# Sources

## Bootstrap

- **Documentation:** [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

## Fullcalendar

- **Demos:** [Fullcalendar Demos](https://fullcalendar.io/demos)

## CDNJS Fullcalendar

- **Library:** [CDNJS Fullcalendar](https://cdnjs.com/libraries/fullcalendar/3.9.0)
