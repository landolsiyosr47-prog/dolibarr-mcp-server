from pathlib import Path
import json


class SQLGenerator:

    def __init__(self):
        self.schema = self._load_schema()
        self.prompt = self._load_prompt()

    def _load_schema(self):
        with open("schema/schema.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def _load_prompt(self):
        return Path("prompts/sql_prompt.txt").read_text(
            encoding="utf-8"
        )

    def generate(self, question: str):
        """
        Cette méthode appellera plus tard le LLM
        pour transformer une question
        en requête SQL.
        """
        raise NotImplementedError(
            "LLM not connected yet."
        )
