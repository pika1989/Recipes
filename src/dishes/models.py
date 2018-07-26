from djongo import models

# Create your models here.
class Dish(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=300)
    ingredients = models.ListField()
    time = models.IntegerField()
    recipe = models.TextField()

    objects = models.DjongoManager()

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = "dishes"
        verbose_name_plural = "dishes"
