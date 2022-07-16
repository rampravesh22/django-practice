from django.forms import ModelForm
from blog.models import Blog

class AddBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["title",'desc']