import random

with open('stocks/weekly.txt', 'w') as file:

    random.seed(random.randint(0,10000000000000))

    weekly_base = random.randint(-1000,1000) / 1000

    file.write(str(weekly_base))