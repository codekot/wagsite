from wagtail.core import hooks
from wagtail.core.models import Site
from wagtail.documents.models import get_document_model


def document_link_handler(attrs):
    """Handle a link of the form <a linktype="document" id="123">"""
    Document = get_document_model()
    try:
        report = Document.objects.get(id=attrs['id'])
    except (Document.DoesNotExist, KeyError):
        return "<a>"
    base_url = Site.objects.first().root_url
    return f'<a href="{base_url}{report.url}">'


@hooks.register('register_rich_text_features')
def register_document_feature(features):
    features.register_link_type('document', document_link_handler)


def init_wagtail_hooks():
    pass
