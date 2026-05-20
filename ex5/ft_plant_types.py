class Plant:
    def __init__(self, name, height, age, growthrate):
        self._name = name
        self._grate = growthrate
        if height < 0:
            print("Error, height can't be negative")
            print("Height initialization rejected")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print("Error, age can't be negative")
            print("Age initialization rejected")
            self._age = 0
        else:
            self._age = age

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self):
        self._height = round(self._height + self._grate, 2)

    def aging(self):
        self._age += 1

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height
        print(f"Height updated: {round(new_height)}cm")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected\n")
            return
        self._age = new_age
        print(f"Age updated: {new_age} days\n")


class Flower(Plant):
    def __init__(self, name, height, age, growthrate, color):
        super().__init__(name, height, age, growthrate)
        self._color = color
        self._bloom = 0

    def show(self):
        super().show()
        print(" Color:", self._color)
        if self._bloom == 1:
            print(f" {self.get_name()} is blooming beautifully!")
        else:
            print(f" {self.get_name()} has not bloomed yet")

    def bloom(self):
        self._bloom = 1


class Tree(Plant):
    def __init__(self, name, height, age, growthrate, diameter):
        super().__init__(name, height, age, growthrate)
        self._diameter = diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")

    def produce_shade(self):
        a = self._name
        b = self._height
        c = self._diameter
        print(f"Tree {a} now produces a shade of {b}cm long and {c}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, age, growthrate, harvest_season, n_value):
        super().__init__(name, height, age, growthrate)
        self._season = harvest_season
        self._nvalue = n_value

    def show(self):
        super().show()
        print(" Harvest season:", self._season)
        print(" Nutritional value:", self._nvalue)

    def nvalue_increase(self):
        self._nvalue += 1


def main():
    print("=== Garden Plant Types ===\n=== Flower")
    plant1 = Flower("Rose", 15.0, 10, 0.8, "red")
    plant1.show()
    print("[asking the rose to bloom]")
    plant1.bloom()
    plant1.show()
    print("\n=== Tree")
    plant2 = Tree("Oak", 200.0, 365, 100.0, 5.0)
    plant2.show()
    print("[asking the oak to produce shade]")
    plant2.produce_shade()
    plant3 = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0)
    print("\n=== Vegetable")
    plant3.show()
    print("[make tomato grow and age for 20 days]")
    i = 0
    while i < 20:
        plant3.grow()
        plant3.aging()
        plant3.nvalue_increase()
        i += 1
    plant3.show()


if __name__ == "__main__":
    main()
