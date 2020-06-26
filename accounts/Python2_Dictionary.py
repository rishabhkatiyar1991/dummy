# dictionary is nothing but key value
d1 = {}
#print(type(d1))
d2 = {"Rahul":"Roti", "harry":"Burger","shubham":"Egg","rohit":{"A": "chicken", "B":"banana"}}
#print(d2["Rahul"])
#print(d2["rohit"]["A"])
#d2["Ankit"] = "junk food"
#del d2["Rahul"]
#d2.update({"Rishi":"veg"})
#d2.clear()
#d3 = d2.keys()    OR
#print(d2.keys())        # ex. dict_keys(['Rahul', 'harry', 'shubham', 'rohit'])
#print(d2.items())       # ex. dict_items([('Rahul', 'Roti'), ('harry', 'Burger'), ('shubham', 'Egg'), ('rohit', {'A': 'chicken', 'B': 'banana'})])
#print(d2.values())      # ex. dict_values(['Roti', 'Burger', 'Egg', {'A': 'chicken', 'B': 'banana'}])
#print(d2.get("harry"))     #Returns the value of the specified key
#print(dict.fromkeys(d2))   #The fromkeys() method returns a dictionary with the specified keys and values. In this condition key value should None
#print(d2.pop("shubham"))    #The pop() method removes the specified item from the dictionary.
#print(d2.popitem())      #Remove the last item from the dictionary / The popitem() method removes the item that was last inserted into the dictionary
dict_name = input("Please enter Name ")
#name = dict_name.capitalize()
#print(d2[name])
print(d2[dict_name])