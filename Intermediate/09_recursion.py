# recursive function

#ex. a recursive function that prints numbers from 5 to 1

def countdown(n):   #defined the function with 'n' as var
    if n == 0:    #set a for loop for iterative recurision
        return

    print(n)
    countdown(n - 1) #set a condtion for going form 5 to 1

countdown(5)  #recalling function with argumetent