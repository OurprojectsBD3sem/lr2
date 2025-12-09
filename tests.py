from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Ad


class AdValidatorsTest(TestCase):
    def test_title_too_short_is_invalid(self):
        ad = Ad(
            title='abc',          # меньше 4 символов
            price=100,
            contact_email='user@example.com',
            website='https://example.com',
            slug='test-ad'
        )
        with self.assertRaises(ValidationError):
            ad.full_clean()       # запускает все валидаторы модели

    def test_title_long_enough_is_valid(self):
        ad = Ad(
            title='Нормальный заголовок',
            price=100,
            contact_email='user@example.com',
            website='https://example.com',
            slug='normal-ad'
        )
        # Не должно выбрасывать ValidationError
        ad.full_clean()

    def test_price_below_min_is_invalid(self):
        ad = Ad(
            title='Корректный заголовок',
            price=-10,            # меньше 0
            contact_email='user@example.com',
            website='https://example.com',
            slug='bad-price'
        )
        with self.assertRaises(ValidationError):
            ad.full_clean()

    def test_price_not_multiple_of_step_is_invalid(self):
        ad = Ad(
            title='Корректный заголовок',
            price=95,             # не кратно 10
            contact_email='user@example.com',
            website='https://example.com',
            slug='bad-step'
        )
        with self.assertRaises(ValidationError):
            ad.full_clean()

    def test_email_invalid(self):
        ad = Ad(
            title='Корректный заголовок',
            price=100,
            contact_email='not-an-email',  # некорректный e-mail
            website='https://example.com',
            slug='bad-email'
        )
        with self.assertRaises(ValidationError):
            ad.full_clean()

