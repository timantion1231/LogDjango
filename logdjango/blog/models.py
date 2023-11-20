from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class Post(models.Model):
    class PostStatus(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Pusblished")

    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.SlugField(max_length= 250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=PostStatus.choices, default=PostStatus.DRAFT)

    class Meta:
        ordering = ('-publish',)

        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('blog:post_detail',
                           args = [
                               self.publish.year,
                               self.publish.strftime('%m'),
                               self.publish.strftime('%d'),
                               self.slug,
                           ]
                           )