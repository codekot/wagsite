from django.core.management.base import BaseCommand
from faker import Faker
from articles.models import ArticlePage, TestPage

class Command(BaseCommand):
    help = 'Command to populate database'

    def handle(self, *args, **options):
        result = ""
        if options['news']:
            result += "You want to create {} news items \n".format(options['news'])
        if options['articles']:
            result += "You want to create {} articles items \n".format(options['news'])
        if options['stories']:
            result += "You want to create {} story items \n".format(options['news'])

        else:
            a = TestPage(title="Main Article", depth=4, path="0001000100010003")
            a.save()
            return "Working great!"

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--news',
            action='store',
            default=False,
            required=False,
            help='Add specified amount of news items')
        parser.add_argument(
            '-a',
            '--articles',
            action='store',
            default=False,
            help='Add specified amount of article items')
        parser.add_argument(
            '-s',
            "--stories",
            action='store',
            default=False,
            help='Add specified amount of story items')