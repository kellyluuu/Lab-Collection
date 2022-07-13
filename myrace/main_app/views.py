
from django.shortcuts import render
from django.http import HttpResponse
from .models import Race
from django.views.generic.edit import CreateView, UpdateView, DeleteView

## demo Myrace data base



# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def races_index(request):
    races = Race.objects.all()
    return render(request, 'races/index.html', {'races': races})

def races_detail(request, race_id):
    race = Race.objects.get(id=race_id)
    return render(request, 'races/detail.html', {'race': race})

class RaceCreate(CreateView):
    model = Race
    fields = '__all__'
    success_url= '/races/'
    
class RaceUpdate (UpdateView):
    model = Race
    fields = ['race_name', 'race_type', 'year', 'distance', 'image']
    
class RaceDelete(DeleteView):
    model = Race
    success_url="/races/"
    

