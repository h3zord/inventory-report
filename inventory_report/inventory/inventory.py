from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path: str, report_type):
        if path.endswith(".csv"):
            data = CsvImporter().import_data(path)
        if path.endswith(".json"):
            data = JsonImporter().import_data(path)
        if path.endswith(".xml"):
            data = XmlImporter().import_data(path)

        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
