from django.test import TestCase
from apiv1.models import File


class FileModelTest(TestCase):
    def setUp(self):
        self.file = File.objects.create(file='test_file.txt')

    def test_file_creation(self):
        self.assertEqual(self.file.file, 'test_file.txt')
        self.assertFalse(self.file.processed)

    def test_file_processed(self):
        self.file.processed = True
        self.file.save()
        self.assertTrue(self.file.processed)
