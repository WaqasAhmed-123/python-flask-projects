f = open("data.txt", "r")
print(f.read())
print("--------------")

f = open("data.txt", "r")

print(f.readline())
for x in f:
  print(x)

f.close()


f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#removing file
import os

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#removing folder
os.rmdir("test")