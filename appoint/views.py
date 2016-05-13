from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from .models import Appoint
from .forms import AppointForm


@require_POST
def apply_appoint(request):
    form = AppointForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect('/')
