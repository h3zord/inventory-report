from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".xml"):
            with open(path, encoding="utf-8") as file:
                objElementTree = ElementTree.fromstring(file.read())
                data = [
                    {item.tag: item.text for item in record}
                    for record in objElementTree
                ]
            return data

        raise ValueError("Arquivo inválido")
