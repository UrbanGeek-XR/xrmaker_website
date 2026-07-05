import pyautogui
import time
import sys
pyautogui.PAUSE = 0.02
def auto_click_and_paste_fast():
    try:
        # 获取循环次数（简化输入验证）
        loop_count = int(input("循环次数: "))
        
        # 简化的准备提示
        print("5秒后开始...")
        time.sleep(5)
        
        # 快速循环执行
        for _ in range(loop_count):
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    auto_click_and_paste_fast()