import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        errs=[]
        for w in [320,375,414,768,900,1024,1280,1440]:
            pg = await b.new_page(viewport={'width':w,'height':900})
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto(sys.argv[1]); await pg.wait_for_timeout(300)
            r = await pg.evaluate('''()=>({sx:document.documentElement.scrollWidth-document.documentElement.clientWidth,
              slides:document.querySelectorAll('#mediaSlot .mt-slide').length,
              dots:document.querySelectorAll('#mediaSlot .mt-dots button').length,
              on:[...document.querySelectorAll('#mediaSlot .mt-slide')].findIndex(e=>e.classList.contains('on')),
              imgsOk:[...document.querySelectorAll('img')].every(i=>i.complete&&i.naturalWidth>0),
              mail:[...document.querySelectorAll('a[href^=mailto]')].map(a=>a.getAttribute('href')),
              h:Math.round(document.getElementById('mediaSlot').getBoundingClientRect().height)})''')
            print(w, r)
            if w in (375,1280):
                await pg.locator('#mediaSlot').scroll_into_view_if_needed()
                await pg.screenshot(path=f'shot_{w}_a.png')
                await pg.wait_for_timeout(5600)
                on = await pg.evaluate("[...document.querySelectorAll('#mediaSlot .mt-slide')].findIndex(e=>e.classList.contains('on'))")
                print('  after 5.6s on=',on)
                await pg.screenshot(path=f'shot_{w}_b.png')
            await pg.close()
        print('errors', errs)
        await b.close()
asyncio.run(main())
