from animal import Animal

import logging
logger =  logging.getLogger(__name__)

class Dog(Animal):
    dog_count = 0
    def __init__(self, chip_num: int, age: int, race: str, says: str = "Bow Wow"):
        super().__init__(chip_num, age, says)
        self.race = race
        Dog.dog_count +=1

    def _make_sound(self) -> None:
        print(f"This is {self.race}. He is {self.age} and says {self.says}.")

    def do_command(self, command: str):
        if command == "make_sound":
            self._make_sound()

    def go_abroad(self, num: int):
        logger.info(f"Dog is going abroad. Set Chip number to {num}")
        if num < 0:
            raise ValueError("Chip number must be greater than 0")
        self._chip_num = num

    def get_chip_num (self):
        return self._chip_num