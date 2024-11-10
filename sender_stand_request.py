import requests

# Артём Сухов, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import data


def post_create_order(order_body):
    header_copy = data.headers.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body,
                         headers=header_copy)

# получить заказ по треку
def get_track_order(params):
    return requests.get(
        configuration.URL_SERVICE + configuration.REQUEST_ORDER,
        headers=data.headers,
        params=params
    )