from django import forms
from .models import Question


class MyForm1(forms.ModelForm):

    class Meta:
        model = Question
        fields = ["name_text", "ic_text", "phone_text", "income", "address1", "address2", "city", "mukim", "parlimen", "state", "poskod"]
        labels = {'name_text': "name", "ic_text": "ic", "phone_text": "phone", 'income': "Income", 'address1': "Address1", 'address2': "Address2", 'city': "City", 'mukim': "Mukim", 'parlimen': "Parlimen", 'state': "State", 'poskod': "Poskod"}
        widgets = {
            'ic_text': forms.TextInput(
                attrs={'pattern': '(([[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01]))([0-9]{2})([0-9]{4})'}),
        }
    def __init__(self, *args, **kwargs):
        super(MyForm1, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['name_text'].widget.attrs['readonly'] = True
            self.fields['ic_text'].widget.attrs['readonly'] = True
            self.fields['income'].widget.attrs['readonly'] = True
            self.fields['address1'].widget.attrs['readonly'] = True
            self.fields['address2'].widget.attrs['readonly'] = True
            self.fields['city'].widget.attrs['readonly'] = True
            self.fields['mukim'].widget.attrs['readonly'] = True
            self.fields['parlimen'].widget.attrs['readonly'] = True
            self.fields['state'].widget.attrs['readonly'] = True
            self.fields['poskod'].widget.attrs['readonly'] = True
