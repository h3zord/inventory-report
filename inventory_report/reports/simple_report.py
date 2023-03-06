from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def __fabricacao_mais_antiga(products):
        datas_fabricacao = [
            date.fromisoformat(product["data_de_fabricacao"])
            for product in products
        ]
        return min(datas_fabricacao)

    @staticmethod
    def validade_mais_proxima(products):
        now = date.today()
        datas_validade = [
            date.fromisoformat(product["data_de_validade"])
            for product in products
        ]
        return min(data for data in datas_validade if data >= now)

    @staticmethod
    def empresa_com_mais_produtos(products):
        dict_empresas = Counter([
            product["nome_da_empresa"] for product in products])

        empresa_mais_frequente = dict_empresas.most_common()[0][0]
        return empresa_mais_frequente

    @staticmethod
    def generate(data_list):
        data_fabricacao = SimpleReport.__fabricacao_mais_antiga(data_list)
        data_validade = SimpleReport.validade_mais_proxima(data_list)
        empresa = SimpleReport.empresa_com_mais_produtos(data_list)
        return (
            f"Data de fabricação mais antiga: {data_fabricacao}\n"
            f"Data de validade mais próxima: {data_validade}\n"
            f"Empresa com mais produtos: {empresa}"
        )
