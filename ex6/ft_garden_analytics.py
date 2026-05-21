class Plant:
    def __init__(self, name, height, age, growthrate):
        self._name = name
        self._grate = growthrate
        self._grow = 0
        self._aging = 0
        self._show = 0
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
        self._show += 1

    def grow(self):
        self._height = round(self._height + self._grate, 2)
        self._grow += 1

    def aging(self):
        self._age += 1
        self._aging += 1

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

    @staticmethod
    def check_year(age):
        if age > 365:
            return True
        else:
            return False

    class Stats:
        @staticmethod
        def show_stats(Plant: "Plant"):
            a = Plant._grow
            b = Plant._aging
            c = Plant._show
            print(f"[statistics for {Plant._name}]")
            print(f"Stats: {a} grow, {b} age, {c} show")

    @classmethod
    def anonymous(self):
        return Plant("Unknown plant", 0.0, 0, 0.0)


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
        self._shade = 0

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")

    def produce_shade(self):
        a = self._name
        b = self._height
        c = self._diameter
        self._shade += 1
        print(f"Tree {a} now produces a shade of {b}cm long and {c}cm wide.")

    def show_stats(self):
        super().Stats.show_stats(self)
        print(f"{self._shade} shade")


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


class Seed(Flower):
    def __init__(self, name, height, age, growthrate, color):
        super().__init__(name, height, age, growthrate, color)
        self._bloom = 0
        self.seeds = 0

    def aging(self):
        self._age += 20
        self._aging += 1

    def bloom(self):
        super().bloom()
        if self._bloom == 1:
            self.seeds = 42

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")


def main():
    print("=== Garden statistics ===\n=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.check_year(30))
    print("Is 400 days more than a year? ->", Plant.check_year(400))
    print("\n=== Flower")
    plant1 = Flower("Rose", 15.0, 10, 8.0, "red")
    plant1.show()
    plant1.Stats.show_stats(plant1)
    print("[asking the rose to grow and bloom]")
    plant1.grow()
    plant1.bloom()
    plant1.show()
    plant1.Stats.show_stats(plant1)
    print("\n=== Tree")
    plant2 = Tree("Oak", 200.0, 365, 100.0, 5.0)
    plant2.show()
    plant2.show_stats()
    print("[asking the oak to produce shade]")
    plant2.produce_shade()
    plant2.show_stats()
    plant3 = Seed("Sunflower", 80.0, 45, 30, "yellow")
    print("\n=== Seed")
    plant3.show()
    print("[make sunflower grow, age and bloom]")
    plant3.grow()
    plant3.aging()
    plant3.bloom()
    plant3.show()
    plant3.Stats.show_stats(plant3)
    print("\n=== Anonymous")
    plant4 = Plant.anonymous()
    plant4.show()
    plant4.Stats.show_stats(plant4)


if __name__ == "__main__":
    main()
