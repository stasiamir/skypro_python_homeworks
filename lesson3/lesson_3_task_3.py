from address import Address
from mailing import Mailing

to_address = 127521, "г. Москва", "ул. Шереметьевская", 13, 115
from_address = 195112, "г. Санкт-Петербург", "пр-кт Новочеркасский", 26, 112
cost = 1450
track = 123456789

sending = Mailing
sending (to_address, from_address, 1450, 1234567890)

print("Отправление", track, "из", from_address,"в", to_address, ". Стоимость", cost, "рублей.")