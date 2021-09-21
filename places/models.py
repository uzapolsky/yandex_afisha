from django.db import models
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='название',
    )
    description_short = models.TextField(
        blank=True,
        verbose_name='короткое описание',
    )
    description_long = HTMLField(
        blank=True,
        verbose_name='подробное описание',
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
        return self.title


class Image(models.Model):
    position = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        verbose_name='порядковый номер',
    )
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='место',
    )
    img = models.ImageField(
        verbose_name='изображение',
    )

    def __str__(self):
        return '{0} - {1}'.format(self.place.title, self.position)

    class Meta:
        ordering = ['position']
