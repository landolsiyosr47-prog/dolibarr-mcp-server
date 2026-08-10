"""
dolibarr_client.py

Client REST API Dolibarr
"""

import os
import json
import requests
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


DOLIBARR_URL = os.getenv("DOLIBARR_URL")

DOLIBARR_KEY = (
    os.getenv("DOLIBARR_KEY")
    or os.getenv("DOLIBARR_TOKEN")
)


if not DOLIBARR_URL or not DOLIBARR_KEY:
    raise RuntimeError(
        "DOLIBARR_URL et DOLIBARR_KEY/DOLIBARR_TOKEN "
        "doivent être définis dans le fichier .env"
    )



class DolibarrClient:


    def __init__(self):

        self.url = DOLIBARR_URL.rstrip("/")

        self.headers = {
            "DOLAPIKEY": DOLIBARR_KEY,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Accept-Encoding": "identity"
        }

        self.timeout = 30



    def _build_url(self, endpoint):

        return f"{self.url}/{endpoint.lstrip('/')}"



    def _clean_php_warnings(self, text):

        """
        Supprime les warnings PHP envoyés avant le JSON.
        """

        if not isinstance(text, str):
            return text


        if "<br" in text:

            parts = text.split("<br")

            # garde seulement la partie JSON
            text = parts[-1]


        if "<b>Warning</b>" in text:

            return ""


        return text.strip()



    def _parse_response(
        self,
        response,
        method=None,
        data=None
    ):


        if not response.ok:

            print("\n================================")
            print("        ERREUR DOLIBARR API")
            print("================================")
            print("Méthode :", method)
            print("URL :", response.url)
            print("Code HTTP :", response.status_code)
            print("Données envoyées :", data)
            print("Réponse :")
            print(response.text)
            print("================================\n")


        response.raise_for_status()


        if response.status_code == 204 or not response.content:

            return None


        text = self._clean_php_warnings(
            response.text
        )


        if not text:

            return None


        try:

            return json.loads(text)


        except json.JSONDecodeError:

            return text



    def get(self, endpoint):

        response = requests.get(
            self._build_url(endpoint),
            headers=self.headers,
            timeout=self.timeout
        )

        return self._parse_response(
            response,
            method="GET"
        )



    def post(self, endpoint, data):

        response = requests.post(
            self._build_url(endpoint),
            headers=self.headers,
            json=data,
            timeout=self.timeout
        )

        return self._parse_response(
            response,
            method="POST",
            data=data
        )



    def put(self, endpoint, data):

        response = requests.put(
            self._build_url(endpoint),
            headers=self.headers,
            json=data,
            timeout=self.timeout
        )

        return self._parse_response(
            response,
            method="PUT",
            data=data
        )



    def delete(self, endpoint):

        response = requests.delete(
            self._build_url(endpoint),
            headers=self.headers,
            timeout=self.timeout
        )

        return self._parse_response(
            response,
            method="DELETE"
        )



# Instance globale utilisée par les tools MCP

client = DolibarrClient()