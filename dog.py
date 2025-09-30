class Dog:
    def __init__(self, race: str, age: int, says: str) -> None:
        self.race = race
        self.age = age
        self.says = says

    def bark(self) -> None:
        print(f"This is {self.race}. He is {self.age} and says {self.says}.")