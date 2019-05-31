import os
path="D:\\LT\\pyproj\\ht\\111"
for i in os.walk(path):
    print(i[-1])
    for n in i[-1]:
        print(n)