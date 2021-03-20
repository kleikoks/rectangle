from rest_framework.test import APITestCase
from django.urls import reverse
from project.models import Book
from project.serializers import BookSerializer
from rest_framework import status

class TestBookCase(APITestCase):
    def test_list_get(self):
        queryset = [
            Book.objects.create(name='test book1', price=24.24),
            Book.objects.create(name='test book2', price=25.25)
        ]
        url = reverse('book_list')
        response = self.client.get(url)
        data = BookSerializer(queryset, many=True).data
        self.assertEqual(data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
