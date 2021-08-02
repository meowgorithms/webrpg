"""
Provides ez DB queries
"""
from app import db


def get_base_stats(archetype_name: str):
    query_string = f"""
    SELECT *
    FROM base_stats
    WHERE archetype = '{archetype_name}'
    """

    with db.engine.connect() as conn:
        result = conn.execute(query_string).fetchone()

    return result
