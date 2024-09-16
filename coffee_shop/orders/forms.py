from django.forms import Form, ModelForm
from .models import OrderProduct

class OrderProductForm(ModelForm):
    
    class Meta:
        
        model = OrderProduct
        fields = ['product']
