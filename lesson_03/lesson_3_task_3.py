from address import Address
from mailing import Mailing

to_address = Address("190000", "Санкт-Петербург", "Невский пр.", "10", "5")
from_address = Address("101000", "Москва", "Тверская", "7", "12")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track="RA123456789RU",
)

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.postcode}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.postcode}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
