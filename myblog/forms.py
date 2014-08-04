from django import forms
from myblog.models import myBlog
class PostForm(forms.ModelForm):
	class Meta:
		model = myBlog
		fields = ('title', 'body',)
#<a href="{% url 'myblog.views.newpost' %}" class="top-menu"><span class="glyphicon glyphicon-