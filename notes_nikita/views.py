from django.http import HttpRequest
from django.shortcuts import render

def notes_views_nikita(request):
    context = {'notes': [{'Caption': 'my new note', 'text': 'buy milk'}, {'Caption': 'my new note', 'text': 'buy milk'}]}
    return render(request, 'notes_nikita/index.html', context=context)
# Create your views here.
