from django.db import models

# Create your models here.
from django.db import models
from .validators import validate_file_extension
from django.core.exceptions import ValidationError


# Create your models here.
class Articles(models.Model):  # форма которую надо изменить для видео
    objects = models.Manager()
    title = models.CharField('Название', max_length=25)
    file = models.FileField(upload_to='uploads_model', validators=[validate_file_extension])
    date = models.DateTimeField('Дата загрузки',auto_now_add=True)

    def __str__(self):
        return f'Запись:{self.title}'

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

# class UploadFiles(models.Model):
# file = models.FileField(upload_to='uploads%Y/%m/%d/', validators=[validate_file_extension])
# подсоединяется к админу
