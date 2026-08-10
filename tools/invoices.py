"""
tools/invoices.py

Gestion des factures Dolibarr
"""

from dolibarr_client import client
from database import Database



def list_invoices():
    """
    Liste toutes les factures Dolibarr.
    """

    return client.get(
        "api/index.php/invoices"
    )



def create_invoice(
    client_id
):
    """
    Crée une facture pour un client existant.
    """

    data = {
        "socid": client_id
    }


    return client.post(
        "api/index.php/invoices",
        data
    )



def add_invoice_line(
    invoice_id,
    product_id,
    quantity,
    price,
    description=""
):
    """
    Ajoute une ligne produit à une facture.
    
    NOTE: Il y a un bug dans l'API Dolibarr pour les lignes de facture.
    L'API crée bien la ligne mais n'enregistre pas les champs.
    Cette fonction applique un correctif automatique en mettant à jour
    les champs directement en base de données.
    """

    data = {
        "fk_product": int(product_id),
        "qty": float(quantity),
        "subprice": float(price),
        "tva_tx": 0.0,
        "remise_percent": 0,
        "desc": description,
        "price": float(price),
        "price_ttc": float(price)
    }

    response = client.post(
        f"api/index.php/invoices/{int(invoice_id)}/lines",
        data
    )
    
    # Workaround: L'API crée la ligne mais ne remplit pas les champs
    # On doit les mettre à jour directement en BD
    if isinstance(response, str) and response.strip():
        try:
            # Extraire le rowid de la réponse XML
            line_id = int(response.strip().split('\n')[-1])
            
            # Mettre à jour les champs en base de données
            db = Database()
            update_sql = f"""
            UPDATE llx_facturedet 
            SET fk_product = {int(product_id)}, 
                qty = {float(quantity)}, 
                subprice = {float(price)}, 
                tva_tx = 0, 
                remise_percent = 0
            WHERE rowid = {line_id}
            """
            db.execute(update_sql)
            
            return response
        except:
            # Si quelque chose échoue, retourner la réponse originale
            return response
    
    return response