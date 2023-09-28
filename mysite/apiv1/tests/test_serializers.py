from django.test import TestCase
from django.utils.timezone import utc
from apiv1.models import File
from apiv1.serializers import FileSerializer


class FileSerializerTest(TestCase):
    def setUp(self):
        self.file = File.objects.create(file='test_file.txt')
        self.serializer = FileSerializer(instance=self.file)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'file', 'uploaded_at', 'processed'})

    def test_serializer_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.file.id)
        self.assertEqual(data['file'], self.file.file.url)
        self.assertEqual(data['processed'], self.file.processed)

