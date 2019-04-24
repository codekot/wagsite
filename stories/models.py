from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

# Create your models here.
class StoryPageTag(TaggedItemBase):
    content_object = ParentalKey('stories.StoryPage', on_delete=models.CASCADE, related_name='tagged_items')

class AllStories(Page):
    description = models.CharField(max_length=255, blank=True)

    control_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

class StoryPage(Page):
    author = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    content_image = models.ForeignKey(
            "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
        )
    tags = ClusterTaggableManager(through=StoryPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('body', classname='full'),
        ImageChooserPanel("content_image"),
        FieldPanel('tags')
    ]

    api_fields = [
        APIField('author'),
        APIField('body'),
        APIField('content_image'),
        APIField('tags')
    ]