from django.shortcuts import render
from django.http import HttpResponse
from api.models import Question
from django.conf import settings
import os
import csv
from api.models import Hospital


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def importHospitals(request):
    csvFile = open(os.path.join(settings.BASE_DIR, 'api', 'csvFiles', 'hospitals.csv'))
    reader = csv.DictReader(csvFile)
    for row in reader:
        if not isInt(row['beds']):
            #if number of beds not provided
            p = Hospital(name=row['name'], latitude=row['lat'], longitude=row['long'], nbBeds=0)
        else:
            p = Hospital(name=row['name'], latitude=row['lat'], longitude=row['long'], nbBeds=int(row['beds']))
        p.save()
    return HttpResponse("<h1>Imported succesfully</h1>")

def isInt(value):
    try:
        int(value)
        return True
    except:
        return False
