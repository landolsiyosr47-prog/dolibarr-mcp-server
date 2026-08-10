"""
tools/orders.py

Gestion des commandes Dolibarr
"""

from datetime import datetime
from dolibarr_client import client



def list_orders():
    """
    Liste toutes les commandes Dolibarr.
    """

    return client.get(
        "api/index.php/orders"
    )



def create_order(
    client_id
):
    """
    Crée une commande pour un client existant.
    """

    data = {
        "socid": client_id,
        "date": int(datetime.now().timestamp())
    }


    return client.post(
        "api/index.php/orders",
        data
    )