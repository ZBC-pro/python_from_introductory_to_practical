def make_pizaza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizaza(16,'tomato')
make_pizaza(24,'mashrooms', 'green pepers', 'extra cheese')