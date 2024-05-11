import uuid

from django.shortcuts import get_object_or_404
from ninja import Router

from expenses.models import Expense
from expenses.schemas import ExpenseIn
from expenses.schemas import ExpenseOut


router = Router()


@router.post("/")
def create_expense(request, payload: ExpenseIn):
    expense = Expense.objects.create(**payload.dict())
    return {"id": expense.id}


@router.get("/", response=list[ExpenseOut], by_alias=True)
def list_expenses(request):
    expenses = Expense.objects.all()
    return expenses


@router.get("/{expense_id}", response=ExpenseOut)
def get_expense(request, expense_id: uuid.UUID):
    expense = get_object_or_404(Expense, id=expense_id)
    return expense
