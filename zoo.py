from animal import Animal
from custom_exceptions import DogNotFoundException
import logging
logger =  logging.getLogger(__name__)

class Zoo:
    def __init__(self, animals: list[Animal]) -> None:
        self.animals = animals

    def make_sound_all(self) -> None:
        for animal in self.animals:
            animal.do_command("make_sound")