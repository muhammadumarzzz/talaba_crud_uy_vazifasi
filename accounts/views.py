# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RoyxatForm

 
def royxatdan_otish(request):
    if request.method == 'POST':
        form = RoyxatForm(request.POST)
        if form.is_valid():
            user = form.save()           # foydalanuvchini saqlaydi
            login(request, user)         # darhol tizimga kiritadi
            return redirect('royxat')    # ro'yxatga yo'naltiradi
    else:
        form = RoyxatForm()
    return render(request, 'registration/royxat.html', {'form': form})
