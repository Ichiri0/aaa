from django.db import models

# Create your models here.

class User(models.Model):
    last_name = models.CharField('Фамилия', max_length=40)
    name = models.CharField('Имя', max_length=40)
    middle_name = models.CharField('Отчество', max_length=40)
    email = models.CharField('Электронная почта', max_length=100)
    phone = models.CharField('Телефон', max_length=12)

    def __str__(self):
        return f"{self.last_name} {self.name} {self.middle_name} {self.phone}"


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Tattoo(models.Model):
    title = models.CharField("Наименование", max_length=50, default='Татуировка')
    date = models.DateField("Дата")
    time = models.TimeField("Время")
    duration = models.IntegerField('Длительность процедуры', default=15)
    is_busy_tatt = models.BooleanField(default=False, verbose_name='Отметьте, если занято.')

    def __str__(self):
        busy = "Нет записей на это время. "
        if self.is_busy_tatt:
            busy = "На это время есть запись!"
        return f"Время: {self.time} | Дата: {self.date}  | Длительность: {self.duration} мин. | {busy} | Процедура: {self.title} "

    class Meta:
        verbose_name = 'Запись '
        verbose_name_plural = 'Записи. Тату. '

class Piercing(models.Model):
    title = models.CharField("Наименование", max_length=50, default='Татуировка')
    date = models.DateField("Дата")
    time = models.TimeField("Время")
    duration = models.IntegerField('Длительность процедуры', default=30)
    is_busy_pier = models.BooleanField(default=False, verbose_name='Отметьте, если занято.')

    def __str__(self):
        busy = "Нет записей на это время. "
        if self.is_busy_pier:
            busy = "На это время есть запись!"
        return f"Время: {self.time} | Дата: {self.date}  | Длительность: {self.duration} мин. | {busy} | Процедура: {self.title} "

    class Meta:
        verbose_name = 'Запись '
        verbose_name_plural = 'Записи. Пирсинг. '



class Goods(models.Model):
    name = models.CharField('Наименование', max_length=80)
    image = models.ImageField('Изображение', default='no_image.jpg', upload_to='goods')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
