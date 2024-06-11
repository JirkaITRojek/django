from django.contrib import admin
from .models import Autor, Novela, Recenze

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'prijmeni', 'datum_narozeni')
    search_fields = ('jmeno', 'prijmeni')

@admin.register(Novela)
class NovelaAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'autor', 'datum_vydani')
    search_fields = ('nazev', 'autor__jmeno', 'autor__prijmeni')
    list_filter = ('datum_vydani',)

@admin.register(Recenze)
class RecenzeAdmin(admin.ModelAdmin):
    list_display = ('novela', 'hodnoceni', 'datum_recenzovani')
    search_fields = ('novela__nazev', 'obsah')
    list_filter = ('hodnoceni', 'datum_recenzovani')
