from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def importer(path: str):
    if path.endswith(".csv"):
        return InventoryRefactor(CsvImporter)
    if path.endswith(".json"):
        return InventoryRefactor(JsonImporter)
    if path.endswith(".xml"):
        return InventoryRefactor(XmlImporter)


def main():
    try:
        if len(sys.argv) < 3:
            raise ValueError("Verifique os argumentos")

        inventory = importer(sys.argv[1])
        report = inventory.import_data(sys.argv[1], sys.argv[2])
        sys.stdout.write(report)
    except ValueError as exc:
        print(exc, file=sys.stderr)
