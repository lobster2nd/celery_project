from mysite.celery import app

from .models import File

@app.task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        # Здесь вы можете выполнить обработку файла
        file.processed = True
        file.save()
        return {'status': 'success', 'message': 'Файл успешно обработан'}
    except File.DoesNotExist:
        return {'status': 'error', 'message': 'Файл не найден'}

