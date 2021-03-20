from django.core.management.base import BaseCommand
from import_export import resources
import os
from pathlib import Path
from django.conf import settings
import tablib
import ntpath
import django.apps

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', default='\export\\')

    def handle(self, *args, **kwargs):
        paths = get_paths(kwargs['path'])
        for path in paths:
            with open(path, 'r', newline='', encoding='utf-8') as f:
                model_name = ntpath.basename(f.name).split('.')[0]
                ext = path[path.rfind('.') + 1:]
                models = django.apps.apps.get_models()
                dataset = tablib.Dataset()
                for model in models:
                    if model_name == model.__name__:
                        fields = []
                        for field_name in model._meta.get_fields():
                            fields.append(field_name.name)
                        f.seek(0)
                        field = f.readline().replace('\r\n', '').split(',')
                        if fields.sort() == field.sort():
                            dataset.load(f.read(), format=ext)
                            resource = resources.modelresource_factory(model=model)()
                            resource.import_data(dataset)
                            print(f'{model.__name__:<20} Success!')

def get_paths(path):
    path = slash_check(path)
    base_path = str(settings.BASE_DIR) + path
    file_paths = []
    for (dirpath, dirnames, filenames) in os.walk(Path(base_path)):
        for file in filenames:
            file_paths.append(dirpath + '\\' + file)
    return file_paths

def slash_check(stroke):
    if stroke[0] != '\\':
        stroke = '\\' + stroke
    if stroke[-1] != '\\':
        stroke = stroke + '\\'
    return stroke

