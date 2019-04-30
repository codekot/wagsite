from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.templatetags import wagtailcore_tags

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from demo_site.settings.base import BASE_DIR


# Create your models here.

class ArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.ArticlePage', on_delete=models.CASCADE, related_name='tagged_items')

class AllArticles(Page):
    description = models.CharField(max_length=255, blank=True)
    
    control_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        ]

class ArticlePage(Page):
    author = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    content_image = models.ForeignKey(
            "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
        )
    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)

    def rendered_body(self):
        body = wagtailcore_tags.richtext(self.body)
        from wagtail.core.models import Site
        body = body.replace('"/documents/', f'{Site.objects.first().root_url}/documents/')
        return body

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('body', classname='full'),
        ImageChooserPanel("content_image"),
        FieldPanel('tags')
    ]

    api_fields = [
        APIField('author'),
        APIField('rendered_body'),
        APIField('content_image'),
        APIField('tags')
    ]

class TestPage(Page):
    pass