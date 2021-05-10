from app.models import Classes
from app.forms import ClassesForm
from django.shortcuts import redirect, render


def classes(request):
    if request.method == "POST":
        form = ClassesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/classes/new')
            except Exception as e:
                pass
    elif request.method == "GET":
        form = ClassesForm()
        return render(request, 'index.html', {'form': form})


def display_classes(request):
    if request.method == "GET":
        classes = Classes.objects.all()
        return render(request, 'display.html', {'classes': classes})
