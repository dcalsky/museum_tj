from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from .models import Appoint


@require_POST
def apply_appoint(request):
    appoint = Appoint(
        name=request.POST.get('name'),
        phone=request.POST.get('phone'),
        note=request.POST.get('note'),
        time=request.POST.get('time'),
        amount=request.POST.get('amount')
    )
    appoint.save()
    return HttpResponse("预约成功!")
