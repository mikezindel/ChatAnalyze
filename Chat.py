#Python script to parse through text file
date = 0
file = open('WhatsApp Chat.txt', 'r',  encoding="utf8") 
thisdic = {}

for line in file:
	#parce out date
	part = line.partition(',')
	datenew = part[0]
	if datenew != date:
		date = datenew
		#parce out part of the name from date
		name = part[2]
		name = name.partition('-')
		#parce out name and message
		name = name[2]
		name = name.partition(':')
		name = name[0].strip(" ")
		#name and add counter value
		if name in thisdic.keys():
			thisdic[name] += 1
		else:
			thisdic[name] = 1

print(thisdic)
