# init_manual.py
from fleets import create_app
from fleets.db import init_db

app = create_app()
with app.app_context():
    init_db()