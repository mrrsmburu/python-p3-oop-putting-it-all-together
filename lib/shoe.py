#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            print("Error: size must be an integer.")
        else:
            self.size = size
            self.condition = 'New'    
   
    pass