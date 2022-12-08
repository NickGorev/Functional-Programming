"""
задание:
Нужно реализовать класс Seq , который будет принимать в метод __init__ любую
последовательность Sequence[T] , где T - некоторый тип (generic).
Для класса Seq нужно будет реализовать методы map, filter и take.

Метод map будет принимать функцию, которая будет трансформировать тип Т
(тот который внутри последовательности, которую передали в инит) в любой тип.

Метод filter будет принимать функцию, которая входным параметром принимает
тип T и возвращает bool.

Метод take принимает число и возвращает список из того количества элементов,
которое передали в take.

Методы должны быть ленивые - map и filter применяются только к тому количеству
элементов, которое необходимо для того, чтобы вернуть запрошенное в take.
"""
from __future__ import annotations
from collections.abc import Sequence, Iterable
from typing import TypeVar, Generic, Callable

T = TypeVar('T')
S = TypeVar('S')


class Seq(Generic[T]):
    def __init__(self, seq: Iterable[T]):
        """
        метод __init__
        принимает любую последовательность Sequence[T]
        """
        self.seq = seq

    def map(self, func: Callable[[T], S]) -> Seq[S]:
        """
        Метод map
        принимает функцию, которая трансформирует тип Т
        (тот который внутри последовательности, которую передали в инит)
        в любой тип S.
        """
        return Seq(map(func, self.seq))

    def filter(self, func: Callable[[T], bool]) -> Seq[T]:
        """
        Метод filter
        принимает функцию, которая входным параметром принимает
        тип T и возвращает bool.
        """
        return Seq(filter(func, self.seq))

    def take(self, number: int) -> Sequence[T]:
        """
        Метод take
        принимает число и возвращает список из того количества элементов,
        которое передали в take.
        """
        ans = []
        iter_obj = iter(self.seq)
        for _ in range(number):
            try:
                ans.append(next(iter_obj))
            except StopIteration:
                break
        return ans


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(3)
    assert res == [12, 14]
