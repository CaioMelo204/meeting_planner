from django.shortcuts import render, HttpResponse
from datetime import datetime
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html', 
                  {"num_meetings": Meeting.objects.count()})
