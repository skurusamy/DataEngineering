import re
dic = {}
file = open("log.txt","r")
for line in file:
	#print(line)
	result = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',line)
	if result[0] not in dic:
		dic[result[0]] = 1
	else:
		dic[result[0]] += 1
print(sorted(dic.items(), key= lambda x:x[1],reverse = True))
