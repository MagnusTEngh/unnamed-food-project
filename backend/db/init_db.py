"""To run this, run the command 'uv run python -m db.init_db'"""

from db.base import Base
from core.database import engine

from modules.nutrients import models
from modules.test import models


print("Connecting to database...")
Base.metadata.create_all(engine)
print("Tables created successfully!")
