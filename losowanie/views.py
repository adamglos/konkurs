from random import randint
from django.shortcuts import render

from losowanie.forms import LosowanieForm

# Create your views here.


def losowanie(request):

    form = LosowanieForm(request.GET)

    lista = request.GET.get("q").split(",")

    wybrana = lista[randint(0, len(lista) - 1)]

    return render(
        request,
        "losowanie.html",
        {
            "form": form,
            "wybrana": wybrana,
        },
    )
