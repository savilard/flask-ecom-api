import datetime
import enum

from sqlalchemy_utils import EmailType
from werkzeug.security import check_password_hash, generate_password_hash

from flask_ecom_api.api.v1.users.admin import UserAdminView
from flask_ecom_api.app import admin, db


class UserRoleEnum(enum.Enum):
    """Class for choosing user role."""

    guest = 'guest'
    admin = 'admin'
    manager = 'manager'


class User(db.Model):
    """User model."""

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(
        EmailType,
        index=True,
        unique=True,
        nullable=False,
    )

    password = db.Column(db.String(128))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    role = db.Column(
        db.Enum(UserRoleEnum),
        default=UserRoleEnum.guest,
        nullable=False,
    )

    def set_password(self, password):  # noqa: WPS615
        """Generate password hash."""
        self.password = generate_password_hash(password)  # noqa: WPS601

    def check_password(self, password):
        """Check password hash."""
        return check_password_hash(self.password, password)  # type: ignore

    def __repr__(self):
        """Printable representation of Users model."""
        return self.email


admin.add_view(UserAdminView(User, db.session, category='Users'))
