from django.shortcuts import render, HttpResponse
from tution.models import Contact
def home(request):
    
    name=['abk','maigga rakib','senti rahad','votka sifat','porn mushi']
        
    context={
        'name': name
    }
    return render(request,'home.html',context)

      