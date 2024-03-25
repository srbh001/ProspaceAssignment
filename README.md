
# ProSpace Assignment 

## Structure Overview
- The project includes models for handling classes, assignments, and questions related to those assignments.
- Two main models are involved: `Class` and `Assignment`.
- The `Class` model represents different classes with a section identifier.
- The `Assignment` model represents an assignment with a title, description, due date, associated class, teacher, and total marks.
- Additionally, there is a `Question` model that represents questions related to an assignment.

## Authorization
- Authorization and access control are managed through the `Teacher` and `Student` models.
- Token-based authentication is implemented using Django REST Framework's Token Authentication.
- The authorization logic is handled in the `views.py` file of the authentication app.

## APIs
- The URLs and corresponding views for handling classes and assignments are defined in the `urls.py` file.
- The APIs available for this project include:
  - `/classes`: Endpoint for viewing all classes.
  - `/class/<uuid:class_id>`: Endpoint for viewing a specific class identified by its UUID.
  - `/assignments`: Endpoint for viewing all assignments.
  - `/assignment/<uuid:assignment_id>`: Endpoint for viewing a specific assignment identified by its UUID.

## Example APIs
- To access these APIs, assuming a Django development server with token authentication:
  - For registering a new student: `POST /api/auth/student/register/`
  - For registering a new teacher: `POST /api/auth/teacher/register/`
  - For logging in and getting a token: `POST /api-token-auth/`

## Note
- The provided code snippet focuses on the model, URL routing, and authentication aspects.
- Token authentication requires sending a valid token in the request headers for authorized API access.
- Additional views and logic may be required for managing permissions and roles within the system.


## Runnig the Project

- Clone the repository
- Install pipenv if not installed using `pip install pipenv`
- Create a virtual environment using `pipenv shell`
- Install the dependencies using `pipenv install`
- Run the server using `python manage.py runserver`

