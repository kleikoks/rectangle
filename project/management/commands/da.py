from django.core.management import BaseCommand
import datetime

global response
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        d = datetime.date.today()
        tdelta = datetime.timedelta(days=7)
        print(d + tdelta)
        print(d.isoweekday())

def fprint(data):
    for item in data:
        print(item)