from animal import Animal

class Cat(Animal):
    def __init__(self, chip_num: int,  age: int, race: str, says: str = "Meow"):
        super().__init__(chip_num, age, says)
        self.race = race

    def _make_sound(self) -> None:
        print(f"This is {self.race}. She is {self.age} and says {self.says}.")

    def do_command(self, command: str):
        if command == "make_sound":
            self._make_sound()