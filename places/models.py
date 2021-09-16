from django.db import models
from django.db.models.deletion import CASCADE


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


class Image(models.Model):
    position = models.PositiveSmallIntegerField(default=0)
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE,
    )
    img = models.ImageField()

    def __str__(self):
        return '{0} - {1}'.format(self.place.title, self.position)

    class Meta:
        ordering = ['position']
