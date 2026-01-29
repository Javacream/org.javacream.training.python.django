from django.test import TestCase
from .models import Person, Address


class PersonCrudTest(TestCase):
    def setUp(self) -> None:
        # Arrange: create one initial object for read/update/delete tests
        self.person = Person.objects.create(
            firstname="Hugo",
            lastname="Meier",
            height=165,
            weight=55.0,
        )

    def test_create_person(self):
        # Act
        p = Person.objects.create(
            firstname="Hannah",
            lastname="Müller",
            height=170,
            weight=62.5,
        )

        # Assert
        self.assertIsNotNone(p.pk)
        self.assertEqual(Person.objects.count(), 2)

    def test_read_person(self):
        # Act
        p = Person.objects.get(pk=self.person.pk)

        # Assert
        self.assertEqual(p.firstname, "Hugo")
        self.assertEqual(p.lastname, "Meier")
        self.assertEqual(p.height, 165)
        self.assertEqual(p.weight, 55.0)

    def test_update_person(self):
        # Act
        self.person.height = 166
        self.person.weight = 56.2
        self.person.save()

        updated = Person.objects.get(pk=self.person.pk)

        # Assert
        self.assertEqual(updated.height, 166)
        self.assertEqual(updated.weight, 56.2)

    def test_delete_person(self):
        # Act
        pk = self.person.pk
        self.person.delete()

        # Assert
        self.assertEqual(Person.objects.filter(pk=pk).count(), 0)
        self.assertEqual(Person.objects.count(), 0)

class AddressModelCRUDTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            street="Main Street 1",
            city="Berlin"
        )

    def test_create_address(self):
        address = Address.objects.create(
            street="High Street 5",
            city="Munich"
        )
        self.assertEqual(Address.objects.count(), 2)
        self.assertEqual(address.city, "Munich")

    def test_read_address(self):
        address = Address.objects.get(id=self.address.id)
        self.assertEqual(address.street, "Main Street 1")
        self.assertEqual(address.city, "Berlin")

    def test_update_address(self):
        self.address.street = "Updated Street 99"
        self.address.city = "Hamburg"
        self.address.save()

        updated = Address.objects.get(id=self.address.id)
        self.assertEqual(updated.street, "Updated Street 99")
        self.assertEqual(updated.city, "Hamburg")

    def test_delete_address(self):
        self.address.delete()
        self.assertEqual(Address.objects.count(), 0)
