from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Talaba


# TODO: modelni import qiling
# from .models import Talaba


class TalabaList(ListView):
    """
    2.1-band: TODO
        model = Talaba
        template_name = 'talabalar/royxat.html'
        context_object_name = 'talabalar'
    """
    model = Talaba
    template_name = 'talabalar/royxat.html'
    context_object_name = 'talabalar'
    paginate_by = 5


class TalabaCreate(LoginRequiredMixin, CreateView):
    """
    2.2-band va 2.5-band: TODO
        model = Talaba
        fields = [...]                  (ism, familiya, guruh, yosh, faol)
        template_name = 'talabalar/talaba_form.html'
        success_url = ...                (yoki modelga get_absolute_url() qo'shing)

    DIQQAT: LoginRequiredMixin doim CHAPDA, asosiy View (CreateView)
    O'NGDA yoziladi — bu yerda allaqachon to'g'ri tartibda turibdi,
    shu tartibni saqlang.
    """
    model = Talaba
    fields = ['ism','familiya','guruh','yosh','faol']
    template_name = 'talabalar/talaba_form.html'
    success_url = reverse_lazy('royxat')


class TalabaUpdate(LoginRequiredMixin, UpdateView):
    """
    2.3-band va 2.5-band: TODO
        model = Talaba
        fields = [...]                  (TalabaCreate bilan bir xil bo'lishi mumkin)
        template_name = 'talabalar/talaba_form.html'   (Create bilan BITTA shablon!)
        success_url = ...

    Django <int:pk> orqali qaysi talabani tahrirlashni avtomatik topadi —
    urls.py'da to'g'ri path yozilganiga ishonch hosil qiling.
    """
    model = Talaba
    fields = ['ism','familiya','guruh','yosh','faol']
    template_name = 'talabalar/talaba_form.html'
    success_url = reverse_lazy('royxat')


class TalabaDelete(LoginRequiredMixin, DeleteView):
    """
    2.4-band va 2.5-band: TODO
        model = Talaba
        template_name = 'talabalar/talaba_confirm_delete.html'
        success_url = reverse_lazy('royxat')
    """
    model = Talaba
    template_name = 'talabalar/talaba_confirm_delete.html'
    success_url = reverse_lazy('royxat')


# ======================================================================
# MISOL — to'liq CRUD, "Kitob" modeli asosida (faqat tushunish uchun,
# ko'chirmang). Mixin tartibiga e'tibor bering: LoginRequiredMixin doim
# CHAPDA turadi.
# ======================================================================
#
# class KitobList(ListView):
#     model = Kitob
#     template_name = 'talabalar/kitob_royxat.html'
#     context_object_name = 'kitoblar'
#
#
# class KitobCreate(LoginRequiredMixin, CreateView):
#     model = Kitob
#     fields = ['nomi', 'muallif', 'narx', 'mavjud']
#     template_name = 'talabalar/kitob_form.html'
#     success_url = reverse_lazy('kitob_royxat')
#
#
# class KitobUpdate(LoginRequiredMixin, UpdateView):
#     model = Kitob
#     fields = ['nomi', 'muallif', 'narx', 'mavjud']
#     template_name = 'talabalar/kitob_form.html'  # Create bilan bir xil shablon
#     success_url = reverse_lazy('kitob_royxat')
#
#
# class KitobDelete(LoginRequiredMixin, DeleteView):
#     model = Kitob
#     template_name = 'talabalar/kitob_confirm_delete.html'
#     success_url = reverse_lazy('kitob_royxat')