import pyautogui

paswrd = pyautogui.password(text='', title='', default='', mask='*')
print(paswrd)