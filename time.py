#Time of the day

while True:

    time=input("Enter time of the day between 0 - 24 or press 'N'to exit: ")
    
    if time == 'N':
        break
        
    try:
    
        time=int(time) 


        if time >=0 and time <=24:


            if time>=12 and time <=16:
                print('good afternoon')

            elif time >=16 and time <=18:
                print('good evening')

            elif time >=18 and time <=24:
                print('good night')

            else:
                print('good morning')

        else:
            print('Enter time between 0 - 24')
    
    except ValueError:
        print('Enter number')