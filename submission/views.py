from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'loc': request.POST['location'],
            'lang': request.POST['language'],
            'com': request.POST['comment'],
        }
        return render(request,'result.html', context)
    return render(request, 'result.html')