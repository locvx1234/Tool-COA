inp = raw_input("Input : ")

tag = int(raw_input("Tag : "))
idx = int(raw_input("Index: "))
off = int(raw_input("Offset: "))
print "Tag: ", inp[:tag]
print "Index: ", inp[tag:tag+idx]
print "Offset: ", inp[tag+idx:]