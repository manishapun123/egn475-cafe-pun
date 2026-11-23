
import sqlite3
import click
from flask import current_app, g


def get_db():
    """Connect to the SQLite database for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"]
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """Close the database connection after the request."""
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Create database tables using schema.sql."""
    db = get_db()

    with current_app.open_resource("schema.sql") as file:
        db.executescript(file.read().decode("utf8"))


@click.command("init-db")
def init_db_command():
    """Initialize the database."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with Flask."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
