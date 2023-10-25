from django.test import TestCase
from .models import Category, Book, Student

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="Test Category")

    def test_category_creation(self):
        self.assertEqual(self.category.category_name, "Test Category")

class BookTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="Test Category")
        self.book = Book.objects.create(category=self.category, book_title="Test Book")

    def test_book_creation(self):
        self.assertEqual(self.book.book_title, "Test Book")
        self.assertEqual(self.book.category.category_name, "Test Category")

class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="John Doe", age=20, father_name="John Doe Sr.")

    def test_student_creation(self):
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.father_name, "John Doe Sr.")
