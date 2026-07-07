import pyautogui
import time
import random
pyautogui.PAUSE = 0
# 去掉最后的 }，交给编辑器自动补全
code = "#include <iostream>\nusing namespace std;\nint main()\n{\n\nreturn 0;"

char_min = 0.01
char_max = 0.13
line_delay = 0.2

for ch in code:
    if ch == "\n":
        pyautogui.press("enter")
        time.sleep(line_delay)
    else:
        pyautogui.typewrite(ch)
        time.sleep(random.uniform(char_min, char_max))
