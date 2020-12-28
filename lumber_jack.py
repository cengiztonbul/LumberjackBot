import pyautogui
import time
import d3dshot

d = d3dshot.create()

pyautogui.click(350, 320)

pyautogui.press('left')
pyautogui.press('left')
# 126, 161, 175

while True:
	screenshot = d.screenshot(region=(220, 78, 221, 579))
	if screenshot.getpixel((0, 500))[0] < 176:
		pyautogui.press('right')
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('left')

	if screenshot.getpixel((0, 400))[0] < 176:
		pyautogui.press('right')
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('left')

	if screenshot.getpixel((0, 300))[0] < 176:
		pyautogui.press('right')
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('left')
	
	if screenshot.getpixel((0, 200))[0] < 176:
		pyautogui.press('right')
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('left')
		
	if screenshot.getpixel((0, 100))[0] < 176:
		pyautogui.press('right')
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('left')

	if screenshot.getpixel((0, 0))[0] < 176:
		pyautogui.press('right')
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('left')



"""
	while i < 5:
		if screenshot.getpixel((210, 600 - i * 100))[0] == 153:
			pyautogui.press('right')
			pyautogui.press('right')
		else:
			pyautogui.press('left')
			pyautogui.press('left')

		i += 1
"""
