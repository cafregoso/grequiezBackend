from django.db import models

# Create your models here.

class Newsletter(models.Model):
    name = models.CharField(
        max_length = 120,
        verbose_name = 'Nombre',
    )

    email = models.EmailField(
        verbose_name='Email'
    )

    created = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return self.email