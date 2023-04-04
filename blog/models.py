from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __str__(self) -> str:
        return self.slug

class Post(models.Model):
    standBy = 'standBy'
    published = 'published'
    removed= 'removed'
    
    STATUS_POST = (
        (standBy, 'standBy'),
        (published, ' published'),
        (removed, 'removed'),
    )

    post = models.CharField(max_length=200)
    date_published = models.DateTimeField('date_published')
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, null=True)
    category = models.ManyToManyField(Category)
    status = models.CharField(max_length=10, choices=STATUS_POST, default='standBy')

    def __str__(self) -> str:
        return self.post + " " + str(self.date_published)
