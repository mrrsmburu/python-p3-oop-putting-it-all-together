#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "Used"

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    @property
    def condition(self):
        return self._condition

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"

    pass