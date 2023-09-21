import metods
import params

import requests
import allure

@allure.title('Проверка корзины')
@allure.description('Проверка на то, что по умолчанию корзина пуста')
def test_basket():
    response = requests.get(metods.basket_info, params=params.par_basket_info)
    products_list = response.json()["products"]
    print(response.json())
    print(products_list)
    assert products_list == []