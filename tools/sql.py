import json
from pathlib import Path

from database import Database
from sql_guard import validate_sql



db = Database()



def execute_sql(sql: str):
    """
    Exécute une requête SQL après validation.
    """

    validate_sql(sql)

    return db.execute_select(sql)



def get_schema():
    """
    Retourne le schéma de la base Dolibarr.
    """

    schema_path = (
        Path(__file__)
        .parent
        .parent
        / "schema"
        / "schema.json"
    )


    if not schema_path.exists():

        raise FileNotFoundError(
            "schema.json introuvable. "
            "Lance d'abord generate_schema.py"
        )


    with open(
        schema_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)