# unnamed-food-project

## How to work with

### Requirements

- uv
- docker

### Instructions

Make an .env file in the root folder.

```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
SECRET_KEY=not implemented
```

Move to /backend and run 'uv venv' to install uv environment.

To establish database:

- Start the database container: `docker compose up -d db`
- Apply the database models to your instance, run this from the backend folder: `uv run python -m db.init_db`

To launch backend api, run this command from the backend folder: `uv run fastapi dev main.py`


## Structure

### Backend

#### Models

Feature based structure.

- Each feature has its own folder under 'modules'.
- Each folder contains logic related to that feature
    - router.py: API routes
    - models.py: Database models
    - service.py: Business logic
    - schemas.py: Pydantic models
    - crud.py: Optional place to keep interactions with the database.

Database models are defined using SQLAlchemy.

#### Core

- config.py: Configuration logic (empty atm)
- database.py: Logic to connect to and utilize database.
- security.py: Stuff for authentication and security stuff.

#### Api

- deps.py: 
- router.py: Gathers the routers from modules and supplies it to the router in main.py

#### Database

- base.py: Defines the SQLAlchemy Base from declarative_base to reuse in the project.
- init_db.py: Initializes the database.

### Frontend

#### Reflex_mat_app

- app.py
- state.py

##### Pages

- index.py

##### 