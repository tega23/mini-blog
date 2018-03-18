from django import forms
from django.core.exceptions import ValidationError

class UserCommentForm(forms.Form):
    comment_text = forms.CharField(max_length=2000, widget = forms.Textarea(attrs={"style": "width: 800px; rows:'2'","placeholder": "Write your comment"}),)
    
def clean(self):
        cleaned_data = super(UserCommentForm, self).clean()
        comment_text = cleaned_data.get('comment_text')
        if not comment_text:
            raise forms.ValidationError('You have to write something!')