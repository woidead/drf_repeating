from django.db import models

class Celebrity(models.Model):
    title = models.CharField("Имя Фамилия", max_length=255)
    content = models.TextField("Информация", blank=True)
    time_create = models.DateTimeField("Время создания", auto_now_add=True)
    time_update = models.DateTimeField("Время изменения", auto_now_add=True)
    is_published = models.BooleanField("Опубликована", default=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    name = models.CharField("Название категории", max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.name
