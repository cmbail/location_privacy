from dataclasses import dataclass

@dataclass
class Item:
    title: str
    id_number: int

    def get_info(self):
        return f"ID: {self.id_number} - Title: {self.title}"

@dataclass
class Book(Item):
    author: str

    def get_info(self):
        return f"ID: {self.id_number} - Book: {self.title} by {self.author}"


library = [
    Item("Library Map", 101),
    Book("The Great Gatsby", 202, "F. Scott Fitzgerald"),
    Book("1984", 303, "George Orwell"),
]

for item in library:
    print(item.get_info())
