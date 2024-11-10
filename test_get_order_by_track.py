# Галушко Владимир, 23-я когорта, дипломный проект

import data
import sender_stand_request

#создание заказа
def create_order():
    response = sender_stand_request.post_create_order(data.order_body)
    new_order_track = response.json().get("track")
    return new_order_track


# проверка трека заказа
def positive_assert():
    order_track = create_order()
    params = {"t": order_track}
    response = sender_stand_request.get_track_order(params)

    assert response.status_code == 200


def test_get_order():
    positive_assert()
# не получается вместить в одну функцию (как я понял из комментария) только двумя на создание и получение и проверку