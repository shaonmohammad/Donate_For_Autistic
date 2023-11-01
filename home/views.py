from django.shortcuts import render
from events.models import Event_Model
# Create your views here.


def home(request):
    finished_events = Event_Model.objects.filter(is_finished=False)
    news = Event_Model.objects.filter(is_finished=True)
    return render(request, 'home/index.html', {'events': finished_events, 'all_news': news})
