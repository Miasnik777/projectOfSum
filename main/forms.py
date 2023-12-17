from django import forms
from .validators import validate_file_extension
from django.core.exceptions import ValidationError
from .models import *


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['file']
    # title = forms.CharField(max_length=50)
    # file = forms.FileField(label="Файл", validators=[validate_file_extension])
# та самая форма на гл. странице с загрузкой файла и его отправкой
