import random
import json
import fileinput
import discord


async def stocks_job(bot):
    channel = await bot.fetch_channel(1116342952113999923)

    message = channel.fetch_message(1116375965807935538)

    file = fileinput.input(files="./stocks/weekly.txt")

    weekly_base = float(file.readline())

    file.close()

    embed = discord.Embed(
        title="Stock information",
        description= "The updated market prices of all stocks",
        color=discord.Colour.blurple()
    )

    with open("./stocks/stocks.json") as json_file:
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

            embed.add_field(name= stock["name"], value="Market price: " + str(stock["price"]), inline=False)

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

    await message.message.edit_original_response(embed=embed)

