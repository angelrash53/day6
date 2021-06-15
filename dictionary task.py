#Given a list of dictionaries containing data such as Productname, 
# exclusiveprice passed to a function as a parameter, to get her with the taxrate
#calculate the inclusive price of each products, then return a list of dictionaries containing the product and 
#their respective incl prices.

def calculatevat(products, taxrate):
    inclusiveprice = {}
    for price in products:
        vattax = price["exclusiveprice"] * taxrate
        inclusiveprice = price["exclusiveprice"] + vattax
        
        return inclusiveprice
        print(products["productname"] + "" + str(inclusiveprice))

products = [
    {
        "productname": "Milk",
        "exclusiveprice": 40
    },
    {
        "productname": "Bread",
        "exclusiveprice": 50
    }
]

print(calculatevat(products, 0.16))
