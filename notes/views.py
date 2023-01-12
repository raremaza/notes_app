from django.http import HttpResponse
from django.shortcuts import render
from .models import Notes

from django.db.models import F
from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum, Max

# Create your views here.
def index(request):
    notes = Notes.objects.all()
    # context = {
    #     'notes': [
    #         {'title': 'Grocery list', 'text': "Don't forget to pick up bread, eggs, and bananas at the store."},
    #         {'title': 'Meeting with client', 'text': 'Meet with the client at 2pm in the conference room to discuss the project proposal.'},
    #         {'title': 'Pay rent', 'text': 'Remember to pay the rent by the 5th of the month.'},
    #         {'title': 'Dentist appointment', 'text': 'You have a dentist appointment at 10am on Friday.'},
    #         {'title': 'Book flight to visit grandma', 'text': 'Book a flight to visit grandma in Florida for Christmas.'},
    #         {'title': 'Car maintenance', 'text': 'Take the car in for an oil change and tire rotation.'},
    #         {'title': 'Register for marathon', 'text': 'Register for the marathon on the website before registration closes.'},
    #         {'title': 'RSVP for wedding', 'text': 'RSVP to the wedding invitation by next Wednesday.'},
    #         {'title': 'Buy birthday present for mom', 'text': 'Pick up a birthday present for mom at the mall on Saturday.'},
    #         {'title': 'Study for history exam', 'text': 'Spend at least two hours studying for the history exam on Monday.'}
    #     ]
    # }

    #Task_1
    # notes_count = Notes.objects.count()
    # print(notes_count)

    #Task_2
    #notes = Notes.objects.filter(text__contains="Product")
    #notes = Notes.objects.filter(text__icontains=F("caption"))
    #notes = Notes.objects.filter(caption__exact = "My_note")
    #notes = Notes.objects.all()[:2]

    #Task_3
    # notes_count = Notes.objects.count()
    # print(notes_count)
    # notes_max = Notes.objects.aggregate(notes_maximum = Max('reminder'))
    # print(notes_max)
    # notes_avg = Notes.objects.aggregate(notes_avg=Avg('id'))
    # print(notes_avg)
    # notes_sum = Notes.objects.aggregate(notes_sum=Sum('category_id'))
    # print(notes_sum)



    context = {"notes": notes}
    return render(request, "index.html", context=context)