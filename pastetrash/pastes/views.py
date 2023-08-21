from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .models import Paste

@csrf_protect
def index(request):
    error = None
    if request.method == "POST":
        try:
            paste = Paste.objects.create(
                title=request.POST.get("title"),
                content=request.POST.get("paste"),
                password=request.POST.get("password"),
                syntax="raw",
                )
        except Exception as e:
            error = e

    pastes = Paste.objects.all()
    return render(request, "index.html", {"pastes": pastes, "error": error})

@csrf_protect
def paste(request, slug):
    paste = get_object_or_404(Paste, slug=slug)    
    if paste.password:
        if request.method == "POST":
            if paste.check_password(request.POST.get("password")):
                return render(request, "paste.html", {"paste": paste})
            else:
                return render(request, "password.html", {"paste": paste, "error": "Wrong password"})
        else:
            return render(request, "password.html", {"paste": paste})
    return render(request, "paste.html", {"paste": paste})