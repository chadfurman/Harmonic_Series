
target = int(input("Enter a whole number: "))

runningsum = 0 
counter = 0

while runningsum <= target:

    counter = counter + 1 #by putting this first, counter isn't 0 anymore, plus we're not sure where the loop exits
    reciprocal = 1/(counter)
    runningsum = runningsum + reciprocal 
    
    
print('You need to add %g reciprocals up to 1/%g to reach the whole number %g.' %(counter,counter,target))
