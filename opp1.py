from dog import Dog
from dogshelter import DogShelter

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

dog_shelter.bark_all()

print ("end of program")