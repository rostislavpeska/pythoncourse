from dog import Dog

class DogShelter:
    def __init__(self, animals: list[Dog]) -> None:
        self.animals = animals

    def bark_all(self) -> None :
        for animal in self.animals:
            animal.bark()
