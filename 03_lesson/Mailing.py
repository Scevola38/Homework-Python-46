class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} Из: {self.from_address}"
                f" В: {self.to_address}. Стоимость {self.cost} рублей")
