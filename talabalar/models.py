from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    guruh = models.CharField(max_length=50)
    yosh = models.PositiveIntegerField()
    faol = models.BooleanField(default=True)

    """
    TODO (1-band): Quyidagi maydonlarni vazifa hujjatidagi jadvalga
    qarab qo'shing:

        ism       -> CharField(max_length=100)
        familiya  -> CharField(max_length=100)
        guruh     -> CharField(max_length=50)
        yosh      -> PositiveIntegerField()
        faol      -> BooleanField(default=True)

    Pastdagi "Kitob" misoliga qarang — usul bir xil, faqat
    maydon nomlari va modeli boshqa. O'zingiz moslashtiring.

    Eslatma: get_absolute_url() qo'shish bonus topshiriq (4-band) —
    agar uni qo'shsangiz, CreateView/UpdateView'da success_url
    yozmasangiz ham bo'ladi.
    """

    # --- shu yerga maydonlarni yozing ---
    

    def __str__(self):
        # TODO: ism va familiyani birga qaytaring,
        # masalan: return f'{self.ism} {self.familiya}'
        return f'{self.ism}'

def get_absolute_url(self):
    from django.urls import reverse
    return reverse('royxat')

    # Bonus (ixtiyoriy):
    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('royxat')


# ======================================================================
# MISOL — faqat tushunish uchun (vazifaning bir qismi emas, ko'chirmang)
#
# Bu "Kitob" modeli — hujjatdagi "Mashina" namunasidan ham, sizning
# "Talaba" vazifangizdan ham boshqa, uchinchi bir misol.
# ======================================================================
#
# class Kitob(models.Model):
#     nomi = models.CharField(max_length=150)
#     muallif = models.CharField(max_length=100)
#     narx = models.DecimalField(max_digits=10, decimal_places=2)
#     mavjud = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.nomi
