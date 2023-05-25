import asyncio
from pyppeteer import launch

def load_html(level, experience, percent):
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title><style>@import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@500&display=swap");#myProgress {'+'width:'+'100%; background-color: #010102;}#myBar {width: '+ str(percent) +'%; height: 30px;background-color: green;}</style></head><body style="background-color: #282a35;"><h1 style="font-family: Roboto Mono, monospace;">Rank Card</h1><div style="display:inline-flex"><div style="margin-right: 100px;"><p style="font-family: Roboto Mono, monospace;">Level</p><p style="font-family: Roboto Mono, monospace;">'+ str(level) +'</p></div><div><p style="font-family: Roboto Mono, monospace;">Experience</p><p style="font-family: Roboto Mono, monospace;">'+ str(experience) +'</p></div></div><div id="myProgress"><div id="myBar"></div></div><script>var i = 0;function move() {if (i == 0) {i = 1;var elem = document.getElementById("myBar");var width = 1;var id = setInterval(frame, 10);function frame() {if (width >= 100) {clearInterval(id);i = 0;} else {width++;elem.style.width = width + "%";}'+'}'+'}'+'}</script></body></html>'
    f = open("tmp.html", "w")
    f.write(html)
    f.close()

async def convert_html_to_png(level, exp, percent_to_next_lvl):

    load_html(level, exp, percent_to_next_lvl)
    print("load")

    # Launch headless Chrome browser
    browser = await launch(executablePath='/usr/bin/chromium-browser', args=['--no-sandbox'])
    print("Launch")

    # Create a new page
    page = await browser.newPage()
    print("newPage")

    # Set the viewport size (optional)
    await page.setViewport({'width': 500, 'height': 215})
    print("viewport")

    # Navigate to your HTML file
    await page.goto('root/Tischler/tmp.html')
    print("goto")

    # Wait for any additional content to load (optional)
    await asyncio.sleep(0.5)
    print("sleep")

    # Take a screenshot of the page
    await page.screenshot({'path': 'output.png'})
    print("screenshot")

    # Close the browser
    await browser.close()
    print("close")

asyncio.get_event_loop().run_until_complete(convert_html_to_png(12, 12000, 25))