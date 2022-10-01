class Investment:
    def __init__(self, stavka, summa):
        self.stavka = stavka
        self.summa = summa

    def value_after(self, n):
        return(self.summa*(1+(self.stavka/100))**n)
    def __str__(self):
        return (f"summa {self.summa} and stavka {self.stavka}")

stavka = int(input())
summa = int(input())
period = int(input())

deposit1 = Investment(stavka, summa)
print(deposit1.value_after(period))
