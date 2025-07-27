from Address import Address
from Mailing import Mailing

from_address = Address("307171", "Zheleznogorsk", "Gagarina", "32", "45")
to_address = Address("307170", "Zheleznogorsk", "Lenina", "60", "1")
mailing = Mailing(to_address, from_address, "550", "99812009")

print(mailing)
