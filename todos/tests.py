from django.test import TestCase
from .models import Todo
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
