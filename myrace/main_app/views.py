
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Race, Completed
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import TrainingForm



# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1><a href="/races">index</a>')

def about(request):
    return render(request, 'about.html')

def races_index(request):
    races = Race.objects.all()
    return render(request, 'races/index.html', {'races': races})


def races_detail(request, race_id):
    race = Race.objects.get(id=race_id)
    training_form = TrainingForm()
    # completed_race_false = Completed.objects.exclude(id__in = race.completed.all().values_list('id'))
    return render(request, 'races/detail.html', {'race': race, 'training_form': training_form})

## functions
def assoc_completed(request, race_id, completed_id):
    Race.objects.get(id=race_id).completed.add(completed_id)
    return redirect ('detail', race_id=race_id)

def add_training(request, race_id):
    form = TrainingForm(request.POST)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.race_id = race_id
        new_training.save()
    return redirect('detail', race_id=race_id)



class RaceCreate(CreateView):
    model = Race
    fields = ['race_name', 'race_type', 'year', 'distance', 'image']
    success_url= '/races/'
    
class RaceUpdate (UpdateView):
    model = Race
    fields = ['race_name', 'race_type', 'year', 'distance', 'image']
    
class RaceDelete(DeleteView):
    model = Race
    success_url="/races/"
    
class CompletedList(ListView):
    model = Completed
    
class CompletedDetail(DetailView):
    model = Completed
    
class CompletedCreate(CreateView):
    model = Completed
    fields = '__all__'
    
class CompletedUpdate(UpdateView):
    model = Completed
    fields = ['completed_race']
    
class CompletedDelete(DeleteView):
    model: Completed
    success_url = '/completed/'
    
    

