import re 

with open('src/output.txt') as f:
    payload = f.read()
    print(payload)
    
splitted = payload.split(',')
for i, single in enumerate(splitted):
    result = re.search('"(.*)"', single)
    print(result.group(1))
    splitted[i]=result.group(1)
    
print(splitted[0])