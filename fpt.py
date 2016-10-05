def even(a):
	return a%2==0

print filter(even,(3,5,6,8,10))  

print filter(lambda name: name.startswith('p'), ['hari','prakash','atm']) #filter used only for filter operation in group of elements


print 2**3
print map(lambda x: x%3==0,(1,2,3,4,5)) #map is used for manipulation of each element in group of elements

 