from app.forms import ClassesForm
from django.shortcuts import redirect, render


def classes(request):
    if request.method == "POST":
        form = ClassesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    elif request.method == "GET":
        form = ClassesForm()
        return render(request, 'index.html', {'form': form})
