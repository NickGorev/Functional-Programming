"""
Написать в функциональном стиле функции get_names и get_object_names
реализующие (x['name'] for x in users) и (x.name for x in users).

Попробуйте сделать максимально переиспользуюемую реализацию:
1) Хотелось бы переиспользовать код, для работы со словарями и объектами
2) Что если нужно будет возвращать не names, а что-то другое?


Помогут:
1) from operator import itemgetter, attrgetter
2) from functools import partial
"""
from dataclasses import dataclass
from operator import itemgetter, attrgetter
from functools import partial
from typing import Callable, Iterator, List, TypeVar

T = TypeVar('T')
S = TypeVar('S')


def get_attr(array: List[T],
             getter: Callable[[str], Callable[[T], S]],
             attribut: str) -> Iterator[S]:
    """
    Функция принимает на вход:
    array - массив либо словарей, либо объектов
    getter - функтор, который по заданному аттрибуту генерирует
             функцию, которая принимает на вход элемент массива array,
             а возвращает значение аттрибута этого элемента
    attribut - аттрибут
    функция возвращает массив аттрибутов
    """
    return (getter(attribut)(x) for x in array)


get_names = partial(get_attr, getter=itemgetter, attribut='name')
get_obj_names = partial(get_attr, getter=attrgetter, attribut='name')


@dataclass
class User:
    name: str
    age:  int


users_objects = [User(name='Paul', age=28), User(name='Liz', age=18)]

users = [
  {'name': 'Paul', 'age': 28},
  {'name': 'Liz', 'age': 18},
]


assert list(get_names(users)) == ['Paul', 'Liz']
assert list(get_obj_names(users_objects)) == ['Paul', 'Liz']
