import math as m

user_input = input('Input a number >> ')

# Check for fraction input
if "/" in user_input:
    temp = user_input.split('/')
    # print(len(temp))
    if len(temp) == 2:
        real_input = float(temp[0])/float(temp[1])
# For normal decimal inputs
else: real_input = float(user_input)

result = m.gamma(real_input)
print('The Gamma function of ', user_input, ' is equal to: ', result)