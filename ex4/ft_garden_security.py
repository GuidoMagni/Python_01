class Plant:
    def __init__(self, name, height, age):
        self._name = name
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
        a = self._name
        b = self._height
        c = self._age
        print(f"Plant created: {a}: {b}cm, {c} days old\n")

    def grow(self):
        self._height = round(self._height + 0.8, 2)

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


def main():
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15.0, 10)
    plant1.show()
    plant1.set_height(25.0)
    plant1.set_age(30)
    plant1.set_height(-42)
    plant1.set_age(-42)
    a = plant1.get_name()
    b = plant1.get_height()
    c = plant1.get_age()
    print(f"Current state: {a}: {b}cm, {c} days old")


if __name__ == "__main__":
    main()
