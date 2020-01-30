print "My first python program in many days!!"
str = "Hello World!!"
print "Input Sring : " +str
print "Using Simple slice Method"
print str[::-1]

print "Using For loop Method"
revStr = "";
for loopVar in str:
    revStr = loopVar + revStr;
print revStr

print "Using List method"
revList = list(str)
revList.reverse();
print ''.join(revList);
