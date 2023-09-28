import os
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apiv1.models import File
from apiv1.serializers import FileSerializer


class FileUploadViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_file_upload_success(self):
        url = reverse('file-upload')
        file_path = os.path.join(os.path.dirname(__file__), 'test_file.txt')
        file_data = {'file': open(file_path, 'rb')}
        response = self.client.post(url, file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)
        file = File.objects.first()
        self.assertEqual(response.data, FileSerializer(file).data)

    def test_file_upload_invalid_data(self):
        url = reverse('file-upload')
        file_data = {'file': 'invalid_data'}
        response = self.client.post(url, file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(File.objects.count(), 0)


class FileListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.file = File.objects.create(file='test_file.txt')

    def test_file_list(self):
        url = reverse('file-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
