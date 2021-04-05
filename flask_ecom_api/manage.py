import importlib
import os

from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand

from flask_ecom_api import create_app, db

PROJECT_DIRECTORY = 'flask_ecom_api'


def import_models() -> None:
    """Import models for migrate of flask_migrate."""
    for dir_path, _, file_names in os.walk(PROJECT_DIRECTORY):
        for file_name in file_names:
            if file_name != 'models.py':
                continue
            file_path_wo_ext, _ = os.path.splitext((os.path.join(dir_path, file_name)))
            module_name = file_path_wo_ext.replace(os.sep, '.')
            importlib.import_module(module_name)


if __name__ == '__main__':
    import_models()

    app = create_app()
    migrate = Migrate(app, db)
    cli = FlaskGroup(create_app=create_app)
    cli.add_command('db', MigrateCommand)  # type: ignore

    cli()
