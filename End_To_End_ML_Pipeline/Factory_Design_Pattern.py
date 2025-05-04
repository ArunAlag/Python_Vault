from abc import ABC, abstractmethod

#Step 1 : Define the Product Interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Step 2: Implement Concrete Products
class Espresso(Coffee):
    def prepare(self):
        print("Preparing Espresso")

class Latte(Coffee):
    def prepare(self):
        print("Preparing Latte")


class Cappuccino(Coffee):
    def prepare(self):
        print("Preparing Cappuccino")


# Step 3: Implement the factory
class CoffeeMakingMachine:
    def make_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            return Espresso().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        elif coffee_type == "Cappuccino":
            return Cappuccino().prepare()
        else:
            return "Unknown coffee type"


# Step 4: Use the factory to create products
if __name__ == "__main__":
    coffee_maker = CoffeeMakingMachine()

    coffee = coffee_maker.make_coffee("Espresso")
    print(coffee)

    coffee = coffee_maker.make_coffee("Latte")
    print(coffee)

    coffee = coffee_maker.make_coffee("Cappuccino")
    print(coffee)