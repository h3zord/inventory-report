
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        with open(path, encoding="utf-8") as file:
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            if (".csv" in path):
                data = [product for product in products]
            if (".json" in path):
                data = json.load(file)

        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)
