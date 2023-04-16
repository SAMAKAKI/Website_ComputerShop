from django.db import models
from django.urls import reverse


class CatComputerElems(models.Model):
    name = models.CharField(verbose_name='Nazwa kategorii', max_length=255)
    slug = models.SlugField(verbose_name='URL kategorii', unique=True, db_index=True, max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat_elem', kwargs={'cat_elem_slug': self.slug})

    class Meta:
        verbose_name = 'Kategoria dla elementów'
        verbose_name_plural = 'Kategorie dla elementów'


class ComputerElems(models.Model):
    title = models.CharField(verbose_name='Nagłówek', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=255)
    content = models.TextField(verbose_name='Cały tekst', blank=True)
    photo = models.ImageField(verbose_name='Zdjęcie', upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(verbose_name='Czas tworzenia', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Czas aktualizacji', auto_now=True)
    available = models.BooleanField(verbose_name='Dostępny', default=True)
    price = models.FloatField(verbose_name='Cena', null=True, default=100)
    cat = models.ForeignKey(CatComputerElems, on_delete=models.PROTECT, verbose_name='Kategoria')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_elem', kwargs={'post_elem_slug': self.slug})

    class Meta:
        verbose_name = 'Element komputera'
        verbose_name_plural = 'Elementy komputera'
