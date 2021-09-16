from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=200,
    )
    description_short = models.TextField()
    description_long = models.TextField(
        blank=True,
    )
    coordinate_lng = models.DecimalField(
        max_digits=20,
        decimal_places=17,
        verbose_name='долгота'
    )
    coordinate_lat = models.DecimalField(
        max_digits=20,
        decimal_places=17,
        verbose_name='широта'
    )

    def __str__(self):
        return '{0}'.format(self.title)
