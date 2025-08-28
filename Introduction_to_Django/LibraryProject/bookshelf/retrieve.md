# Retrieve Operation

```python
Book.objects.all()
# Expected output: <QuerySet [<Book: 1984 by George Orwell>]>

Book.objects.get(id=book.id)
# Expected output: <Book: 1984 by George Orwell>