from sqlalchemy import create_engine, text, inspect
from app.core.config import settings

# Create engine (SQLAlchemy Core — no ORM)
engine = create_engine(settings.DATABASE_URL)


def get_connection():
    """Get a raw database connection."""
    return engine.connect()


def execute_query(sql: str) -> list[dict]:
    """
    Execute a raw SQL query and return results as a list of dicts.
    Raises exception if query fails.
    """
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        columns = result.keys()
        rows = result.fetchall()
        return [dict(zip(columns, row)) for row in rows]


def get_schema_info() -> str:
    """
    Introspect the database and return a schema description string
    for use in the LLM prompt.
    """
    inspector = inspect(engine)
    schema_parts = []

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        col_descriptions = ", ".join(
            f"{col['name']} ({col['type']})" for col in columns
        )
        schema_parts.append(f"Table: {table_name}\n  Columns: {col_descriptions}")

    return "\n\n".join(schema_parts)
