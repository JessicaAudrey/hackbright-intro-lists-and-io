#JessicaFood = my_file.readlines()
#print JessicaFood
#my_file.close()

#my_file2 = open("Alexis_fav_foods.txt")
#AlexisFood = my_file2.readlines()
#print AlexisFood
#my_file2.close()

def read_file(filename):
	my_file = open(filename)
	faves = my_file.readlines()
	my_file.close()
	return faves


jessica_food = read_file("jessica_fav_foods.txt")
print jessica_food

alexis_food = read_file("Alexis_fav_foods.txt")
print alexis_food


def compare_favs(var1,var2):
	if(var1[0] == var2[0]):
		print "Our favorite foods are the same"
	else:
		print "Our favorite foods are different"

compare_favs(jessica_food,alexis_food)

def compare_favs2(var1,var2):
	if(var1[0] == var2[0]):
		print "We both love " + var1[0]
	elif(var1[1] == var2[1]):
		print "we both love " + var1[1]
	elif(var1[2] == var2[2]):
		print "we both love " + var1[2]
	else:
		print "We like different foods"

compare_favs2(jessica_food,alexis_food)

