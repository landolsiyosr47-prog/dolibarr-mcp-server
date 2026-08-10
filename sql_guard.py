"""
sql_guard.py

Vérifie qu'une requête SQL respecte les règles de sécurité.
"""

import re



def validate_sql(sql: str) -> bool:
    """
    Vérifie qu'une requête SQL est autorisée.

    Règle actuelle :
    - DELETE est interdit.
    """


    if not sql or not sql.strip():

        raise ValueError(
            "La requête SQL est vide."
        )


    sql = sql.strip()



    # Bloque DELETE peu importe la casse
    if re.search(
        r"\bDELETE\s+FROM\b",
        sql,
        re.IGNORECASE
    ):

        raise ValueError(
            "Les requêtes DELETE sont interdites."
        )


    return True