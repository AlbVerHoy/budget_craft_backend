import uuid

from django.shortcuts import get_object_or_404
from ninja import Router

from expense_categories.models import ExpenseCategory
from expense_categories.schemas import ExpenseCategoryIn
from expense_categories.schemas import ExpenseCategoryOut

router = Router()


@router.post("")
def create_expense_category(request, payload: ExpenseCategoryIn):
    expense_category = ExpenseCategory.objects.create(**payload.dict())
    return {"id": expense_category.id}


@router.get("", response=list[ExpenseCategoryOut])
def list_expense_categories(request):
    expense_categories = ExpenseCategory.objects.all()
    return expense_categories


@router.get("/{expense_category_id}", response=ExpenseCategoryOut)
def get_expense_category(request, expense_category_id: uuid.UUID):
    expense_category = get_object_or_404(ExpenseCategory, id=expense_category_id)
    return expense_category
