from django.db import models


class Menu(models.Model):
    """Меню"""

    name = models.CharField(
        max_length=100,
        verbose_name='Название меню',
        unique=True
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категории меню."""

    name = models.CharField(max_length=100, verbose_name='Название категории')
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='cats'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Подкатегории."""

    name = models.CharField(
        max_length=100,
        verbose_name='Название подкатегории'
    )
    cat = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcats'
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name
