from django import forms
from django.core import validators
class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
                               validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("bot caught")
    #     return botcatcher 
        # instead of all this function we can use inbuilt validator. 