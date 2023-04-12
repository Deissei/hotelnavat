from django.db import models



class CategoryRooms(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории номеров'


class Rooms(models.Model):
    category = models.ForeignKey(CategoryRooms, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    ploshadM2 = models.CharField(max_length=8)
    sizeBed = models.CharField(max_length=9)
    priceInDay = models.IntegerField()
    roomEquipment = models.ManyToManyField('RoomEquipment')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Номера'
    

class RoomEquipment(models.Model):
    name =  models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Оснащение номера'