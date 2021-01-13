import pyautogui
import time
import d3dshot

d = d3dshot.create()

# click the position of the start button
pyautogui.click(350, 320)

# there is not any branch on first 2 click
pyautogui.press('left')
pyautogui.press('left')

while True:
	# take a screenshot of the left side of the tree
	screenshot = d.screenshot(region=(220, 78, 221, 579))
	
	# (0, 500) is the position of the undermost branch 
	# if the red value of the pixel is less than 176,
	# then there is a branch on left side. press the right arrow key
	# else press left.
	# (every branch requires 2 press)
	if screenshot.getpixel((0, 500))[0] < 176:
		pyautogui.press('right')
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('left')
	
	# the distance between two branches is 100 pixels on my computer.
	# therefore it looks for 400, 300 and so on.
	# a loop is a better solution for this.
	# however I had to apply terrible practices, in order to optimize it
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
