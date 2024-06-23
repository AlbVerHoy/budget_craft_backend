from ninja import ModelSchema

from expense_categories.schemas import ExpenseCategoryOut
from expenses.models import Expense
from payment_methods.schemas import PaymentMethodOut


class ExpenseIn(ModelSchema):
    class Meta:
        model = Expense
        fields = ["date", "amount", "description", "category", "payment_method"]
        fields_optional = [
            "is_recurring",
            "recurrence_frequency",
            "next_occurrence",
            "end_of_recurrence",
        ]


class ExpenseOut(ModelSchema):
    payment_method: PaymentMethodOut
    category: ExpenseCategoryOut

    class Meta:
        model = Expense
        fields = "__all__"
