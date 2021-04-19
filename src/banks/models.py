from django.db import models
from django.contrib.auth import get_user_model


from utils.models import DateModel

User = get_user_model()



class Bank(DateModel, models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='banks')

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    balance = models.FloatField(default=0.0)



    class Meta:
        verbose_name = "Банковский счет"
        verbose_name_plural = "Банковские счета"
        unique_together = ('owner', 'slug')
    
    def __str__(self) -> str:
        return f"{self.owner.username} - {self.name}"


    def operate(self, type: str, amount: float) -> None:
        operation_str = f"{self.balance} {type} {amount}"
        self.balance = eval(operation_str)
        self.save()
