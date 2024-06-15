from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "Iphone 14", "+79101448989")
phone2 = Smartphone("Nokia", "3310", "+79101234567")
phone3 = Smartphone("Apple", "Iphone 12 Pro Max", "+79101449090")
phone4 = Smartphone("Siemens", "A65", "+79101509898")
phone5 = Smartphone("Sony Ericsson", "K750i", "+79201668080")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.number}")