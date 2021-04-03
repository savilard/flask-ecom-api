from flask_admin.contrib.sqla import ModelView

from flask_ecom_api.api.v1.common.custom_admin_views import ImageView


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


class ProductImageAdminView(ImageView):
    can_view_details = True
    column_list = ('id', 'src', 'is_main', 'product', )
    please_do_show_primary_keys_value = True
