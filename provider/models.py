

# Django
from django.db import models




class Articles(models.Model):


    productId = models.CharField(null=True,blank=False,max_length=100)
    title = models.CharField(null=True,blank=False,max_length=100)

    proce = models.CharField(
        'Precio del producto',
        null=True,
        blank=False,
        max_length=100
    )

    picture = models.URLField(
        'Url de la previsualizacion del producto',
        null=True,
        blank=False
    )

    origin = models.URLField(
        'url del producto',
        null=True,
        blank=False
    )


    date = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> (str):
        return self.title



