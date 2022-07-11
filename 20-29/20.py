"""
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""
from typing import Generator

class Div7:
    def go_through(self, max_value: int) -> Generator[int,None, None]:
        for i in range(max_value+1):
            if i % 7 == 0:
                yield i

item = Div7()
sevens = item.go_through(1000)

for seven in sevens:
    print(seven)