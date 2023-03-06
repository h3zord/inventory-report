
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from xml.etree import ElementTree
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
            if (".xml" in path):
                objElementTree = ElementTree.fromstring(file.read())
                data = [
                    {item.tag: item.text for item in record}
                    for record in objElementTree
                ]

        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
