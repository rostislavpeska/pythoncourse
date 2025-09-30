from dog import Dog
from dogshelter import DogShelter

my_dog = Dog("jezevcik", 12, "Woof")
my_dog2 = Dog("retriever", 9, "Woa Woa")

animal = [
    my_dog,
    my_dog2
]

animal_list = DogShelter(animal)

animal_list.bark_all()

"""

my_dog.bark()
my_dog2.bark()
my_cat.meow()"""