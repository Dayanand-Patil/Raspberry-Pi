for i in range(0, 5) :
	print "*" * (i + 1)
   # Or
for i  in range(0, 5 + 1) :
	print "#" * i   
for i in range (5, 0, -1) :
	print "*" * (i - 1)	
print "\n above pattern in one line"
print "\n".join("1" * i for i in range(0, 5+1))

print "\n Diamond pattern"
def run():
    j = 7
    k = 7
    p = 1
    for i in range(8):
        print " " * k," #" *  i
      # k -=1
    while j > 1:
        j -= 1
        print " " * p," #" * j
        p +=1
run()
print "another pattern"
k = 7
for i in range(0, 6) :
		print " " * k , "#" * i
		k -= 1

k = 7
for i in range (5, 0, -1) :
		print " " * k, "#" * (i)
print "\npyramid "
w = 20
for i in range(w):print(">"+" "*(w-i)+"."*i*2+" "*(w-i)+"<")        


		
import time
import datetime
print "what is datetime :",datetime
print "what is inside datetime module :",dir(datetime)
print "info of datetime module :",datetime.__doc__
print datetime.date
print datetime.datetime.now().minute
print datetime.datetime.now().second
print datetime.datetime.now().date
print dir(datetime.datetime.now().date)