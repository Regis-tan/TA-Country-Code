def menu():
    option = str(input('Enter country name or country code: '))

    with open("TA Lab 6-3.txt") as text_file:
        text_file.readline()
        for row in text_file:
            data = row.strip("\n").split("|")
            country, _, code, _, _, _, _ = data
            if option == country or option == code:
                if option == country:
                    print(f"The code for the country {country} is {code}.")  
                    menu()
                else:
                    print(f"The name for the country code {code} is {country}.")
                    menu()
    print(f"Country or Country code '{option}' not found.")
    menu()

menu()


