is_going = input("is there other people to pass it on?")
while is_going == "yes":

    logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
    '''
    price = ""
    name = ""
    print(logo)
    name = input("whats your name")
    price = input("whats your price")
    print(f"ok so your name is {name} and your price is {price} thanks")
    person_info = {name: price}
    is_going = input("is there other people to pass it on?")
    print("\n" * 200)
    if is_going == "no":
        print(f"the person whom had the hiest bid is {name} with {price}$")
















































































































