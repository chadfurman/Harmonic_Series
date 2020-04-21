from IPython.display import display,Math

def harmonic():

    target = int(input("Enter a whole number: "))

    runningsum = 0 
    counter = 0

    while runningsum <= target:

        counter = counter + 1
        reciprocal = 1/(counter)
        runningsum = runningsum + reciprocal
    
    
    display(Math('\\text{You need to add }%g\\text{ reciprocals up to }\\frac{1}{%g}\\text{ to reach the whole number }%g.' %(counter,counter,target)))
    harmonic()   
    
harmonic()
