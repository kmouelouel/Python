from string import Template
def main():
    cart=[]
    cart.append(dict(item="coke", price=30, qty=2))
    cart.append(dict(item="cake", price=100, qty=5))
    cart.append(dict(item="fish", price=42, qty=1))
    t=Template('$qty * $item=$price')
    total=0
    print("Cart:")
    for data in cart :
        print(t.substitute(data))
        total=total+data['price']
    print("Total: "+ str(total));
main();
