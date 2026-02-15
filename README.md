# unnamed-food-project

## How to work with

Make an .env file in the root folder.

POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
SECRET_KEY=not implemented

To establish database:

- Start the database container: docker compose up -d db
- Apply the database models to your instance, run this from the backend folder: uv run python -m db.init_db

To launch backend api, run this command from the backend folder: uv run fastapi dev main.py


## Structure

### Backend


Feature based structure.

- Each feature has its own folder
- Each folder contains logic related to that feature
    - router.py: API routes
    - models.py: Database models
    - service.py: Business logic
    - schemas.py: Pydantic models
    - crud.py: Optional place to keep interactions with the database.

Database models are defined using SQLAlchemy.

#### Core

Basic config.

#### Api

- deps.py
- router.py

### Frontend

#### Reflex_mat_app

- app.py
- state.py

##### Pages

- index.py

##### 