# Consider how the plant should change over time when using grow() and age().
# Different plants can evolve differently.
# Think about giving your plants behaviors that will drive grow() differently.
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height = round(self.height + 0.8, 2)

    def aging(self):
        self.age += 1


def main():
    i = 0
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30)
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
