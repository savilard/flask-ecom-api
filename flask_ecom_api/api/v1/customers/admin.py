from flask_admin.contrib.sqla import ModelView


class CustomerAdminView(ModelView):
    """Customer admin view."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        'name',
        'date_of_birth',
        'email',
    )


class CustomerShippingAddressAdminView(ModelView):
    """Customer shipping address admin view."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        'first_name',
        'last_name',
        'country',
        'city',
        'street',
        'house_number',
        'apartment_number',
    )
