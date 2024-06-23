import uuid

from django.shortcuts import get_object_or_404
from ninja import Router

from expense_categories.models import ExpenseCategory
from expenses.models import Expense
from expenses.schemas import ExpenseIn
from expenses.schemas import ExpenseOut
from payment_methods.models import PaymentMethod
from users.models import User

router = Router()


@router.post("")
def create_expense(request, payload: ExpenseIn):
    payload_dict = payload.dict()
    payload_dict["payment_method"] = PaymentMethod.objects.get(
        id=payload_dict["payment_method"]
    )
    payload_dict["category"] = ExpenseCategory.objects.get(id=payload_dict["category"])
    payload_dict["user"] = User.objects.get(id=request.current_user.id)

    expense = Expense.objects.create(**payload_dict)
    return {"id": expense.id}


@router.get("", response=list[ExpenseOut], by_alias=True)
def list_expenses(request):
    expenses = Expense.objects.all()
    return expenses


@router.get("/user", response=list[ExpenseOut])
def get_user_expenses(request):
    user_expenses = Expense.objects.filter(user_id=request.current_user.id).all()
    return user_expenses


@router.get("/{expense_id}", response=ExpenseOut)
def get_expense(request, expense_id: uuid.UUID):
    expense = get_object_or_404(Expense, id=expense_id)
    return expense
