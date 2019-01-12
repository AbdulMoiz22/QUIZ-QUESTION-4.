def cups():
    cups= int(input('How many cups do you want?'))
    cost = cups*25
    print('Your bill is : ',cost)
    amount = int(input('What note do you have?'))

    if amount < cost:
        left = abs(cost-amount)
        print('You have to give more :',left , '(RS)')
        left_paid = int(input('You are asked to pay the left amount'))
        amount = amount + left_paid

        
        
    if amount == cost:
        print ('you have given me total amount and your change is zero,Thankyou')
    if amount > cost:
        diff1 = amount - cost

    total = 0


    print('Your change is: ')

    if diff1 >= 5000:
        fth= diff1//5000
        diff1 =diff1%5000
        tot = fth*5000
        total = total + tot
        print (str(fth) ,'* 5000' ,' = ',str(tot))
    if diff1 >= 1000:
        fth= diff1//1000
        diff1 =diff1%1000
        tot = fth*1000
        total = total + tot
        print (str(fth) ,'* 1000' ,' = ',str(tot))
    if diff1 >= 500:
        fth= diff1//500
        diff1 =diff1%500
        tot = fth*500
        total = total + tot
        print (str(fth) ,'* 500' ,' = ',str(tot))
    if diff1 >= 100:
        fth= diff1//100
        diff1 =diff1%100
        tot = fth*100
        total = total + tot
        print (str(fth) ,'* 100' ,' = ',str(tot))
    if diff1 >= 50:
        fth= diff1//50
        diff1 =diff1%50
        tot = fth*50
        total = total + tot
        print (str(fth) ,'* 50' ,' = ',str(tot))
    if diff1 >= 20:
        fth= diff1//20
        diff1 =diff1%20
        tot = fth*20
        total = total + tot
        print (str(fth) ,'* 20' ,' = ',str(tot))
    if diff1 >= 10:
        fth= diff1//10
        diff1 =diff1%10
        tot = fth*10
        total = total + tot
        print (str(fth) ,'* 10' ,' = ',str(tot))
    if diff1 >= 5:
        fth= diff1//5
        diff1 =diff1%5
        tot = fth*5
        total = total + tot
        print (str(fth) ,'* 5' ,' = ',str(tot))
    if diff1 >= 2:
        fth= diff1//2
        diff1 =diff1%2
        tot = fth*2
        total = total + tot
        print (str(fth) ,'* 2' ,' = ',str(tot))
    if diff1 >= 1:
        fth= diff1//1
        diff1 =diff1%1
        tot = fth*1
        total = total + tot
        print (str(fth) ,'* 1' ,' = ',str(tot))
    print ('------------YOUR TOTAL AMOUNT -------------: \n' , amount)
    print('-------------CASH RETURNED -----------------: \n' ,str(total))
    
cups()



















                  
    
