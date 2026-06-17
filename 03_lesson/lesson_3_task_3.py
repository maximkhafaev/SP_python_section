from address import Address
from mailing import Mailing

from_ = Address('673332', 'Кайдалово', 'переулок Южный', '120', '40')
to_ = Address('164694', 'Палащелье', 'проспект Космонавтов', '9', '108')

mail = Mailing(to_, from_, 359.99, '444148160')

print(f'Отправление {mail.track} из {mail.from_address.getAddress()} в {mail.to_address.getAddress()}. Стоимость {mail.cost} рублей.')