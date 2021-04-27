from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        print("if i have venom i'm going to use it")

    def moving(self):
        print("moving but as a snake")

    def __repr__(self):
        return f"This is a reptile"

    def __str__(self):
        return f"str version of this is reptile"

bob = Reptile()
print(bob)