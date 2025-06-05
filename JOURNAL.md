---
title: "Slate"
author: "samliu"
description: "A sleek e-ink name badge!"
created_at: "2024-06-04"
---

# May 14th: Getting the screen to work

It was a long sitting and I got a TON done... but most of these are proof of concepts that will be later refined.

The [firmware provided by the vendor](https://github.com/WeActStudio/WeActStudio.EpaperModule) was not compatible with any of the MCU's I had. Looking at the provided documentation and datasheets, the [SSD1680 driver](https://github.com/WeActStudio/WeActStudio.EpaperModule/blob/master/Doc/SSD1680.pdf) for 176x196 tri-color epaper displays seem to work with my 128x296 display. Some further search on the web lead me to [this article](https://www.pinteric.com/displays.html#ssd), which confirms my theory.

By bodging Adafruit's [SSD1680 CircuitPython library](https://github.com/adafruit/Adafruit_CircuitPython_SSD1680) with their [eink tutorial](https://learn.adafruit.com/adafruit-2-9-eink-display-breakouts-and-featherwings/circuitpython-usage), I managed to get stuff to show, although the refresh rate is atrocious. 

I followed Adafruit's [custom font tutorial](https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display/overview) and [bitmap image tutorial](https://learn.adafruit.com/preparing-graphics-for-e-ink-displays?view=all). A red square appeard at the top right of the bitmap image, I couldn't find a fix, so I added a white rectangle to cover it... it's a solution for now... The firmware is available at [`firmware/`](https://github.com/samdev-7/slate/tree/main/firmware).

It was very time consuming entering coordinates, waiting for the display to refresh, and then repeat. I ended up making a [local preview](https://github.com/samdev-7/slate/blob/main/firmware/local-testing.py) using PyGame, similar to HackaPet. 

I then started cadding up [a case](https://cad.onshape.com/documents/a05456ed2d3dbf88ec8105fb/w/51e5dfa304cebdf7213165df/e/a33558805291c7404fa135b9?renderMode=0&uiState=6840f32e09687d4e8403ef6e) for it, and it fits great after a few iterations! One of my goals is to make it as small and slim as possible, so tolerances are really important.

![image](https://github.com/user-attachments/assets/4b9db25d-4a5c-4697-b687-8de7ba8a564e)

https://github.com/user-attachments/assets/4f26c620-6cda-4ded-9eeb-af5da3fae484


**Total time spent: 8h**

# May 16th: De-soldering the connector

One of my goals is to make the badge as thin as possible. I want to be able to hang it on a t-shirt! After making sure the display works, I removed the JST connector as it is very tall. The 2x8 holes will be used to flash it instead. I absolutly suck at desoldering SMD components and had to go in with side cutters, but it works!

![IMG_4982](https://github.com/user-attachments/assets/1f3b9e7f-5081-4f11-ae96-d7179a3360d3)
![IMG_5155](https://github.com/user-attachments/assets/e713df14-a52e-4294-8ccf-8010c34c1fa6)

**Total time spent: 1h**
