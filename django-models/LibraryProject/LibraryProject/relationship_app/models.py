from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    # One Author → Many Books
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=255)
    # Many Libraries can contain many Books
    books = models.ManyToManyField(
        Book,
        related_name='libraries',
        blank=True
    )

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    # One Library ↔ One Librarian
    library = models.OneToOneField(
        Library,
        related_name='librarian',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} ({self.library.name})"