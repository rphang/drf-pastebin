from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .models import Paste

def index(request):
    pastes = Paste.objects.all()
    return render(request, "index.html", {"pastes": pastes})

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