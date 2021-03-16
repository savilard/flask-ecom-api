from flask.cli import FlaskGroup

from flask_ecom_api import app

cli = FlaskGroup(app)  # type: ignore


if __name__ == '__main__':
    cli()
