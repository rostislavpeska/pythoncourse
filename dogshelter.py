from dog import Dog

class DogShelter:
    def __init__(self, animals: list[Dog]) -> None:
        self.animals = animals

    def bark_all(self) -> None :
        for animal in self.animals:
            animal.bark()
"""
    def remove_dog_by_id(self, dog_id: int) -> None:
        self.dog = [d for d in self.animals if d.id != dog_id]
"""