from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @staticmethod
    def contagem_produtos(data_list):
        lista_empresas = Counter([
            product["nome_da_empresa"] for product in data_list
        ]).items()
        return lista_empresas

    @staticmethod
    def generate(data_list):
        simple_report = SimpleReport.generate(data_list)
        lista_empresas = CompleteReport.contagem_produtos(data_list)

        full_report = simple_report + "\nProdutos estocados por empresa:\n"

        for empresa, quantidade in lista_empresas:
            full_report += f"- {empresa}: {quantidade}\n"

        return full_report
