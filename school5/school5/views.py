from django .shortcuts import render
from django .http import HttpResponse




def index(request):
    return HttpResponse('hr hr mahadev')

def school(request):
    return HttpResponse('<b>welcome in varanasi software junction</b>')

def school1(request):
     return  render(request,'school.html')
