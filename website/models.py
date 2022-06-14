from django.db import models
from django.utils.html import mark_safe
from import_export import resources


class Yonal(models.Model):
    title = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.title
class Talaba(models.Model):
    familiya=models.CharField(max_length=255)
    ism=models.CharField(max_length=255)
    ota_ism=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    talim=models.CharField(max_length=255)
    yonal=models.ForeignKey(Yonal,on_delete=models.CASCADE)
    diplom=models.CharField(max_length=255,unique=True)
    pasport=models.CharField(max_length=255,unique=True)
    pasport_image=models.ImageField(upload_to="pas_img/%Y/%m/%d")
    diplom_image=models.ImageField(upload_to="dip_img/%Y/%m/%d")
    image_3x4=models.ImageField(upload_to="img_3x4/%Y/%m/%d")
    added_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism


    def pasport_image_tag(self):
        return mark_safe(f'<img src="/media/{self.pasport_image}" width="150" height="150" /><br><a href="/media/{self.pasport_image}" style="atext-align-last: justify;">/media/{self.pasport_image}</a>')
    pasport_image_tag.short_description = 'pasport image'
    def diplom_image_tag(self):
        return mark_safe(f'<img src="/media/{self.diplom_image}" width="150" height="150" /><br><a href="/media/{self.diplom_image}">/media/{self.diplom_image}</a>')
    diplom_image_tag.short_description = 'diplom image'
    def image_3x4_tag(self):
        return mark_safe(f'<img src="/media/{self.image_3x4}" width="150" height="150" /><br><a href="/media/{self.image_3x4}">/media/{self.image_3x4}</a>')
    image_3x4_tag.short_description = 'image 3x4'
