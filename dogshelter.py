from dog import Dog
from custom_exceptions import DogNotFoundException
import logging
logger =  logging.getLogger(__name__)

class DogShelter:
    def __init__(self, animals: list[Dog]) -> None:
        self.animals = animals

    def bark_all(self) -> None :
        for animal in self.animals:
            animal.do_command("make_sound")

    def get_dog_by_id(self, dog_id: int) -> Dog | None:
        logger.info(f"getting dog by id: {dog_id}")
        for d in self.animals:
            if d.get_chip_num() == dog_id:
                return d

        raise DogNotFoundException(f"Dog {dog_id} not found")


"""
    def remove_dog_by_id(self, dog_id: int) -> None:
        self.dog = [d for d in self.animals if d.id != dog_id]
"""