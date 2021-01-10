from django import forms
from .models import Stock, Category, Customer, Order, OrderItems

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['game_title', 'manufacturer', 'price','stock_level', 'reorder_level','category']
    def clean_category(self):
        category = self.cleaned_data['category']
        if not category:
            raise forms.ValidationError('This field is a required field')
        # for instance in Stock.objects.all():
        #     if instance.category == category:
        #         raise forms.ValidationError("Category already exists")
        return category

    def clean_gametitle(self):
        game_title = self.cleaned_data['game_title']
        if not game_title:
            raise forms.ValidationError("This field is required")
        return game_title
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be less than 0")
        return quantity
        

class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['game_title']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'game_title', 'quantity', 'manufacturer', 'price', 'reorder_level','stock_level']


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'customer_address', 'telephone_number']

    def clean_phonenumber(self):
        telephone_number = self.cleaned_data['telephone_number']
        if len(telephone_number) > 11:
            raise forms.ValidationError("Telephone number should be less than 10")
        return telephone_number


class CustomerSearchForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name']


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'customer_address', 'telephone_number']

# Order Form for creating the order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','paid']


class OrderSearchForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer']

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','paid']


class OrderItemsCreateForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = ['order', 'stock', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError("Quantity should be better than 0")
        return quantity


class OrderItemsSearchForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = ['order']


class OrderItemsUpdateForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = ['order', 'stock', 'quantity']