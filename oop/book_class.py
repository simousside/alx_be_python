class Book:
    # Constructor to initialize a book instance
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor to handle book deletion
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation for the user (readable form)
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation of the object (for developers)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"