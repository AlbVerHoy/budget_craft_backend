from typing import Optional

from ninja import ModelSchema

from users.models import User


class UserIn(ModelSchema):
    class Meta:
        model = User
        fields = ["email_address", "first_name", "last_name", "auth0_id"]
        fields_optional = ["avatar"]


class UserOut(ModelSchema):
    full_name: Optional[str] = None

    class Meta:
        model = User
        fields = ["id", "email_address", "first_name", "last_name", "avatar"]

    @staticmethod
    def resolve_full_name(obj):
        if not obj.first_name and obj.last_name:
            return
        return f"{obj.first_name} {obj.last_name}"
