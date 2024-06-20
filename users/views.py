import uuid

from django.shortcuts import get_object_or_404
from ninja import Router

from expenses.models import Expense
from users.models import User
from users.schemas import UserOut


router = Router()


@router.get("/", response=list[UserOut])
def list_users(request):
    users = User.objects.all()
    return users


@router.get("/me", response=UserOut)
def get_me(request):
    return get_object_or_404(User, id=request.current_user.id)


@router.get("/{user_id}", response=UserOut)
def get_user(request, user_id: uuid.UUID):
    user = get_object_or_404(User, id=user_id)
    return user


@router.get("/{user_id}/expenses", response=UserOut)
def get_user_expenses(request, user_id: uuid.UUID):
    user = get_object_or_404(Expense, user_id=user_id)
    return user
