## Getting Started

- Clone the repository
- Set up the virtual environment
    `python -m venv .venv`
- Activate the virtual environment
    `source .venv/bin/activate`
- Install the dependencies from `requirements.txt`
    `pip install -r requirements.txt`
- Create a database called `phewa_lake` in PostgreSQL
- Create an `.env` as show in `.env.example`
- Run `flask db init` and `flask db upgrade` for database migration
- Run `python3 seed_pollution_data.py` to seed database
- Run `flask run` to run the app
