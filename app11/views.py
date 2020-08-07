from django.shortcuts import render
from app11.form import StudentForm

# Create your views here.
def index(request):
    form = StudentForm(request.POST)
    return render(request, 'main.html',{'form':form}) 

   