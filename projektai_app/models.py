from django.db import models
from datetime import datetime

# Create your models here.
class Projektas(models.Model):
    pavadinimas = models.CharField('NT_projektas', max_length=40)
    plotas = models.FloatField('Plotas kv m')
    kaina = models.FloatField('Kaina be PVM')
    ivedimo_data = models.DateTimeField('Įved. data', default=datetime.now)

    def __str__(self):
        return f"{self.pavadinimas} {self.plotas} {self.kaina} {self.ivedimo_data}"

    @property
    def kaina_pvm(self):
        return round(self.kaina * 1.21, 2)

# !!!!! parašius naują modelio klasę, visada yra vykdomos migracijos
# python manage.py makemigrations
# python manage.py migrate
