import persons
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.template import loader

from .models import Person

def index(request):
    latest_persons_list = Person.objects.order_by('id')

    template = loader.get_template('persons/index.html')

    context = {
        'latest_persons_list': latest_persons_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'persons/detail.html', {'person': person})

def new(request):
    person = None
    return render(request, 'persons/form.html', {'person': person})
