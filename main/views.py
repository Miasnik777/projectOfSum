from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Articles
from .forms import UploadFileForm
from .validators import validate_file_extension


#from somewhere import handle_uploaded_file


def about(request): # функция просто для перехода)
    return render(request,"main/about.html")

def handle_uploaded_file(f): #функция для загрузки видео
    with open(f"uploads/{f.name}", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def show_video (request): #функция для загрузки видео
    video = Articles.objects.order_by('-date')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            fp = Articles(file=form.cleaned_data['file'])
            fp.save()
            #handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()
    return render(request, "main/index.html",
                 {'video': video, 'form': form})





def save(self, *args, **kwargs):
    try:
        self.full_clean()
        super(UploadFiles, self).save(*args, **kwargs)
    except ValidationError as e:
        pass

#def recent (request):
#    with open(f"uploads/{f.name}", 'wb+') as destination:
 #       file = Articles.objects.order_by('-date')
 #       return render(request, "main/index.html", {'video': file})

