# ===================================================================================================================
# Реализуйте класс «Книга».
# Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ===================================================================================================================.


class Book:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.year = kwargs.get('year', None)
        self.publisher = kwargs.get('publisher', None)
        self.genre = kwargs.get('genre', None)
        self.author = kwargs.get('author', None)
        self.price = kwargs.get('price', 0.0)
    
    def set_title(self, title):
        self.title = title
    def set_year(self, year):
        self.year = year
    def set_publisher(self, publisher):
        self.publisher = publisher
    def set_genre(self, genre):
        self.genre = genre
    def set_author(self, author):
        self.author = author
    def set_price(self, price):
        self.price = price
    
    def get_title(self):
        return self.title
    def get_year(self):
        return self.year
    def get_publisher(self):
        return self.publisher
    def get_genre(self):
        return self.genre
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price
    
    def __str__(self) -> str:
        result = ''
        for key, value in self.__dict__.items():
            result += f'{key}: {value}\n'
        return result

the_lord_of_the_rings_1 = Book(
    title = 'The Lord of the Rings: The Fellowship of the Ring',
    year = '29 July 1954',
    publisher = 'Allen & Unwin',
    genre = 'High Fantasy Adventure',
    author = 'J. R. R. Tolkien',
    price = '30.37 USD',
)

print(the_lord_of_the_rings_1)