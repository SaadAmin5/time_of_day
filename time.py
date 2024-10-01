#Time of the day

while True:

    time=input("Enter time of the day between 0 - 24 or press 'N'to exit: ")
    
    if time == 'N':
        break
        
    try:
    
        time=int(time) 


        if time >=0 and time <=24:


            if time>4 and time <12:
                print('good morning')

            elif time>=12 and time <=17:
                print('good afternoon')

            elif time >17 and time <=21:
                print('good evening')

            else:
                print('good night')

        else:
            print('Enter time between 0 - 24')
    
    except ValueError:
        print('Enter number')
