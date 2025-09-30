from dog import Dog
from dogshelter import DogShelter
from custom_exceptions import DogNotFoundException

import logging
logger =  logging.getLogger(__name__)
logging.basicConfig(filename="mylog.log", encoding="utf-8", level=logging.DEBUG)

dog_list = [
    Dog(0,"dachshund", 12, "Woof"),
    Dog(1,"retriever", 9, "Woa Woa"),
    Dog(1,"pit bull", 4, "Wrrrr, Wuff wuff"),
    Dog(3,"terier", 11, "wuf, wuw, wuw"),
    Dog(4,"dalmatin", 2, "woof, woof")
]

dog_shelter = DogShelter(dog_list)

dog_shelter.bark_all()

print(Dog.dog_count)

dog_list.append(Dog(5,"husky", 3, "wooof"))

print(Dog.dog_count)

dog_list.append(Dog(6,"labrador", 5, "wrrr, wuff"))

print(Dog.dog_count)

try:
    print(dog_shelter.get_dog_by_id(10))
except DogNotFoundException as dnf:
    print("Dog already died.")

print ("end of program")