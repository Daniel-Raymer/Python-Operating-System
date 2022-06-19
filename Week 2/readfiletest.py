#f = open("spider.txt")

#content = f.read()
#print(content)
#f.close()

with open("spider.txt") as f:
    print(f.read())