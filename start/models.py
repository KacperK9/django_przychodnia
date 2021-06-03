from django.db import models

# Create your models here.

class Lekarz(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=255)
    dataUrodzenia = models.DateField()
    PESEL = models.CharField(max_length=11)
    specjalizacja = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.imie+' '+self.nazwisko+'('+self.specjalizacja+')'

    class Meta:
        verbose_name_plural = "Lekarz"

class Lek(models.Model):
    nazwa = models.CharField(max_length=255)
    refundacja = models.SmallIntegerField()
    wymaganaRecepta = models.BooleanField()
    class Meta:
        verbose_name_plural = "Lek"

class Recepta(models.Model):
    dataWystawienia = models.DateField()
    dataWaznosci = models.DateField()
    idLek = models.ForeignKey(to=Lek, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Recepta"    


class Objaw(models.Model):
    nazwaObjawu = models.CharField(max_length=64)
    opis = models.CharField(max_length=1024)
    class Meta:
        verbose_name_plural = "Objaw"


class Choroba(models.Model):
    nazwaChoroby = models.CharField(max_length=255)
    opis = models.CharField(max_length=1024)
    zakazna = models.BooleanField(default=False)
    idObjaw = models.ForeignKey(to=Objaw, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Choroba"


class Pacjent(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=255)
    data_urodzenia = models.DateField()
    PESEL = models.CharField(max_length=11)
    idChoroba = models.ForeignKey(to=Choroba, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.imie+' '+self.nazwisko

    class Meta:
        verbose_name_plural = "Pacjent"


class Wizyta(models.Model):
    dataWizyty = models.DateField()
    godzina = models.TimeField()
    idRecepta = models.ForeignKey(to=Recepta, on_delete=models.CASCADE)
    idLekarz = models.ForeignKey(to=Lekarz, on_delete=models.CASCADE)
    idPacjent = models.ForeignKey(to=Pacjent, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Wizyta"


class Dyzur(models.Model):
    czasRozpoczecia = models.DateTimeField()
    czasZakonczenia = models.DateTimeField()
    idLekarz = models.ForeignKey(to=Lekarz, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Dyzur"