from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        'Alexa',
        'Trybe',
        '07/08/1995',
        '07/08/2023',
        '121519',
        'Colocar na geladeira'
    )

    assert new_product.id == 1
    assert new_product.nome_do_produto == 'Alexa'
    assert new_product.nome_da_empresa == 'Trybe'
    assert new_product.data_de_fabricacao == '07/08/1995'
    assert new_product.data_de_validade == '07/08/2023'
    assert new_product.numero_de_serie == '121519'
    assert new_product.instrucoes_de_armazenamento == 'Colocar na geladeira'
