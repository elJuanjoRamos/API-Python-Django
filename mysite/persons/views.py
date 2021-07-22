from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.template import loader
from datetime import date

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

def new(request, person_id):
    person = None
    if person_id != 0:
      person = get_object_or_404(Person, pk=person_id)


    return render(request, 'persons/form.html', {'person': person})

def save(request):
    
    p = Person(name =request.POST['name'], 
    lastname=request.POST['lastname'], 
    tel=request.POST['tel'], 
    dir=request.POST['dir'],
    pub_date= date.today())

    p.save()
    return render(request, 'persons/save.html', {'person' : p})




def upd(request, person_id):
    print(person_id)
    person = None
    if person_id != 0:
      person = get_object_or_404(Person, pk=person_id)
    return render(request, 'persons/form.html', {'person': person})

def put(request, person_id):

    person = get_object_or_404(Person, pk=person_id)

    person.name = request.POST['name']
    person.lastname = request.POST['lastname']
    person.tel = request.POST['tel']
    person.dir = request.POST['dir']

    person.save()

    return render(request, 'persons/save.html', {'person' : person})


def delete(request, person_id):
    pass
