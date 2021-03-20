from pathlib import Path
from django.core.management.base import BaseCommand

import django.apps
from django.conf import settings
from import_export import resources
from pathlib import Path

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--base_path', default='export\\')
        parser.add_argument('--data_type', default='csv')
        parser.add_argument('--models', default='')
        parser.add_argument('--exclude', default='')

    def handle(self, *args, **kwargs):
        models = django.apps.apps.get_models()
        models_cp = models.copy()
        model_names = kwargs['models'].split(',') if kwargs['models'] else ''
        excl_model_names = kwargs['exclude'].split(',') if kwargs['exclude'] else ''
        # Add models
        if model_names:
            for model in models:
                if model.__name__ not in model_names:
                    models_cp.remove(model)
        # Ecxlude models
        if excl_model_names:
            for model in models:
                if model.__name__ in excl_model_names:
                    models_cp.remove(model)
        # Export
        for model in models_cp:
            base_path = slash_check(kwargs['base_path'])
            data_type = '.' + kwargs['data_type']
            path = base_path + model.__module__.split('.')[-2] + '\\'
            Path(get_path(path)).mkdir(parents=True, exist_ok=True)
            export_path = get_path(path + model.__name__ + data_type)
            resource = resources.modelresource_factory(model=model)()
            dataset = resource.export()
            with open(export_path, 'w', newline='', encoding='utf-8') as w:
                w.write(dataset.csv)


def get_path(dir_name):
    str_path = str(settings.BASE_DIR)
    path = Path(str_path + '\\' + dir_name)
    return path

def slash_check(stroke):
    if stroke[0] != '\\':
        stroke = '\\' + stroke
    if stroke[-1] != '\\':
        stroke = stroke + '\\'
    return stroke