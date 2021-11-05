from django.contrib import admin
from .models import Prpdutos,Cliente

class Produtoadmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque')

admin.site.register(Prpdutos,Produtoadmin)
admin.site.register(Cliente)

