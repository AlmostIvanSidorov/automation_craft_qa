from data.data import Person
from faker import Faker
import random

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name = f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}" ,
        firstname= faker_ru.first_name(),
        lastname= faker_ru.last_name(),
        age= random.randint(18,70),
        salary= random.randint(100,1000),
        department= faker_ru.job(),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address(),
    )