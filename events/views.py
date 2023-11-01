from django.shortcuts import render, redirect
from django.views.generic import ListView
from . models import Event_Model
from .models import Event_Model
from blog.models import BlogModel
from django.db.models import Q

# Create your views here.


class Manage_Event(ListView):
    model = Event_Model
    template_name = 'events.html'
    template_name = 'home.html'


def search(request):

    if 'keyword' in request.GET:

        keyword = request.GET['keyword']

        if keyword:

            results_events = Event_Model.objects.filter(
                Q(title__icontains=keyword) | Q(body__icontains=keyword))

            # results_blogs = BlogModel.objects.filter(Q(title__icontains=keyword) | Q(body__icontains=keyword))

        if not keyword:

            return redirect('home')

    context = {

        'results': results_events,

        # 'results_blogs':results_blogs

    }

    return render(request, 'search.html', context)
