from django.shortcuts import render
import csv, io
from django.contrib import messages
from .models import Mdata
# Create your views here.

def csv_upload(request):
    template = "csv_upload.html"
    data = Mdata.objects.all()
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Mdata.objects.update_or_create(
            id=column[0],
            name=column[1],
            date=column[3],
            location=column[4]
        )
    context = {}
    return render(request, template, context)