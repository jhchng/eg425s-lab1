from django import forms

class FormName(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'placeholder':'Write Your Name',
            'required':'true'
            }
        )
    )
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
