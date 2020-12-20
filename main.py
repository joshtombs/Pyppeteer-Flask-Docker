# main.py

# Imports for web server
import os
from flask import Flask

# Imports for web scraping
from requests_html import AsyncHTMLSession
import asyncio
import pyppeteer

app = Flask(__name__)

async def get_page(url):
    new_loop=asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    session = AsyncHTMLSession()
    print("Launching browser...")
    browser = await pyppeteer.launch({ 
        # 'executablePath': 'google-chrome-stable',
        'executablePath': 'google-chrome-unstable',
        'ignoreHTTPSErrors':True,
        'dumpio':True,
        'headless':True, 
        'handleSIGINT':False, 
        'handleSIGTERM':False, 
        'handleSIGHUP':False
    })
    print("Launched browser...")
    session._browser = browser
    resp_page = await session.get(url)
    print("Got response from page...")
    await resp_page.html.arender()
    print("Rendered page...")
    return resp_page.html # note, changed from content

@app.route("/test/<path:url>")
def get_page_name(url):
    print("Got request to collect ", url)
    try:
        page_html = asyncio.run(get_page(url))
    except:
        return "Error retrieving match content from URL"

    return page_html.find('title')[0].text

@app.route("/")
def get_toscrape_name():
    return get_page_name("http://toscrape.com")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
