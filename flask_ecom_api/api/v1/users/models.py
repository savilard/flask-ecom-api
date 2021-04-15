import datetime

from sqlalchemy_utils import EmailType
from werkzeug.security import check_password_hash, generate_password_hash

from flask_ecom_api.app import db


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

    roles = db.relationship(
        'Role',
        secondary='user_role',
        lazy='joined',
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


class Role(db.Model):
    """Role model."""

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, index=True, nullable=False)
    description = db.Column(db.String(255))

    def __repr__(self):
        """Printable representation of Role model."""
        return self.name


class UserRole(db.Model):
    """Roles users model."""

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer(),
        db.ForeignKey('user.id'),
        index=True,
        nullable=False,
    )
    role_id = db.Column(
        db.Integer(),
        db.ForeignKey('role.id'),
        index=True,
        nullable=False,
    )

    user = db.relationship('User', lazy='joined')
    role = db.relationship('Role', lazy='joined')

    def __repr__(self):
        """Printable representation of UserRole model."""
        return f'<{self.user_id} - {self.role_id}>'
