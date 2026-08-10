"""
tools/clients.py

Gestion des clients Dolibarr (thirdparties)
"""

from dolibarr_client import client



def list_clients():
    """
    Liste tous les tiers Dolibarr.
    """

    return client.get(
        "api/index.php/thirdparties"
    )



def create_client(
    name,
    email="",
    phone=""
):
    """
    Crée un nouveau client.
    """

    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "client": 1
    }


    return client.post(
        "api/index.php/thirdparties",
        data
    )



def update_client(
    client_id,
    data
):
    """
    Modifie un client existant.
    """

    return client.put(
        f"api/index.php/thirdparties/{client_id}",
        data
    )



