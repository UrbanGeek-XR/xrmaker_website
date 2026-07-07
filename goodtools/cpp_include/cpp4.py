import pyautogui
import time
import random
pyautogui.PAUSE = 0
# 去掉最后的 }，交给编辑器自动补全
code = "#include <iostream>\nusing namespace std;\nint main()\n{\n\nreturn 0;"

char_min = 0.01
char_max = 0.13
line_delay = 0.2

print("倒计时5秒，请切到代码编辑器！")
time.sleep(5)

for ch in code:
    if ch == "\n":
        pyautogui.press("enter")
        time.sleep(line_delay)
    else:
        pyautogui.typewrite(ch)
        time.sleep(random.uniform(char_min, char_max))
print("输入完成，编辑器已自动补齐右大括号")
