"""A Python dictionary is a collection of items that allows us to store data in key: value pairs."""


car = {
    "model": "BMW",
    "year" : 2025,
    "speed" : "2000ms"
}

mobile = {
    'model': 'Apple',
    'price': '3000',
    'product':"USA"
}

country = {
    'kh' : 'Phnom Penh',
    'us' : "Washintone DC",
    'en' : "New York"
}

print(car) # print all data in car dictionary
print(car["model"]) # access to value of car key
print(mobile['price'])

# use .get() method to retieve data
print(car.get('model'))
print(country.get('kh'))

country['th'] = "Bangkok" # add new key to dictionary

print(country) #{'kh': 'Phnom Penh', 'us': 'Washintone DC', 'en': 'New York', 'th': 'Bangkok'}

# delete key from dictionary

del country['us']
print(country) #{'kh': 'Phnom Penh', 'en': 'New York', 'th': 'Bangkok'}

print(country.pop('en')) # print value of key that has been remove
print(country)

country.clear() # clear all data from country variable
print(country) # {} 

# change the value of "price" key to "Something"
print(mobile) #{'model': 'Apple', 'price': '3000', 'product': 'USA'}
mobile['price'] = "Something" 
print(mobile) #{'model': 'Apple', 'price': 'Something', 'product': 'USA'}



# Iterate Through a Dictionary
subject = {
    'kh' : "Khmer Letureture",
    'en' : "English",
    'ma' : "Mathimatic",
    'bo' : "Bography"
}

for sub in subject:
    print(subject[sub]) #display value
    print(sub) # display key

# check length of dictionary length
print(len(subject))


"""
Function	Description
pop()	    Removes the item with the specified key.
update()	Adds or changes dictionary items.
clear()	    Remove all the items from the dictionary.
keys()	    Returns all the dictionary's keys.
values()	Returns all the dictionary's values.
get()	    Returns the value of the specified key.
popitem()	Returns the last inserted key and value as a tuple.
copy()	    Returns a copy of the dictionary.

"""