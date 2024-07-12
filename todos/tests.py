from django.test import TestCase
from .models import Todo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='Test title',
            body='test body',
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'Test title')
        self.assertEqual(self.todo.body, 'test body')
        self.assertEqual(str(self.todo), 'Test title')

    def test_api_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(reverse('detail_view', kwargs={"pk": self.todo.pk}),
        format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
