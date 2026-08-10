"""
tools/products.py

Gestion des produits/services Dolibarr
"""

from dolibarr_client import client



def list_products():
    """
    Liste tous les produits/services.
    """

    return client.get(
        "api/index.php/products"
    )



def create_product(
    ref,
    label,
    price,
    description=""
):
    """
    Crée un nouveau produit/service.
    """

    data = {
        "ref": ref,
        "label": label,
        "price": price,
        "price_base_type": "HT",
        "type": 0,
        "status": 1,
        "description": description
    }


    return client.post(
        "api/index.php/products",
        data
    )



def update_product(
    product_id,
    data
):
    """
    Modifie un produit/service existant.
    """

    return client.put(
        f"api/index.php/products/{product_id}",
        data
    )
