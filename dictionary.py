#given a list of dictionaries containing data such as product name, exclusive price,
#  passed to a function as a parameter, together with the taxrate, calculate the inclusive price
#  of each products.


def calculatevat(products, taxrate):
    inclprice = {}
    for product in products:
        vat = product["pprice"] * taxrate
        inclprice = product["pprice"] + vat
        print(product["pname"] + "" + str(inclprice))
    

        


products = [
   {
        "pname": "milk",
        "pprice": 120,
          
    },
    {
        "pname": "bread",
        "pprice": 90,
      
    },
    {
        "pname": "butter",
        "pprice": 250,
      
    },
    {

        "pname": "sugar",
        "pprice": 60,
  
    },
]



calculatevat(products, 0.16)
