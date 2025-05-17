class Author:
    def __init__(self, name  ):
        self.name = name


class Book:
    all = []
    def __init__(self, title  ):
        self.title = title
        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value


class Contract:
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties