import random
import json
import fileinput


async def stobk_jobs():
    file = fileinput.input(files="stocks/stocks.txt")

    weekly_base = int(file.readline())

    with open("stock/stock.json") as json_file:
        data = json.load(json_file)

        stocks = data["stocks"]

        for stock in stocks:
            random.seed(random.randint(0, 10000000000000))

            hourly_base = random.randint(-1000, 1000) / 1000

            stock["price"] = stock["price"] + (
                stock["price"] / 100 * (weekly_base + hourly_base)
            )

            if int(stock["price"]) < 1:
                stock["price"] = 1


    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
