#1.Return all customer from customer table
customers=Customer.objects.all()

#2.Return 1st customer in table
firstcustomer=Customer.objects.first()

#3.Return last customr in table
lastcustomer=Customer.objects.last()

#4.Return single customer by name
customerbyname=Customer.objects.get(name="Asad Bhau")

#5.Return single customer by name
customerbyid=Customer.objects.get(id=4)

#6Return all orders related to customer (firstcustomer variable set above)
firstCustomer.order_set.all()

#7.Returns orsders customers name:(Query parent model values)
order=Order.objects.first()
parentName=order.customer.name

#8Return products froms products table with value of Outdoor in category attribute
products=Products.objects.filter(category="Outdoor")

#9.Order/Sort aobjects by id
leasttogreatest=Product.objects.all().order_by('id')
greatesttoleast=Product.objects.all().order_by('-id')

#10 Returns all prodcuts with tag of sports:(Query many to many field)
productsFiltered=Product.objects.filter(tags_name="Sports")

#11 If customer has more than one ball how should reflect in the database?
#return total counts of number of time a ball
allorders={}
for order in firstcustomer.order_set.all():
    if order.products.name in allorders:
        allorders[order.products.name]+=1
    else:
        allorders[order.products.name]=1

#related set example
class Parentmodel(models.Model):
    name=models.Charfield(max_length=200,null=True)

class Childmodel(models.Model):
    parent=models.ForeignKey(Parentmodel)
    name=models.Charfield(max_length=200,null=True)

parent=Parentmodel.objects.first()
parent.Childmodel_set.all()