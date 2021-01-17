#Python script to parse through text file

file = open('WhatsApp Chat.txt', 'r') 
thisdic = {}

for line in file:
	part = line.partition(',')
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
