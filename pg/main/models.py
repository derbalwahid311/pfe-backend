from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Doctorant(models.Model):
    id = models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50,null=True)
    prenom=models.CharField(max_length=50,null=True)
    date_de_naissance= models.DateField( help_text='dd-mm-yy')
    lieu_de_naissance=models.CharField(max_length=50,null=True)
    adresse=models.CharField(max_length=150,null=True)
    Telephone=models.IntegerField(null=True)
    adresse_email = models.EmailField() 
    num_bac=models.IntegerField(null=True)
    annèe_bac=models.IntegerField(null=True)
    annèe_premiere_inscription=models.IntegerField(null=True)
    type = [('lmd', 'Lmd'),('classique', 'Classique'),]   
    Type = models.CharField(max_length=10, choices=type)
    
    def __str__(self):
        return f'{self.id} - {self.nom} {self.prenom}'
    def __str__(self):
        return f'  ID_Doctorant : {self.id}'
    class Meta:
        verbose_name = "Ajoute Doctorant"
        verbose_name_plural = "Ajoute Doctorants"

class Publication(models.Model):
    #pdf_file = models.FileField(
        #upload_to='pdfs/',
       # #verbose_name='PDF File',
       # help_text='Upload a PDF file',
        #validators=[FileExtensionValidator(['pdf'])])
    Titre_Publication=models.CharField(max_length=300,null=True)
    ID_Doctorantt =models.ForeignKey(Doctorant,on_delete=models.CASCADE,default=0)


    



class Enseignant(models.Model):
     id = models.AutoField(primary_key=True)
     nom=models.CharField(max_length=50,null=True)
     prenom=models.CharField(max_length=50,null=True)
     date_de_naissance= models.DateField()
     lieu_de_naissance=models.CharField(max_length=50,null=True, help_text='dd-mm-yy')
     Telephone=models.IntegerField(null=True)
     adresse_email = models.EmailField()
     Domain_competence = [('mcb', 'Mcb'),('mca', 'Mca'),('maa', 'Maa'),]
     Domain_competence  = models.CharField(max_length=10, choices=Domain_competence, default='option1')
     OPTION_CHOICES = [('externe', 'Externe'),('interne', 'Interne'),]
     my_field = models.CharField(max_length=10, choices=OPTION_CHOICES, default='option1')
     username = models.CharField(max_length=150,default=0)
     password = models.CharField(max_length=128,default=0)
     def __str__(self):
         return f'{self.id} - {self.nom} {self.prenom}'
     def __str__(self):
         return f'  ID_Enseignant : {self.id}'
     class Meta:
        verbose_name = "Ajoute Enseignant"
        verbose_name_plural = "Ajoute Enseignants"
     
class Inscription(models.Model):
   ID_Doctorant =models.ForeignKey(Doctorant,on_delete=models.CASCADE)
   ID_Directeur_these =models.ForeignKey(Enseignant,on_delete=models.CASCADE,default=0,related_name='directeur_inscriptions')
   ID_Co_Directeur_these =models.ForeignKey(Enseignant,on_delete=models.CASCADE,default=0,related_name='co_directeur_inscriptions')
   Titre_Sujet=models.CharField(max_length=300,null=True)
   annèe_inscription=models.IntegerField(null=True)
   Taux_Avencement=models.IntegerField(null=True)
   Date_Probable_Soutenance=models.DateField( help_text='dd-mm-yy')
   Observation=models.TextField(null=True)
   
