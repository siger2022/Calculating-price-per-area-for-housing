try:
    area = int(input("Please enter the total area of an apartment: "))
except ValueError:
    print("invalid")

unit = input("In ft or sqm? ")
the_price = float(input("Please enter the price in million: "))
currency= input("Currency: HKD, USD or EURO:?" )
area_in_sqm = (area * 0.09290304)


if unit == "ft" and currency == "$HKD":
    print(f"The area of the apartment is {area_in_sqm:.1f} square meter")
    the_price_of_the_apartment_in_euro = float(the_price) * 0.11
    print(f"The price of the apartment is {the_price_of_the_apartment_in_euro} million euros")
    the_average_price =round((the_price_of_the_apartment_in_euro*1000000)/area_in_sqm)
    print(f"{the_average_price} euros/sqm")

elif unit == "ft" and currency == "$USD":
    print(f"The area of the apartment is {area_in_sqm:.1f} square meter")
    the_price_of_the_apartment_in_euro = float(the_price) * 0.88
    print(f"The price of the apartment is {the_price_of_the_apartment_in_euro} million euros")
    the_average_price = round((the_price_of_the_apartment_in_euro * 1000000) / area_in_sqm)
    print(f"{the_average_price} euros/sqm")
else:
    print(f"The area of the apartment is {area:.1f} sqm")
    print(f"The price of the apartment is {the_price} million euros")
    the_average_price = float(the_price * 1000000 / area)
    print(f"{the_average_price:.0f} euros/sqm")

