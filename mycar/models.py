from django.db import models

class Car(models.Model):
    TRN_CHOICES = [
        ( 1 , 'механика'),
        ( 2 , 'автомат'),
        ( 3 , 'робот'),
    ]
    manufacturer = models.CharField(max_length=200, verbose_name='производитель')
    model = models.CharField(max_length=200, verbose_name='модель авто')
    year_start = models.IntegerField(verbose_name='год выпуска')
    transmission = models.SmallIntegerField(choices= TRN_CHOICES, verbose_name='коробка передач')
    color = models.CharField(max_length=100, verbose_name='цвет')

    def __str__(self):
        return f'Модель авто: {self.model}, {self.manufacturer}, {self.year_start} года выпуска, коробка передач: {self.get_transmission_display()}, цвет: {self.color}'