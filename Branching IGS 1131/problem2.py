# Question explanation : 
#     Tax rate is based on the total income.
#     if the income is less than 50000, the tax would be 5 % of the income. e.g if you earn $100, then tax is $5.
#     if the total income is 80000 >> 50000(tax 5% =2500 ) + 30000 (tax 10% =3000), cumulative tax = 2500 + 3000 = 5500
#     if the total income is 300000 >> 50000(tax 5% = 2500) +  150000(tax 10% = 15000) + 100000(tax 15% = 15000), cumulative tax = 32500



income = int(input("Income : "))   # use float if the given numbers are decimals

# first 50000
if (income  < 50000):
    total_tax = (income * 5/100) # 5% 
    
elif (50000 <= income <= 150000):
    first_tax = (50000 * 5/100) # 5% for first 50000
    
    remaining_income = income - 50000  
    second_tax = (remaining_income * 10/100)  # 10% for the remaining money
    total_tax =first_tax + second_tax
else: 
    first_tax = (50000 * 5/100) # 5% for first 50000
    second_tax = (150000* 10/100) # 10% for 50000~ 150000
    remaining_income = income - (50000 + 150000)
    third_tax = (remaining_income * 15/100)
    total_tax = first_tax + second_tax + third_tax
    
print("Cumulative tax ", total_tax)
    
    
