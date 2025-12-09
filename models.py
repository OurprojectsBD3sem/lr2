from django.db import models
from myproject.myproject import settings
from django.core import validators


# Две модели со связью один с одним
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Passport(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='passport'
    )
    number = models.CharField(max_length=20, unique=True)
    issued_at = models.DateField()

    def __str__(self):
        return f'Паспорт {self.number}'

# Связь один с многими
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='ads'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ads'
    )

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    tags = models.ManyToManyField(
        Tag,
        related_name='ads',
        blank=True
    )

    def __str__(self):
        return self.title

# Валидаторы
class Ad(models.Model):
    # Заголовок: от 4 до 50 символов
    title = models.CharField(
        max_length=50,
        validators=[
            validators.MinLengthValidator(
                4,
                message='Заголовок должен быть не короче 4 символов.'
            ),
            validators.ProhibitNullCharactersValidator()
        ],
        verbose_name='Заголовок'
    )

    # Цена: минимум 0, максимум 1 000 000, кратна 10
    price = models.IntegerField(
        validators=[
            validators.MinValueValidator(
                0,
                message='Цена не может быть меньше 0.'
            ),
            validators.MaxValueValidator(
                1_000_000,
                message='Цена не может быть больше 1 000 000.'
            ),
            validators.StepValueValidator(
                10,
                message='Цена должна быть кратна 10.'
            ),
        ],
        verbose_name='Цена'
    )

    # E‑mail продавца с EmailValidator
    contact_email = models.EmailField(
        validators=[
            validators.EmailValidator(
                message='Укажите корректный e‑mail.'
            )
        ],
        verbose_name='E‑mail для связи'
    )

    # URL сайта продавца с URLValidator
    website = models.URLField(
        blank=True,
        validators=[
            validators.URLValidator(
                schemes=['http', 'https'],
                message='Укажите корректный URL, начинающийся с http или https.'
            )
        ],
        verbose_name='Сайт продавца'
    )

    # Слаг объявления (часть URL) с validate_slug
    slug = models.SlugField(
        unique=True,
        validators=[validators.validate_slug],
        verbose_name='Слаг'
    )

    def __str__(self):
        return self.title
