from django import forms
from .models import Post, Comment 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    # visible field to enter tags as comma-separated text
    tags = forms.CharField(required=False, help_text="Comma-separated tags", label="Tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here'}),
        }

    def clean_tags(self):
        txt = self.cleaned_data.get('tags', '')
        # normalize: split by comma, strip and ignore empties
        tags = [t.strip() for t in txt.split(',') if t.strip()]
        return tags

# keep CommentForm and CustomUserCreationForm from earlier
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
                              label='')

    class Meta:
        model = Comment
        fields = ['content']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
