from django.db import models

class Autor(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    datum_narozeni = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'

class Novela(models.Model):
    nazev = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, related_name='novely', on_delete=models.CASCADE)
    datum_vydani = models.DateField()

    def __str__(self):
        return self.nazev

class Recenze(models.Model):
    novela = models.ForeignKey(Novela, related_name='recenze', on_delete=models.CASCADE)
    obsah = models.TextField()
    hodnoceni = models.IntegerField()  # Assuming a rating system, e.g., 1-5 stars
    datum_recenzovani = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Recenze na {self.novela.nazev}'