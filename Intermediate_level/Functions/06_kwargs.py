#**kwargs in function 


#a function that accepts any number of student details using **kwargs and prints them

def student_info(**kwargs):        #defined **kwargs in the function
    for key, value in kwargs.items():     #iteration throgh the KV pairs
        print(key, ":", value) 

student_info(name="Pawan", age=22, course="Python")   #reaccling the key with specified values