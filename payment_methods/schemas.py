from ninja import ModelSchema

from payment_methods.models import PaymentMethod


class PaymentMethodIn(ModelSchema):
    class Meta:
        model = PaymentMethod
        fields = ["name", "description"]
        fields_optional = ["icon"]


class PaymentMethodOut(ModelSchema):
    class Meta:
        model = PaymentMethod
        fields = "__all__"
