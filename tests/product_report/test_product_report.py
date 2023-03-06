from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Water",
        "Crystal",
        "07/08/2022",
        "07/08/2023",
        "QWERTY16",
        "na geladeira"
    )

    assert str(product.__repr__()) == (
        "O produto Water"
        " fabricado em 07/08/2022"
        " por Crystal com validade"
        " até 07/08/2023"
        " precisa ser armazenado na geladeira."
    )
