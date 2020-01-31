from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField


from wagtail.snippets.models import register_snippet



@register_snippet
class People(models.Model):
    first_name = models.CharField("First name", max_length=254)
    last_name = models.CharField("Last name", max_length=254)
    job_title = models.CharField("Job title", max_length=254)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('job_title'),
        ImageChooserPanel('image')
    ]

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    api_fields = [
        APIField('body')
    ]
