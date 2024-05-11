import uuid

from django.shortcuts import get_object_or_404
from ninja import Router

from users.models import User
from users.schemas import UserIn
from users.schemas import UserOut


router = Router()


@router.post("/")
def create_user(request, payload: UserIn):
    user = User.objects.create(**payload.dict())
    return {"id": user.id}


@router.get("/", response=list[UserOut])
def list_users(request):
    users = User.objects.all()
    return users


@router.get("/{user_id}", response=UserOut)
def get_user(request, user_id: uuid.UUID):
    user = get_object_or_404(User, id=user_id)
    return user
