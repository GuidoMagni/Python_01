class Plant:
    def __init__(self, name, height, age, growthrate):
        self.name = name
        self.height = height
        self.age = age
        self.grate = growthrate

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height = round(self.height + self.grate, 2)

    def aging(self):
        self.age += 1


def main():
    i = 0
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30, 0.8)
    while (i <= 7):
        i = i + 1
        plant1.show()
        if i == 8:
            break
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.aging()
    print(f"Growth this week: {round(plant1.height - 25, 2)}cm")


if __name__ == "__main__":
    main()
