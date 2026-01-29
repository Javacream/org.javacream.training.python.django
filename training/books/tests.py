from django.test import TestCase
from decimal import Decimal
from .models import Publisher, Author, Book


class PublisherCrudTests(TestCase):
    def test_create_read_update_delete_publisher(self):
        # CREATE
        p = Publisher.objects.create(name="O'Reilly Media")
        self.assertIsNotNone(p.pk)

        # READ
        fetched = Publisher.objects.get(pk=p.pk)
        self.assertEqual(fetched.name, "O'Reilly Media")

        # UPDATE
        fetched.name = "O'Reilly"
        fetched.save()
        updated = Publisher.objects.get(pk=p.pk)
        self.assertEqual(updated.name, "O'Reilly")

        # DELETE
        updated.delete()
        self.assertFalse(Publisher.objects.filter(pk=p.pk).exists())


class AuthorCrudTests(TestCase):
    def test_create_read_update_delete_author(self):
        # CREATE
        a = Author.objects.create(firstname="Ada", lastname="Lovelace")
        self.assertIsNotNone(a.pk)

        # READ
        fetched = Author.objects.get(pk=a.pk)
        self.assertEqual(fetched.firstname, "Ada")
        self.assertEqual(fetched.lastname, "Lovelace")

        # UPDATE
        fetched.firstname = "Augusta Ada"
        fetched.save()
        updated = Author.objects.get(pk=a.pk)
        self.assertEqual(updated.firstname, "Augusta Ada")

        # DELETE
        updated.delete()
        self.assertFalse(Author.objects.filter(pk=a.pk).exists())


class BookCrudTests(TestCase):
    def setUp(self) -> None:
        self.publisher = Publisher.objects.create(name="Penguin")
        self.author1 = Author.objects.create(firstname="Grace", lastname="Hopper")
        self.author2 = Author.objects.create(firstname="Linus", lastname="Torvalds")

        self.book = Book.objects.create(
            isbn="9780134757599",
            title="Refactoring",
            pages=448,
            price=Decimal("49.99"),
            publisher=self.publisher,
        )
        self.book.authors.add(self.author1)

    def test_create_book_and_assign_authors(self):
        # CREATE another book
        b = Book.objects.create(
            isbn="9781491950357",
            title="Designing Data-Intensive Applications",
            pages=616,
            price=Decimal("59.00"),
            publisher=self.publisher,
        )
        b.authors.add(self.author1, self.author2)

        # Assert create + m2m
        self.assertTrue(Book.objects.filter(isbn="9781491950357").exists())
        self.assertEqual(b.authors.count(), 2)
        self.assertIn(self.author2, b.authors.all())

    def test_read_book_and_relations(self):
        # READ book by PK (isbn)
        fetched = Book.objects.get(pk=self.book.isbn)
        self.assertEqual(fetched.title, "Refactoring")
        self.assertEqual(fetched.publisher.name, "Penguin")

        # READ relations
        authors = list(fetched.authors.all())
        self.assertEqual(len(authors), 1)
        self.assertEqual(authors[0].lastname, "Hopper")

        # reverse relation: publisher -> books
        self.assertIn(fetched, self.publisher.books.all())

        # reverse relation: author -> books
        self.assertIn(fetched, self.author1.books.all())

    def test_update_book_fields_and_relations(self):
        # UPDATE fields
        self.book.title = "Refactoring (2nd Edition)"
        self.book.pages = 460
        self.book.price = Decimal("54.50")
        self.book.save()

        updated = Book.objects.get(pk=self.book.isbn)
        self.assertEqual(updated.title, "Refactoring (2nd Edition)")
        self.assertEqual(updated.pages, 460)
        self.assertEqual(updated.price, Decimal("54.50"))

        # UPDATE many-to-many: add and remove authors
        updated.authors.add(self.author2)
        self.assertEqual(updated.authors.count(), 2)

        updated.authors.remove(self.author1)
        self.assertEqual(updated.authors.count(), 1)
        self.assertIn(self.author2, updated.authors.all())
        self.assertNotIn(self.author1, updated.authors.all())

    def test_delete_book(self):
        isbn = self.book.isbn

        # DELETE book
        self.book.delete()

        # Assert deletion
        self.assertFalse(Book.objects.filter(pk=isbn).exists())

        # M2M join rows should be gone automatically
        self.assertEqual(self.author1.books.filter(pk=isbn).count(), 0)

    def test_publisher_protect_on_delete(self):
        # on_delete=PROTECT should prevent deleting a publisher that still has books
        with self.assertRaises(Exception):
            self.publisher.delete()
