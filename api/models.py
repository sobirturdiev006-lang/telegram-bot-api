from django.db import models
from django.core.validators import RegexValidator


class Account(models.Model):
    """
    Model representing a Telegram user account.
    Stores user profile information synced from Telegram.
    """

    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='User first name'
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='User last name'
    )
    image = models.ImageField(
        upload_to='images/accounts/',
        null=True,
        blank=True,
        help_text='User profile image'
    )

    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Phone number must contain 9-15 digits',
                code='invalid_phone'
            )
        ],
        help_text='User phone number in international format'
    )

    telegram_id = models.CharField(
        unique=True,
        max_length=100,
        help_text='Unique Telegram user ID'
    )
    username = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Telegram username'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Account creation timestamp'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Account last update timestamp'
    )

    @property
    def full_name(self):
        """Return user full name, handling null values gracefully."""
        first = self.first_name or ''
        last = self.last_name or ''
        full_name = f'{first} {last}'.strip()
        return full_name if full_name else 'Unknown User'

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['telegram_id']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        """Return user full name or username as string representation."""
        return self.full_name or self.username or f'User {self.telegram_id}'
