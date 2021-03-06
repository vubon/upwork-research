from django.db import models


# Create your models here.
class Loans(models.Model):
    current_balance = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='Current Balance')
    original_balance = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='Original Balance')
    interest_rate = models.FloatField(verbose_name='Interest Rate')

    def __str__(self):
        return str(self.current_balance)

    def test(self):
        return self.current_balance
    test.short_description = u'your description'

    @classmethod
    def get_numerical_fields(cls):
        numerical_fields = []

        fields = cls._meta.fields

        for f in fields:
            type_name = f.get_internal_type()
            if type_name == 'FloatField' or type_name == 'DecimalField':
                t = tuple(f.verbose_name)
                numerical_fields.append(t)

        return numerical_fields


class TestLoans(models.Model):
    STATUS = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
    )
    choose = models.CharField(max_length=5, choices=STATUS)
    test_decimal = models.DecimalField(max_digits=14, decimal_places=4, null=True, blank=True)
    test2 = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BookManager(models.Manager):

    def create_book(self, data):
        num = self.filter(author=1).count()
        self.create(
            author_id=1,
            name=data['name'],
            book_counter=num + 1
        )
        message = {"message": "created"}
        status = 201
        return message, status

    # def delete_method(self, pk):
    #     self.filter(pk=pk).delete()
    #     self.update()


class Book(models.Model):
    author = models.ForeignKey(Author)
    name = models.CharField(max_length=100)
    book_counter = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BookManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


