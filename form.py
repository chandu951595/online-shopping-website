from django.forms import ModelForm
from .models import user
class wishlist(ModelForm):
    class Meta:
        model = user
        fields = '__all__'