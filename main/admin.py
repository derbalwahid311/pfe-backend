from django.contrib import admin
from .models import Doctorant, Enseignant, Inscription, Publication,Journal,Etablissement


admin.site.site_header = 'Administration'



class DoctorantAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']

admin.site.register(Doctorant, DoctorantAdmin)

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']

admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Inscription)
admin.site.register(Publication)
admin.site.register(Journal)
admin.site.register(Etablissement)


