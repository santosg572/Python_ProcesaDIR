import subprocess
import sys

#print "test1"
#print sys.argv[0]
#print sys.argv[1]
#print len(sys.argv)

file = sys.argv[1]  

#res = subprocess.run(["ls", "-1", "../"])

process = subprocess.Popen(["bash", "esDirectorio.sh", file], stdout=subprocess.PIPE, 
stderr=subprocess.PIPE, 
text=True)

result = process.communicate()

print(result)
np1 = len(result)
print(np1)

for pal in result:
 print(pal)



