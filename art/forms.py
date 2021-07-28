from django import forms
from .models import Art


class ArtForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-product-form'