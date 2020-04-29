from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        content = {
            'name': request.POST['name'],
            'loc': request.POST['location'],
            'lang': request.POST['language'],
            'sex': request.POST['gender'],
            'com': request.POST['comment'],
        }
        return redirect('/result')
    return render(request, 'result.html')