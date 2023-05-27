from django import forms
from .models import dokumen as Dokumen

class DokumenForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(DokumenForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control textarea m-2 '
            field.widget.attrs['id'] = 'formFile '