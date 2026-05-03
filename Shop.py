from dataclasses import dataclass


@dataclass()
class Product:
    name: str
    _price: float

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

    def discount(self, pr):
        return self.price * (100 - pr) / 100

    def __str__(self):
        return f'{self.name}: {self._price} руб.'


@dataclass()
class DigitalProduct(Product):
    file_size: float

    def download_info(self):
        return f'Скачать: {self.name} ({self.file_size} МБ)'


@dataclass()
class PhysicalProduct(Product):
    weight: float

    def shipping_cost(self):
        return self.weight * 50

    def total_price(self):
        return self.price + self.shipping_cost()


@dataclass()
class Cart:
    c: list

    def add(self, item):
        self.c.append(item)

    def remove(self, name):
        for i in range(len(self.c)):
            if self.c[i].name == name:
                del self.c[i]
                break

    def total(self):
        a = 0
        for i in self.c:
            if isinstance(i, PhysicalProduct):
                a += i.total_price()
            else:
                a += i.price
        return a

    def __len__(self):
        return len(self.c)

    def __str__(self):
        return '\n'.join(str(i) for i in self.c)
