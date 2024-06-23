from ninja import Router

from payment_methods.models import PaymentMethod
from payment_methods.schemas import PaymentMethodIn
from payment_methods.schemas import PaymentMethodOut

router = Router()


@router.post("")
def create_expense_category(request, payload: PaymentMethodIn):
    expense_category = PaymentMethod.objects.create(**payload.dict())
    return {"id": expense_category.id}


@router.get("", response=list[PaymentMethodOut])
def list_payment_methods(request):
    payment_methods = PaymentMethod.objects.all()
    return payment_methods
