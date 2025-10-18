# Project Management Tool

This is a simple project management tool built with Python (Flask) and React.

## How to Run the Project

### Backend

1. Navigate to the `backend` directory: `cd project_management_tool/backend`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Set up your MySQL database and update the database URI in `app.py`.
6. Run the application: `python app.py`

### Frontend

1. Navigate to the `frontend` directory: `cd project_management_tool/frontend`
2. Install the dependencies: `npm install`
3. Run the application: `npm start`

## API Endpoints

### Projects

- `GET /projects`: Get all projects
- `POST /projects`: Create a new project
- `PUT /projects/<id>`: Update a project
- `DELETE /projects/<id>`: Delete a project

### Tasks

- `GET /projects/<id>/tasks`: Get all tasks for a project
- `POST /projects/<id>/tasks`: Create a new task for a project
- `PUT /tasks/<id>`: Update a task
- `DELETE /tasks/<id>`: Delete a task
