from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file = file_serializer.save()
            process_file.delay(file.id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    http_method_names = ['get']
    serializer_class = FileSerializer
