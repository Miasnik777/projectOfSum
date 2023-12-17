from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    valid_extensions = ['.avi', '.asf', '.flv', '.mkv', '.mp4', '.mp3', '.wav', '.ogg', '.wma']
    ext = os.path.splitext(value.name)[1]
    #value.name.split('.')[-1]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Файл неподходящего формата.')
    return 'Файл успешно загружен'
