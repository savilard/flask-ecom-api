from flask_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
    """User admin view."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        'username',
        'email',
        'active',
        'created_date',
    )
    please_do_show_primary_keys_value = True
