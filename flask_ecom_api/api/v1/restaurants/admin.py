from flask_admin.contrib.sqla import ModelView


class RestaurantAdminView(ModelView):
    """Restaurant admin view."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        'name',
        'address',
        'latitude',
        'longitude',
        'contact_phone',
    )
    please_do_show_primary_keys_value = True


class CourierAdminView(ModelView):
    """Courier admin view."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        'first_name',
        'last_name',
        'contact_phone',
        'vk_id',
        'tg_id',
        'fb_id',
    )
    please_do_show_primary_keys_value = True


class RestaurantCourierAdminView(ModelView):
    """Restaurant courier admin view."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        'courier.first_name',
        'courier.last_name',
        'courier.contact_phone',
        'restaurant.name',
    )
    please_do_show_primary_keys_value = True


class RestaurantProductAdminView(ModelView):
    """Restaurant product admin view."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        'product.name',
        'restaurant.name',
        'availability',
    )
    please_do_show_primary_keys_value = True
