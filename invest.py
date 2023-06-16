# amount, rate, time
# origin amount: 100
# year 1: $105.0
# year 2: $110.25
# amount + (amount * rate)
# (1 + amount ) * rate * time
# P(1+i)^n

amount = float(input('please enter origin amount:\n'))
# print(type(amount))
rate = 0.05
time = 10
# print(amount*(1 + rate)^10);
def invest(amount, rate, time):
   for i in range(1, time):
      print(f'years {i}: ${amount*(1 + rate)**i}') 

invest(amount, rate, time)

