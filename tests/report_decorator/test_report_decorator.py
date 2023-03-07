from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)

    assert colored_report.generate([{
        "id": "1",
        "nome_do_produto": "Water",
        "nome_da_empresa": "Crystal",
        "data_de_fabricacao": "2022-08-07",
        "data_de_validade": "2023-08-07",
        "numero_de_serie": "QWERTY16",
        "instrucoes_de_armazenamento": "na geladeira",
    }]) == (
        "\x1b[32mData de fabricação mais antiga:\x1b[0m "
        "\x1b[36m2022-08-07\x1b[0m\n"
        "\x1b[32mData de validade mais próxima:\x1b[0m "
        "\x1b[36m2023-08-07\x1b[0m\n"
        "\x1b[32mEmpresa com mais produtos:\x1b[0m "
        "\x1b[31mCrystal\x1b[0m"
    )
