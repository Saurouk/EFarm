
from django.db import models

class BlogPost(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_de_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
