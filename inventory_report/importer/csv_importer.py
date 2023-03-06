from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                products = csv.DictReader(file, delimiter=",", quotechar='"')
                data = [product for product in products]
                return data

        raise ValueError("Arquivo inválido")
