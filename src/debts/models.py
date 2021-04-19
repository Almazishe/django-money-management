from django.db import models
from django.contrib.auth import get_user_model

from utils.models import DateModel

from src.banks.models import Bank

User = get_user_model()



class OperationCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория операции"
        verbose_name_plural = "Категории операций"


class Debt(DateModel, models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="debts")
    with_whom = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    amount_left = models.FloatField(default=0)
    to_me = models.BooleanField(default=False)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, related_name="debts")
    debt_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(OperationCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="debts")
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Долг"
        verbose_name_plural = "Долги"
        
    def __str__(self):
        return f"{self.owner.username} - {self.with_whom} - {self.amount}"

class DebtRepayment(DateModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="debt_payments")
    debt = models.ForeignKey(Debt, on_delete=models.SET_NULL, null=True, related_name="debt_payments")
    amount = models.FloatField(default=0)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Возврат долга"
        verbose_name_plural = "Возвраты долгов"

    def __str__(self):
        return f"{self.user.username} - {self.debt.with_whom} - {self.amount}"


class Operation(DateModel, models.Model):
    OPERATION_TYPE_CHOICES = (
        ('+', "Прибыль"),
        ("-", "Убыток")
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="operations")
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, related_name="operations")
    type = models.CharField(max_length=10, choices=OPERATION_TYPE_CHOICES)
    amount = models.FloatField(default=0)
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(OperationCategory, on_delete=models.SET_NULL, null=True, related_name="operations")
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        
class Transfer(DateModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="transfers")
    from_bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, related_name="from_transfers")
    to_bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, related_name="to_transfers")
    amount = models.FloatField(default=0)
    category = models.ForeignKey(OperationCategory, on_delete=models.SET_NULL, null=True, related_name="transfers")
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Перевод по счету"
        verbose_name = "Переводы по счетам"
