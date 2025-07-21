from collections import deque
import math


class Pagination():

    def __init__(self, text: str, num: int):
        self.text = text
        self.num = num
        self.count_of_symbols = 0
        self.items_on_page: list = []

        if num < 0 or text is None:
            raise ValueError("Invalid input: num < 0 or text is None")

    def page_count(self):
        pages = math.ceil(self.count_of_symbols/self.num)
        return pages

    def item_count(self):
        self.count_of_symbols = len(self.text)
        return self.count_of_symbols

    def count_items_on_page(self, number_of_page):
        self.items_on_page = []
        box = ""

        for i in self.text:
            box += i
            if len(box) == self.num:
                self.items_on_page.append(box)
                box = ""
        if box:
            self.items_on_page.append(box)
            box = ""

        if number_of_page < 0 or number_of_page >= len(self.items_on_page):
            raise Exception("Invalid index. Page is missing")

        return len(self.items_on_page[number_of_page])

    def find_page(self, find_text):
        result = []
        for i, k in enumerate(self.items_on_page):
            if find_text in k:
                result.append(i)
        return result

    def display_page(self):
        pass


page = Pagination("Your beautiful text", 5)
print(page.item_count())  # 19
print(page.page_count())  # 4
print(page.count_items_on_page(0))  # 5
print(page.count_items_on_page(3))  # 4
# print(page.count_items_on_page(4)) #Invalid index. Page is missing.
print(page.find_page('Your'))  # [0]
print(page.find_page('e'))  # [1, 3]
print(page.find_page('beautiful'))  # [1, 2]
# print(page.find_page('great')) #Exception: 'great' is missing on the pages
