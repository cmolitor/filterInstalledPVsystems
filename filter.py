import numpy as np 

data = np.genfromtxt("200901-201612.csv", delimiter=';', dtype=None)
plz = np.genfromtxt("PLZ_tmpl.txt", dtype="S5").tolist()

# print(plz)

counter = 0

for _data in data:
	if _data[1] in plz:
		counter = counter + 1
		# print(_data)

print "Number of PV systems: ", counter