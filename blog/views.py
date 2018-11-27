from django.shortcuts import render
from django.shortcuts import HttpResponse 
from django.views.generic import DetailView ,ListView
from .models import BlogPost ,UserProfile
from django.contrib.auth.forms import UserCreationForm
class Home(ListView):
	model=BlogPost
	template_name='home.html'

def profile(request):
	user=request.user
	args={'user':user}
	return render(request,'profile.html',args)

class Detail(DetailView):
	model=BlogPost
	template_name='detail.html'
	
#def profile(request):
#	return render(request,'profile.html')

	model=BlogPost
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})