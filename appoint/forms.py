from django.forms import ModelForm
from .models import Appoint


class AppointForm(ModelForm):
    class Meta:
        model = Appoint
        fields = ['name', 'phone', 'note']
