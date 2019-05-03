from wagtail.core import hooks
from wagtail.core.models import Site
from wagtail.documents.models import get_document_model
from wagtail.images import get_image_model
from wagtail.images.formats import get_image_format
from wagtail.images.shortcuts import get_rendition_or_not_found


def document_link_handler(attrs):
    """Handle a link of the form <a linktype="document" id="123">"""
    Document = get_document_model()
    try:
        report = Document.objects.get(id=attrs['id'])
    except (Document.DoesNotExist, KeyError):
        return "<a>"
    base_url = Site.objects.first().root_url
    return f'<a href="{base_url}{report.url}">'


def image_link_handler(attrs):
    """Handle a link of the form <embed embedtype="image" id="123">"""
    # Default implementation from wagtail.images.rich_text.image_embedtype_handler
    Image = get_image_model()
    try:
        image = Image.objects.get(id=attrs['id'])
    except Image.DoesNotExist:
        return "<img>"

    image_format = get_image_format(attrs['format'])

    # form extra src attribute
    base_url = Site.objects.first().root_url
    rendition = get_rendition_or_not_found(image, image_format.filter_spec)
    extra_attributes = {'src': f'{base_url}{rendition.url}'}

    # From default implementation, except extra src attribute
    return image_format.image_to_html(image, attrs.get('alt', ''), extra_attributes)


@hooks.register('register_rich_text_features')
def register_document_feature(features):
    features.register_link_type('document', document_link_handler)


@hooks.register('register_rich_text_features')
def register_image_feature(features):
    features.register_embed_type('image', image_link_handler)


def init_wagtail_hooks():
    pass
