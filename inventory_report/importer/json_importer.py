from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".json"):
            with open(path, encoding="utf-8") as file:
                data = json.load(file)
                return data

        raise ValueError("Arquivo inválido")
