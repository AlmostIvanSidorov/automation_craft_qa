from data.data import Person, Date
from faker import Faker
import random
import os

faker_ru = Faker('ru_RU')
faker_en = Faker()
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

def generated_file(format, file_content, write_mode):
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # получаем путь к директории текущего исполняемого файла и выходим в папку на один уровень выше. Получается, что это корневая папка если структура проекта, как в видео
    file_path = os.path.join(current_dir, f'test_file_{random.randint(1, 999)}.{format}')  # добавляем к этому пути имя файла
    with open(file_path, write_mode) as file:
        file.write(file_content)
    return file_path

def generated_color(colors_number):
        color_name = ["Red","Blue","Green","Yellow","Purple","Black","White", "Voilet","Indigo", "Magenta",  "Aqua"]
        color = random.sample(color_name, k=colors_number)
        return color

def generated_date():
     yield Date(
          year = faker_en.year(),
          month = faker_en.month_name(),
          day = faker_en.day_of_month(),
          time = "12:30"
     )
