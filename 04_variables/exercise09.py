# Repeat the previous question but, this time, use augmented 
# assignment to compute the final result, one year at a time.

amount = 1000
years = 5
amount *= 1.05**years

print(f'After {years} years, the balance is ${amount:,.2f}.')
