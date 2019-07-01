from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Entry



# Create your views here.
def simple(request):

    data_model = "Checkingggggggggggggg"
    if request.method == "POST":
        form_data = request.POST
        to_db = Entry(name = form_data['name'],marks = form_data['marks'])
        to_db.save()
        
    
    return render(request,"form.html",context = {'data': data_model,})