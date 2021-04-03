from flask_admin.contrib.sqla import ModelView
from jinja2 import Markup


class ImageView(ModelView):
    """Custom image view."""

    def _list_thumbnail(view, context, model, name):
        """Shows a thumbnail image in the admin area."""
        if not model.src:
            return ''

        return Markup('<img src="{url}" width=200 height=200 />'.format(url=model.src))

    column_formatters = {
        'src': _list_thumbnail,
    }
