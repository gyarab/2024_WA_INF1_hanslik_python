from django import forms
 

class CommentForm(forms.Form):
    text = forms.CharField(label='Komentar', widget=forms.Textarea)