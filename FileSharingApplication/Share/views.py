from django.shortcuts import render
from .models import Fileinfo
# Create your views here.
def Share(request):
    if request.method == "POST":
        title = request.POST['Title']
        file = request.FILES['myfile']
        description = request.POST['Description']
        Fileinfo.objects.create(filepath = file,title=title,description=description)
        return render(request,'share/index.html')
    else:
        return render(request,'share/index.html')

        