from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name =  models.CharField(max_length=50, blank=True, null=True)
    customer_address = models.CharField(max_length=50, blank=True, null=True)
    telephone_number = models.CharField(max_length=10, default=0, blank=True, null=True)

    def __str__(self):
        return self.first_name + '' + self.last_name

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    paid_choice = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    paid = models.CharField(max_length=4,blank=True, null=True, choices=paid_choice)

    def __str__(self):
        return self.paid


class OrderItems(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.quantity)



class Stock(models.Model):
    game_title = models.CharField(max_length=50, blank=True, null=True)
    # category_choice = (
	#  	('Furniture', 'Furniture'),
	#  	('IT Equipment', 'IT Equipment'),
	#  	('Phone', 'Phone'),
	#  )
    # category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice)
    # category = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    # receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    # receive_by = models.CharField(max_length=50, blank=True, null=True)
    # issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    # issue_by = models.CharField(max_length=50, blank=True, null=True)
    # issue_to = models.CharField(max_length=50, blank=True, null=True)
    # phone_number = models.CharField(max_length=50, blank=True, null=True)
    # created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True)
    stock_level = models.IntegerField(default=0, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.game_title + '' + str(self.quantity) + '' + self.manufacturer + '' + str(self.price)
	

    

    
        
		
	
		
