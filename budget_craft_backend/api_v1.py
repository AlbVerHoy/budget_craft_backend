from ninja import NinjaAPI

from budget_craft_backend.auth_utils import AuthBearer
from expense_categories.views import router as expense_categories_router
from expenses.views import router as expenses_router
from payment_methods.views import router as payment_methods_router
from users.views import router as users_router


api = NinjaAPI(
    version="1.0.0",
    auth=AuthBearer(),
    openapi_extra={
        "info": {
            "termsOfService": "https://example.com/terms/",
        }
    },
    title="BudgetCraft API",
    description="This is a API for the BudgetCraft app, most of the operations revolve around expenses.",
)

api.add_router(prefix="expenses", router=expenses_router, tags=["Expenses"])
api.add_router(
    prefix="expense-categories",
    router=expense_categories_router,
    tags=["ExpenseCategories"],
)
api.add_router(
    prefix="payment-methods", router=payment_methods_router, tags=["PaymentMethods"]
)
api.add_router(prefix="users", router=users_router, tags=["Users"])
