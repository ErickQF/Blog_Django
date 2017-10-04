from django.db import models


class Category(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural= 'Categories'

    def __unicode__(self):
        return self.nome


class Post(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    content = models.TextField()
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


