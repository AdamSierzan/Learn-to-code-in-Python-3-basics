
print('''Hi this program will let your 
calculate the invest rate''')

balance = float(input("Enter your current account balance: "))

rate = float(input("Enter the invest rate: "))

years = float(input("Enter the number of years: "))
months = years*12
final_balance = balance*months*rate
print(final_balance)
print("By investing {} euro, for {} years with the rate {} you will be {}".format(balance, years, rate, final_balance))