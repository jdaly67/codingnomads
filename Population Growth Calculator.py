#Population Growth Calculator
#Write the necessary code to display the total population count for the next 3 years (without a leap year).

#Here are the specifications:

#In the country we want to investigate:

#The current population is 380,123,456
#One person is born every 6 seconds
#One person dies every 12 seconds
#One person immigrates every 40 seconds
cur_pop = 380123456
year = 1
while year < 4:
    new_pop = cur_pop + ((60*24*365)/6) - ((60*24*365)/12) + ((60*24*365)/6)
    print("Year ", year,"population is:", new_pop)
    cur_pop = new_pop
    year += 1
    