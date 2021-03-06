from django.conf import settings
from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import TaggedItemBase

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.core.templatetags import wagtailcore_tags
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from rest_framework.fields import Field

from home.models import People

# Create your models here.

class AuthorSerializedField(Field):

    def to_representation(self, value):
        try:
            avatar_url = "{}{}".format(settings.BASE_URL, value.image.file.url)
        except:
            avatar_url = None
        return {
            "id": value.id,
            "first_name": value.first_name,
            "last_name": value.last_name,
            "job_title": value.job_title,
            "avatar": avatar_url,
        }

class ArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.ArticlePage', on_delete=models.CASCADE, related_name='tagged_items')

class AllArticles(Page):
    description = models.CharField(max_length=255, blank=True)
    
    control_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        ]

class ArticlePage(Page):
    description = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    content_image = models.ForeignKey(
            "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
        )
    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)
    author = models.ForeignKey(
        People,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        )
    

    def rendered_body(self):
        return wagtailcore_tags.richtext(self.body)

    def content_image_url(self):
        try:
            return '{}{}'.format(settings.BASE_URL, self.content_image.file.url)
        except:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('body', classname='full'),
        ImageChooserPanel("content_image"),
        FieldPanel('tags'),
        FieldPanel('author'),
    ]

    api_fields = [
        APIField('description'),
        APIField('rendered_body'),
        APIField('content_image_url'),
        APIField('tags'),
        APIField('author', serializer=AuthorSerializedField()),
    ]

class TestPage(Page):
    pass
