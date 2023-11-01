from django.db import models


class New(models.Model):
    title = models.CharField(verbose_name="Название заголовка", max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="news_images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.title}"
