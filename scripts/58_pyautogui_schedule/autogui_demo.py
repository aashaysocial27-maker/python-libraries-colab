import platform, subprocess, time
import pyautogui

pyautogui.FAILSAFE = True          # move the mouse to a screen corner to abort
pyautogui.PAUSE = 0.4              # small pause after every action

w, h = pyautogui.size()
print(f"Screen {w}x{h}. Starting in 3 seconds... (move mouse to a corner to stop)")
time.sleep(3)

x, y = w // 2, h // 2
for dx, dy in [(200, 0), (0, 200), (-200, 0), (0, -200)]:
    pyautogui.moveTo(x + dx, y + dy, duration=0.4)
    x, y = x + dx, y + dy

if platform.system() == "Windows":
    subprocess.Popen(["notepad.exe"])
elif platform.system() == "Darwin":
    subprocess.Popen(["open", "-a", "TextEdit"])
time.sleep(2)
pyautogui.write("Hello from ShopEasy automation!", interval=0.05)
pyautogui.press("enter")
pyautogui.screenshot("screen.png")
print("Done. Saved screen.png")