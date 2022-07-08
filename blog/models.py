from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def upload_to(self, filename):
    return 'blog/{filename}'.format(filename=filename)
    
class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name = 'Titulo',
    )

    content1 = models.TextField(
        verbose_name = 'Contenido principal',
    )

    content2 = models.TextField(
        blank = True,
        verbose_name = 'Parrafo opcional',
    )

    content3 = models.TextField(
        blank = True,
        verbose_name = 'Parrafo opcional',
    )

    resume = models.TextField(
        blank = True,
        verbose_name = 'Resumen'
    )

    created = models.DateTimeField(
        auto_now_add = True
    )

    principal_image  = models.ImageField(
        upload_to = upload_to,
        blank = True,
        null = True,
    )

    image1 = models.ImageField(
        upload_to = upload_to,
        blank = True,
        null = True,
    )

    image2 = models.ImageField(
        upload_to = upload_to,
        blank = True,
        null = True,
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.title
