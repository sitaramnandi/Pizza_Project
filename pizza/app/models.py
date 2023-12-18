from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models import Sum

# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract=True

class PizaaCategory(BaseModel):
    category_name=models.CharField(max_length=100)

class Pizza(BaseModel):
    category=models.ForeignKey(PizaaCategory,on_delete=models.CASCADE,related_name="pizzas")
    pizza_name=models.CharField(max_length=100)
    price=models.IntegerField(default=100)
    image=models.ImageField(upload_to="pizza")

class Cart(BaseModel):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="carts")
    is_paid=models.BooleanField(default=False)
 
    instamojo_id = models.CharField(max_length=100)  
    def get_cart_total(self):
        return CartItems.objects.filter(cart =self).aggregate(total_price=Sum("pizaa__price")).get('total_price') or 0
class CartItems(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    pizaa=models.ForeignKey(Pizza,on_delete=models.CASCADE)



class Name():
    full=models.CharField(max_length=100)


