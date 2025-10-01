from abc import abstractmethod, ABC

class Animal (ABC):
    def __init__(self, chip_num: int,  age: int, says: str = "...") -> None:
        self._chip_num = chip_num
        self.age = age
        self.says = says

    @abstractmethod
    def _make_sound(self) -> None:
        print(f"This is an animal. It is {self.age} and says {self.says}.")

    def do_command(self, command: str):
        if command == "make_sound":
            self._make_sound()

...