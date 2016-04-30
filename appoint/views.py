from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from .models import Appoint


@require_POST
def apply_appoint(request):
    appoint = Appoint(
        name=request.POST.get('name'),
        time=request.POST.get('time'),
        note=request.POST.get('note'),
        email=request.POST.get('email'),
        phone=request.POST.get('phone')
    )
    appoint.save()
    return HttpResponse('apply for appointment successfully!')
