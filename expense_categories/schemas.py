from ninja import ModelSchema

from expense_categories.models import ExpenseCategory


class ExpenseCategoryIn(ModelSchema):
    class Meta:
        model = ExpenseCategory
        fields = ["name", "description"]
        fields_optional = ["icon", "color"]


class ExpenseCategoryOut(ModelSchema):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"
