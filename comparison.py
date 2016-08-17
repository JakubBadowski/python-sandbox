# Python

"""
Komentarze blokowe 
"""

def ageTest() :

	name = "Kuba"
	sName = "Badowski"
	age = 19

	if age > 20 :
		print "Jestes starym koniem"
	else :
		print "jestes mlodym leszczem"


def whoami(name = None, age = None):
	print "----" + str(name) + "--------" + str(age)

def bLoop() :
	for i in range(10) :
		print i


def bLoobDic(dic) :
	for key in dic :
		print dic[key]

def bList():
	# Listy
	L = [1, 2, 3, 4]
	L[1] = 100
	print L[-1]

def bDictionary() :
	# Slowniki
	D = {
		"name": "Kuba",
		"sName": "Badowski",
		"age": 30
	}

	print D["name"]




D = {
	"name": "Kuba",
	"sName": "Badowski",
	"age": 30
}

bLoobDic(D)
# whoami(age = 12);
# ageTest()
# bLoop()

# Listy - List
# bList();

# Slowniki - Dictionary
# bDictionary()

# Klasy
class Animal:

	name = "Pies"

	def Wof() :
		print "Wof Wof"


# name = "AlPaczino"

# print name[3:]
# print (name + " " + sName)