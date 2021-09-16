spam  = 45 #Global variable

def eggs():
    global spam #change global scope from within local function scope
    spam = 34

eggs()
print (spam)