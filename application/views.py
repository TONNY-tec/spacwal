from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def vision(request):
    return render(request, 'vision.html')

def mission(request):
    return render(request, 'mission.html')

def core_values(request):
    return render(request, 'values.html')

def services_list(request):
    return render(request, 'services_list.html')