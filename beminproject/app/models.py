from django.db import models


# 주문 = 가게이름, 가게사진, 가게소개
class order(models.Model):

    image = models.ImageField()
    store = models.CharField( max_length=50) 
    intro = models.models.TextField()
    

    def __str__(self):
        return self.name

# 주문내역 = 메뉴사진, 메뉴이름, 메뉴가격
class order_list(models.Model):

    image = models.ImageField()
    menu = models.CharField( max_length=50)
    price = models.IntegerField()
    

    def __str__(self):
        return self.name