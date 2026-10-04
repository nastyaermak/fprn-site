from django.shortcuts import render

from .models import ExchangeProgram


def program_list(request):
    programs = ExchangeProgram.objects.all()
    return render(request, "exchange/program_list.html", {"programs": programs})
