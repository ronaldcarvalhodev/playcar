from django.contrib import admin
from .models import Carro, Cliente, Aluguel

# Register your models here.

admin.site.register(Carro)
admin.site.register(Cliente)
admin.site.register(Aluguel)