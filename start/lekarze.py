from django.forms import ModelForm
from .models import *

class LekarzForm(ModelForm):
    class Meta:
        model = Lekarz
        fields = '__all__'

class LekForm(ModelForm):
    class Meta:
        model = Lek
        fields = '__all__' 

class ReceptaForm(ModelForm):
    class Meta:
        model = Recepta
        fields = '__all__'

class ObjawForm(ModelForm):
    class Meta:
        model = Objaw
        fields = '__all__'

class ChorobaForm(ModelForm):
    class Meta:
        model = Choroba
        fields = '__all__'

class PacjentForm(ModelForm):
    class Meta:
        model = Pacjent
        fields = '__all__'

class WizytaForm(ModelForm):
    class Meta:
        model = Wizyta
        fields = '__all__'


class DyzurForm(ModelForm):
    class Meta:
        model = Dyzur
        fields = '__all__'

