#!/usr/bin/env python3

class Book:
     def __init__(self, title, page_count):
        self.title = title
        if not isinstance(page_count, int):
            print("Error: page_count must be an integer.")
        else:
            self.page_count = page_count

     def turn_page(self):
        if self.current_page < self.page_count:
            print("Flipping the page...wow, you read fast!")
            self.current_page += 1
        else:
            print("You've reached the end of the book!")
    
        