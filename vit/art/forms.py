from django.forms import ModelForm
from vit.art.models import *

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    exclude = ['post']
    
