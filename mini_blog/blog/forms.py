from django import forms
from django.core.exceptions import ValidationError

class UserCommentForm(forms.Form):
    comment_text = forms.CharField(max_length=2000, widget = forms.Textarea())
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

def clean(self):
        cleaned_data = super(UserCommentForm, self).clean()
        comment_text = cleaned_data.get('comment_text')
        if not comment_text:
            raise forms.ValidationError('You have to write something!')