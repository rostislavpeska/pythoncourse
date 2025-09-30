class Dog:
    dog_count = 0
    def __init__(self, id: int, race: str, age: int, says: str) -> None:
        self.id = id
        self.race = race
        self.age = age
        self.says = says
        Dog.dog_count +=1

    def bark(self) -> None:
        print(f"This is {self.race}. He is {self.age} and says {self.says}.")
"""
    def __del__(self) -> None:
        Dog.dog_count -= 1
"""