from smartphone import Smartphone

catalog = []
catalog.append(Smartphone('Apple', 'iPhone 16', '+79997835852'))
catalog.append(Smartphone('Apple', 'iPhone 13 Pro', '+79992318269'))
catalog.append(Smartphone('Samsung', 'Fold 2', '+79998970129'))
catalog.append(Smartphone('Xiaomi', 'Redmi', '+79995435460'))
catalog.append(Smartphone('Google', 'Pixel', '+79994363990'))

for phone in catalog:
    print(f'{phone.brand} — {phone.model_name}. {phone.phone_number}')