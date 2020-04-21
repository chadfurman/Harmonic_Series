#Given a whole number, this program tells how many consecutive reciprocals must be summed to reach that whole number.
#For example, to reach the number 2, the reciprocals 1/1 + 1/2 + 1/3 + 1/4 must be summed. 
#It would say, "You need to add 4 reciprocals up to 1/4 to reach the whole number 2."
#My code might run out of control, so don't enter a number higher than 3

from IPython.display import display,Math

#Defining functions


def iterationloop():
    
    summ = 0 + iteration_horse #recursive clusterfuck part A
    iteration_horse = summ + recip #recursive clusterfuck part B

    runningcount = pool_recip #position in range of pool_recip
    
    for pool_recip in range(1,10000000): #I'm sure there must be a way to say "range of all positive integers" or maybe just say... for x:
        #Anyway, range should be big but I restricted it to 100 in case my code ran out of control.
        
        recip = 1/pool_recip
        
        while iteration_horse <= target: #This loop runs until the target number is reached. 
          if iteration_horse <= pool_compare:
              recip
              iteration_horse #those two lines should probably be replaced with a function or something
          elif iteration_horse >= pool_compare:
              base = runningcount #this updates the value of base, which is used in the function finalanswer
              continue
          #I'm not clear on how to express that when the while statement is done, it runs finalanswer
          #Does the loop just automatically exit as soon as while condition is exhausted, and then execute the next line of code?
          #I actually don't have to put finalanswer inside iterationloop at all, do I
          #This part is just done?
    
def finalanswer(): 
    
    print('You need to add %g reciprocals up to \\frac{1}{%g} to reach the whole number %g.' %(runningcount,runningcount,target))
    
         
#Defining variables and making it run 

target = int(input('Enter a positive whole number !!Enter 3 while code is under construction: '))
pool_compare = range(1,target) #Should that go inside the function iterationloop?

iterationloop()
finalanswer()



