from flask_admin.contrib.sqla import ModelView


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


class CustomerAdminView(ModelView):
    can_view_details = True
    column_display_pk = True
    column_list = ('id', 'name', 'email',)
    please_do_show_primary_keys_value = True
