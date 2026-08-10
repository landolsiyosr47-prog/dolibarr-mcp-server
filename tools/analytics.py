"""
tools/analytics.py

Statistiques et analyses Dolibarr
"""

from database import Database


db = Database()



def get_total_clients():
    """
    Retourne le nombre total de clients.
    """

    sql = """
    SELECT COUNT(*) AS total
    FROM llx_societe
    WHERE client > 0
    """

    return db.execute_select(sql)



def get_total_invoices():
    """
    Retourne le nombre total de factures.
    """

    sql = """
    SELECT COUNT(*) AS total
    FROM llx_facture
    """

    return db.execute_select(sql)



def get_turnover():
    """
    Retourne le chiffre d'affaires total.
    """

    sql = """
    SELECT SUM(total_ht) AS turnover
    FROM llx_facture
    """

    return db.execute_select(sql)



def get_best_customers():
    """
    Retourne les 10 meilleurs clients
    selon le chiffre d'affaires.
    """

    sql = """
    SELECT
        s.nom,
        SUM(f.total_ht) AS turnover

    FROM llx_societe s

    JOIN llx_facture f
        ON s.rowid = f.fk_soc

    GROUP BY s.rowid

    ORDER BY turnover DESC

    LIMIT 10
    """

    return db.execute_select(sql)



def get_last_invoices():
    """
    Retourne les 10 dernières factures.
    """

    sql = """
    SELECT
        ref,
        datef,
        total_ht

    FROM llx_facture

    ORDER BY datef DESC

    LIMIT 10
    """

    return db.execute_select(sql)



def get_last_clients():
    """
    Retourne les 10 derniers clients créés.
    """

    sql = """
    SELECT
        rowid,
        nom

    FROM llx_societe

    ORDER BY rowid DESC

    LIMIT 10
    """

    return db.execute_select(sql)