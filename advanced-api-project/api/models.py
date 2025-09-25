from django.db import models

class Author(models.Model):
    """
    Author model represents a book writer.
    One author can have many books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents an individual book.
    Each book is linked to exactly one author (ForeignKey).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        related_name="books",  # used for reverse lookup in serializers
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"