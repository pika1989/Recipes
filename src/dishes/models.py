from mongoengine import Document, fields

# Create your models here.
class Dish(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField(max_length=300)
    ingredients = fields.ListField()
    time = fields.IntField()
    recipe = fields.StringField()

    meta = {'collection': 'dishes'}

    def __str__(self):
        return self.name
        
#    class Meta:
#        db_table = "dishes"
#        verbose_name_plural = "dishes"
