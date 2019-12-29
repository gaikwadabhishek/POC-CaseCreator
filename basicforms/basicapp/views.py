from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("RACid: "+form.cleaned_data['RACid'])
            print("Number of Requests: "+str(form.cleaned_data['no_of_req']))

    return render(request,'basicapp/form_page.html',{'form':form})
