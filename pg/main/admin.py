from django.contrib import admin
from .models import  Doctorant,Enseignant,Inscription,Publication

class DoctorantAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']  # Specify the fields to display in the list view
admin.site.register(Doctorant, DoctorantAdmin)

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']
admin.site.register(Enseignant,EnseignantAdmin)
admin.site.register(Inscription)
admin.site.register(Publication)

    