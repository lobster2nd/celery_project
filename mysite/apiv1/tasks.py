import os
import shutil

import magic

from mysite.celery import app
from .models import File


@app.task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        file_name = os.path.basename(file.file.name)
        file_type = magic.from_buffer(file.file.read(), mime=True)
        directory = file_type.replace('/', '_')
        os.makedirs("sorted_files/" + directory, exist_ok=True)
        new_file_path = os.path.join('sorted_files/', directory)
        shutil.copy(file.file.path, os.path.join(new_file_path, file_name))
        file.processed = True
        file.save()
        return {'status': 'success', 'message': 'Файл успешно обработан'}
    except File.DoesNotExist:
        return {'status': 'error', 'message': 'Файл не найден'}

