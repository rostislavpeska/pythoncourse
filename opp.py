from dog import Dog
from dogshelter import DogShelter


dog_list = [
    Dog("jezevcik", 12, "Woof"),
    Dog("retriever", 9, "Woa Woa")
]

dog_shelter = DogShelter(dog_list)

dog_shelter.bark_all()

"""

my_dog.bark()
my_dog2.bark()
my_cat.meow()"""