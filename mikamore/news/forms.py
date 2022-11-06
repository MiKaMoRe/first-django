from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField()
    is_published = forms.BooleanField()
    # photo = forms.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all())

