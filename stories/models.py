from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.
class AllStories(Page):
    description = models.CharField(max_length=255, blank=True)

    control_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

class StoryPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full')
    ]