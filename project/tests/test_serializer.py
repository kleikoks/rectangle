from django.test import TestCase
from project.models import Book
from project.serializers import BookSerializer

class BookSerializerTestCase(TestCase):
    def test_serializer(self):
        queryset = [
            Book.objects.create(name='test book1', price=24.24),
            Book.objects.create(name='test book2', price=25.25)
        ]
        data = BookSerializer(queryset, many=True).data
        expected_data = [
            {
                'id': queryset[0].id,
                'name': 'test book1',
                'price': '24.24'
            },
            {
                'id': queryset[1].id,
                'name': 'test book2',
                'price': '25.25'
            }
        ]
        self.assertEqual(data, expected_data)