from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from .models import Appoint
from .forms import AppointForm


@require_POST
def apply_appoint(request):
    appoint = Appoint(
        name=request.POST('name'),
        phone=request.POST('phone'),
        note=request.POST('note')
    )
    appoint.save()
    return HttpResponse("预约成功!")
