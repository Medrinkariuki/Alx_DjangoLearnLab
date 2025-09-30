from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
class Meta:
model = Post
fields = ['title', 'content', 'tags']
widgets = {
'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your post here...'}),
'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'}),
}

class CommentForm(forms.ModelForm):
class Meta:
model = Comment
fields = ['content']
widgets = {
'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your comment...'}),
}

class SearchForm(forms.Form):
query = forms.CharField(
max_length=100,
required=False,
widget=forms.TextInput(attrs={
'class': 'form-control',
'placeholder': 'Search posts...'
})
)