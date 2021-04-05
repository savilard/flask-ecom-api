from flask_admin.contrib.sqla import ModelView
from jinja2 import Markup


class ImageView(ModelView):
    """Custom image view."""

    def _list_thumbnail(view, context, model, name):  # noqa: N805
        """Shows a thumbnail image in the admin area."""
        if not model.src:
            return ''

        return Markup('<img src="{url}" width=200 height=200 />'.format(url=model.src))

    column_formatters = {
        'src': _list_thumbnail,
    }


class BaseModelView(ModelView):
    """Base model view."""

    def on_model_change(self, form, model, is_created):
        """Generates a slug when the model changes."""
        model.generate_slug()
        return super().on_model_change(form, model, is_created)
