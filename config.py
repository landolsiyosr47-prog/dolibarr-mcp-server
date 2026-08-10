"""
config.py

Chargement de la configuration du projet
"""

import os
from dotenv import load_dotenv


load_dotenv()



# Dolibarr API

DOLIBARR_URL = os.getenv(
    "DOLIBARR_URL"
)


DOLIBARR_KEY = (
    os.getenv("DOLIBARR_KEY")
    or os.getenv("DOLIBARR_TOKEN")
)



# MariaDB

DB_HOST = os.getenv(
    "DB_HOST",
    "localhost"
)

DB_PORT = int(
    os.getenv(
        "DB_PORT",
        3306
    )
)

DB_USER = os.getenv(
    "DB_USER",
    "root"
)

DB_PASSWORD = os.getenv(
    "DB_PASSWORD",
    ""
)

DB_NAME = os.getenv(
    "DB_NAME",
    "dolibarr"
)



# Vérifications

if not DOLIBARR_URL:

    raise ValueError(
        "La variable DOLIBARR_URL est manquante dans .env"
    )


if not DOLIBARR_KEY:

    raise ValueError(
        "La variable DOLIBARR_KEY ou DOLIBARR_TOKEN est manquante dans .env"
    )