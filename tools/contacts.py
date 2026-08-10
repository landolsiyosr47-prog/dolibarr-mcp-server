"""
tools/contacts.py

Gestion des contacts Dolibarr
"""

from dolibarr_client import client



def list_contacts():
    """
    Liste tous les contacts Dolibarr.
    """

    return client.get(
        "api/index.php/contacts"
    )



def create_contact(
    firstname,
    lastname,
    email="",
    phone=""
):
    """
    Crée un nouveau contact.
    """

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "phone": phone
    }


    return client.post(
        "api/index.php/contacts",
        data
    )



def update_contact(
    contact_id,
    data
):
    """
    Met à jour un contact existant.
    """

    return client.put(
        f"api/index.php/contacts/{contact_id}",
        data
    )
