from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата и время загрузки')
    processed = models.BooleanField(default=False, verbose_name='Обработан')
