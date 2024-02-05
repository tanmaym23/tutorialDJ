from django.shortcuts import render

# Create your views here.
from . import forms

def index(request):
    return render(request,'formsapp/index.html')

def other(request):
    return render(request,'formsapp/other.html')

def contact_view(request):
    form=forms.ContactForm()

    if request.method=='POST':
        form=forms.ContactForm(request.POST)

        if form.is_valid():
            # do something code
            print("valid")

    return render(request,'formsapp/forms.html',{'form':form})
