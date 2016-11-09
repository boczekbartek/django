from orders.models import Sauce

sosy = ['ostry', 'lagodny', 'vinegret']

for i in sosy:
	a = Sauce()
	a.name = i
	a.price = 2.00
 	a.image = '#'

