from django.db import models
from django.conf import settings
from shorterurl.converter_url import create_short_url


class Short_link(models.Model):
    """
    Creates a short url based on the long one
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    long_url = models.URLField(max_length=500,verbose_name="Длинная ссылка")
    short_url = models.CharField(max_length=15, unique=True, blank=True, verbose_name="Короткая ссылка")
    user_use = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_short_url(self)

        super().save(*args, **kwargs)
