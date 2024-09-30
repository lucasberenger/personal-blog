from django import forms

# Comment form
class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={'class': 'form_control', 'placeholder': 'Your Name'}
        ),
        required=True,
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form_control', 'placeholder': 'Leave a comment!'}
        ),
        required=True,
    )

# Contact form
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your Name'}
        ),
        required=True,
    )
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'E-mail'}
        ),
        required=True,
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form_control', 'placeholder': 'Your Message'}
        ),
        required=True,
    )