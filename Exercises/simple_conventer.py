cm = float(input("Type the cm you want to convert into meters or inches: "))

metr  = cm/100
inch = cm/0.394
print("Your value {} cm converted to metres is {} and to inches {:.3f}".format(cm,metr, inch))

print("Your value %d cm converted to metres is %d and to inches %.3f" % (cm,metr, inch))


kg = float(input("Type the numbers kg to be converted into punds: "))

kg_to_pounds = kg * 2.4419
kg_to_grams = kg * 1000
print("Your value {}kg is equal to {:.4f} pounds and {} grams".format(kg, kg_to_pounds, kg_to_grams))
