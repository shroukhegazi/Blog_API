from django.db import models
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from model_utils import Choices
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext as _

# Create your models here.
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("blog_posts"))
    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('content'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_("Slug"))
    tags = TaggableManager()
    STATUS = Choices(('Draft', _('Draft')) , ('published',_('published')), ('archive', _('archive')))
    status = models.CharField( choices=STATUS, default=STATUS.published, max_length=12)
    

    def __str__(self):
        return self.title

    

class Comment (models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Author"))
    post= models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    content = models.TextField(_("Content"))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)   

    def __str__(self) ->str:
        return self.content