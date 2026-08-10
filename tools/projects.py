"""
tools/projects.py

Gestion des projets Dolibarr
"""

from dolibarr_client import client



def list_projects():
    """
    Liste tous les projets Dolibarr.
    """

    return client.get(
        "api/index.php/projects"
    )



def create_project(
    title,
    description=""
):
    """
    Crée un nouveau projet Dolibarr.
    """

    data = {
        "ref": "PRJ-001",
        "title": title,
        "description": description,
        "public": 1
    }


    return client.post(
        "api/index.php/projects",
        data
    )