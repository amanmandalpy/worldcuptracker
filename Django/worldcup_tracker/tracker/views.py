from django.shortcuts import render

from .services import get_matches

# Create your views here.

def home(request):
    matches = get_matches()
    

    return render(
        request,
        "tracker/index.html",
        {
            "matches": matches
        }
    )
