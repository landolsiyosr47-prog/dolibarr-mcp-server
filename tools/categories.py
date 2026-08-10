"""
tools/categories.py

Gestion des catégories Dolibarr
"""

from dolibarr_client import client



def list_categories():
    """
    Liste toutes les catégories Dolibarr.
    """

    return client.get(
        "api/index.php/categories"
    )



def create_category(
    label,
    category_type=5
):
    """
    Crée une nouvelle catégorie.
    
    category_type: 1=produits, 2=clients, 3=contacts, 
                   4=commandes, 5=factures (défaut), etc.
    """

    data = {
        "label": label,
        "type": category_type
    }


    return client.post(
        "api/index.php/categories",
        data
    )