from isbnlib import meta,desc,cover
from isbnlib.registry import bibformatters
import csv
import urllib.request


SERVICE = 'default'

# now you can use the service
# isbn = input('isbn')
isbn = '9781408855652'
print((meta(isbn, SERVICE)))
# my_dict = (meta(isbn,SERVICE))

print(desc(isbn))
print(cover(isbn))
# if (desc(isbn)) is None:
# 	print('desc not available')
# else:
# 	my_dict['desc'] = (desc(isbn))

# my_dict['covers'] = (cover(isbn))
# if my_dict['covers']['thumbnail'] == 'None':
# 	my_dict['covers']['thumbnail'] = 'not valid'
# print(link_url)
# data = urllib.request.urlretrieve(link_url,'test.jpg')
# print(data)
# for k,v in my_dict.items():
	# print('{0}:{1}\n'.format(k,v))

# print(dict1['Title']) 
# for k, v in dict1.items():
# 	print('key: ',k)
# 	print('value: ',v)
# print(my_dict)
# with open('my_file.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in my_dict.items()]