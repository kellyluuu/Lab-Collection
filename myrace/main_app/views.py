from django.shortcuts import render
from django.http import HttpResponse

## demo Myrace data base
class Race:
  def __init__(self, name, year, distance, type, time, link):
    self.name = name
    self.year = year
    self.distance = distance
    self.type = type
    self.time = time
    self.link = link


races = [
    Race('Rockets Run', '2010', 3.1, 'Run-5K', '0:37:39', 'https://www.athlinks.com/event/29651/results/Event/110466/Course/151573/Bib/661'),
    Race('Bridgeland Triathlon', '2012', 16.4, 'Sprint Tri-550M Swim, 13Mi Bike, 3.1Mi Run', '1:46:06', 'https://www.athlinks.com/event/32579/results/Event/222349/Course/476105/Bib/1368'),
    Race('Houston Half Marathon', '2012', 13.1, 'Run-Half Marathon', '2:19:02', 'https://www.athlinks.com/event/4971/results/Event/209133/Course/288833/Bib/1680'),
    Race('Sugar Land Finish Line Sports 30K', '2012', 18.6, 'Run-30K', '3:46:31', 'https://www.athlinks.com/event/22448/results/Event/242292/Course/339410/Bib/414'),
    Race('Chevron Houston Marathon', '2013', 26.2, 'Run-Marathon', '5:56:01', 'https://www.athlinks.com/event/4476/results/Event/209186/Course/299862/Bib/13327'),
    Race('Conocophillips Rodeo Run', '2013', 6.2, '10K Run', '0:58:02', 'https://www.athlinks.com/event/34876/results/Event/217526/Course/347852/Bib/7545'),
    Race('Memorial Hermann IRONMAN 70.3 Texas', '2013', 13.1, 'Half Ironman Triathlon-1.2-mile Swim, 56-mile Bike, 13.1-mile Run', '7:48:34', 'https://www.athlinks.com/event/32699/results/Event/262676/Course/390705/Entry/142033731'),
    Race('Bridgeland Triathlon', '2013', 16.1, 'Sprint Triathlon-550M Swim, 12.5Mi Bike, 3.1Mi Run', '1:46:06', 'https://www.athlinks.com/event/32579/results/Event/285687/Course/407451/Bib/1368'),
    Race('Oilman Triathlon', '2013', 70.3, 'Half Iron Distance-1.2 mile Swim, 56 mile Bike, 13.1 mile Run', '8:10:49', 'https://www.athlinks.com/event/190334/results/Event/247025/Course/463149/Bib/637'),
    Race('Sugar Land Finish Line Sports 30k', '2013', 18.6, '30k Run', '3:15:32', 'https://www.athlinks.com/event/22448/results/Event/283393/Course/485264/Bib/975'),
    Race('Chevron Houston Marathon', '2014', 3.1, '5k Run', '0:30:29', 'https://www.athlinks.com/event/4476/results/Event/318560/Course/519740/Bib/54697'),
    Race('Chevron Houston Marathon', '2014', 26.2, 'Marathon', '4:43:55', 'https://www.athlinks.com/event/4476/results/Event/318560/Course/402871/Bib/9467'),   
    Race('No Label Triathlon', '2014', 17.3, 'Triathlon-Swim 300 Meter Swim, Bike 14 Miles, Run 3.1 Miles', '1:21:51', 'https://www.athlinks.com/event/32660/results/Event/340803/Course/565436/Bib/105'),
    Race('Memorial Hermann IRONMAN 70.3 Texas', '2014', 70.3, 'Half Ironman Triathlon-1.2mile Swim, 56mile Bike, 13.1mile Run', '6:55:13', 'https://www.athlinks.com/event/32699/results/Event/343589/Course/510436/Entry/178102437'),
    Race('Ironman Texas', '2014', 140.6, 'Ironman Tri-2.4Mi Swim, 112Mi Bike, 26.2Mi Run', '15:25:30', 'https://www.athlinks.com/event/140911/results/Event/317072/Course/455817/Entry/182136754'),
    Race('Houston Half Marathon & 10K', '2014', 13.1, 'Half Marathon', '2:15:10', 'https://www.athlinks.com/event/4971/results/Event/401076/Course/543221/Bib/4895'),
    Race('Chevron Houston Marathon', '2015', 26.2, 'Marathon', '5:07:23', 'https://www.athlinks.com/event/4476/results/Event/370364/Course/605030/Bib/8632'),
    Race('Chevron Houston Marathon', '2016', 26.2, 'Marathon', '5:03:36', 'https://www.athlinks.com/event/4476/results/Event/512122/Course/760268/Bib/13605'),
    Race('Chevron Houston Marathon', '2017', 26.2, 'Marathon', '5:19:46', 'https://www.athlinks.com/event/4476/results/Event/646492/Course/930905/Bib/14238'),
    Race('Chevron Houston Marathon', '2018', 26.2, 'Marathon', '5:10:28', 'https://www.athlinks.com/event/4476/results/Event/612408/Course/1156721/Bib/13307'),
    Race('USA Fit Marathon', '2018', 13.1, 'Half Marathon', '2:55:49', 'https://www.athlinks.com/event/6623/results/Event/708936/Course/1157959/Bib/2584'),
]    


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def races_index(request):
    return render(request, 'races/index.html', {'races': races})