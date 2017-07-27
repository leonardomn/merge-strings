## Code Merge String 

a = "ab"
b = "zsd"

mergeString = ""

for index in range(max(len(a),len(b))):
	if index+1 <= len(a):
		mergeString += a[index]
	if index+1 <= len(b):
		mergeString += b[index]
print(mergeString)