bookprice=250
discount=.30
shippingcost1=20
shippingcost2=5
totalcopies=60

bookDiscountamount=bookprice*discount*totalcopies
shipping=(shippingcost1*5)+(shippingcost2*55)
totalammount=(bookDiscountamount)+(shipping)

print("the total price for 60 copies:"+ str(totalammount))
