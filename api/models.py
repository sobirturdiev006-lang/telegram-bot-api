from django.db import models

class Account(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/accounts/', null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    telegram_id = models.CharField(unique=True, max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
        ordering = ['-created_at']


    def __str__(self):
        return self.full_name