from django.contrib import admin
from .models import Lekarz, Lek, Recepta, Objaw, Choroba, Pacjent, Wizyta, Dyzur

# Register your models here.

admin.site.register(Lekarz)
admin.site.register(Lek)
admin.site.register(Recepta)
admin.site.register(Objaw)
admin.site.register(Choroba)
admin.site.register(Pacjent)
admin.site.register(Wizyta)
admin.site.register(Dyzur)
