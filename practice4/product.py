class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    def get_price(self, n):
        if n<10:
            return self.price
        elif n>9 and n<100:
            return self.price * 0.9
        elif n>=100:
            return self.price * 0.8
    def make_purchase(self, m):
        if m>self.amount:
            return f"We do not have enough {self.name}"
        else:
            return self.get_price(m)*m


candy = Product("candy", 90, 100)
chocolate = Product("chocolate", 500, 650)
apple = Product("apple", 100, 450)
water = Product("water", 400, 250)
ginger = Product("ginger", 200, 1500)
milk = Product("milk", 160, 360)
lemon = Product("lemon", 60, 150)

products = [candy, chocolate, apple, water, ginger, milk, lemon]

number_of_products = int(input())
grocery = []
for i in range(number_of_products):
    product = input().split()
    grocery.append(product)

total_price = 0

for item in grocery:
    for jtem in products:
        if item[0] == jtem.name:
            if int(item[1])>jtem.amount:
                print(f"we do not have enough {item[0]}")
            else:
                print(f"{item[0]} {item[1]} {jtem.make_purchase(int(item[1]))}", end = "\n")
                total_price += jtem.make_purchase(int(item[1]))

print(f"total price: {total_price}")









