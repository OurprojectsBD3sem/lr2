from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name='Рубрика')
class Meta:
    verbose_name_plural = 'Объявления'
    verbose_name = 'Объявление'
    ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                                        verbose_name='Название')
    def __str__(self):
        return self.name
class Meta:
    verbose_name_plural = 'Рубрики'
    verbose_name = 'Рубрика'
    ordering = ['name']

class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Картинка', upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class ProductMeta(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='meta')
    name = models.CharField('Параметр', max_length=50)
    value = models.CharField('Значение', max_length=200, blank=True)

    def __str__(self):
        return f'{self.name}: {self.value}'