from flask_admin.contrib.sqla import ModelView
from jinja2 import Markup


class ProductAdminView(ModelView):
    can_view_details = True
    column_display_pk = True
    column_list = ('id', 'name', 'categories', 'price', 'slug',)
    please_do_show_primary_keys_value = True


class CategoryAdminView(ModelView):
    can_view_details = True
    column_list = ('id', 'name', 'slug', 'parent',)
    please_do_show_primary_keys_value = True


class IngredientAdminView(ModelView):
    can_view_details = True
    column_list = ('id', 'name',)
    please_do_show_primary_keys_value = True


class ImageView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.src:
            return ''

        return Markup('<img src="{url}" width=200 height=200 />'.format(url=model.src))

    column_formatters = {
        'src': _list_thumbnail,
    }
