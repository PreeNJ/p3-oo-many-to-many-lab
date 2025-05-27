class Book:
    all = []

    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception(f"title must be a string, got {type(value).__name__}")
        self._title = value

    def contracts(self):
        """Return all Contract instances for this book."""
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        """Return all Author instances who have contracts for this book."""
        return [c.author for c in self.contracts()]

    def __repr__(self):
        return f"<Book title={self.title!r}>"

class Author:
    all = []

    def __init__(self, name: str):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception(f"name must be a string, got {type(value).__name__}")
        self._name = value

    def contracts(self):
        """Return all Contract instances for this author."""
        return [c for c in Contract.all if c.author is self]

    def books(self):
        """Return all Books this author has a contract for."""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create a new Contract between this author and a book."""
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        """Sum of royalties percentages from all this author's contracts."""
        return sum(c.royalties for c in self.contracts())

    def __repr__(self):
        return f"<Author name={self.name!r}>"

class Contract:
    all = []

    def __init__(self, author, book, date: str, royalties: int):
        # use the property setters for validation
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception(f"author must be an Author instance, got {type(value).__name__}")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception(f"book must be a Book instance, got {type(value).__name__}")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception(f"date must be a string, got {type(value).__name__}")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception(f"royalties must be an int, got {type(value).__name__}")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts signed on the given date."""
        return [c for c in cls.all if c.date == date]

    def __repr__(self):
        return (f"<Contract author={self.author.name!r} book={self.book.title!r} "
                f"date={self.date!r} royalties={self.royalties}%>")
