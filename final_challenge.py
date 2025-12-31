# Final Challenge: The "Library Management System"
class Item:
    def __init__(self, title, id_number):
        self.title = title
        self.id_number = id_number
    def get_info(self):
        return f'ID: {self.id_number} - Title: {self.title}'

class Book(Item):
    def __init__(self, title, id_number, author):
        super().__init__(title, id_number)
        self.author = author
    def get_info(self):
        return f'ID: {self.id_number} - Book: {self.title} by {self.author}'

library = [
    Item("Library Map", 101),
    Book("The Great Gatsby", 202, "F. Scott Fitzgerald"),
    Book("1984", 303, "George Orwell")
]

for i in library:
    print(i.get_info())