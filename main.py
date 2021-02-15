# Author Mujahid Ahmed
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pyttsx3
engine = pyttsx3.init()

data = pd.read_csv("test.csv")
data_dict = data.to_dict(('list'))
leads = data_dict['Number']
# messages = data_dict['Message']
message = "This is a test message"
combo = zip(leads)

first = True
i = 0
for lead in combo:
    time.sleep(4)
    lead1 = '91_{}'.format(lead)
    link = str("https://web.whatsapp.com/send?phone="+lead1+"&text="+message)
    # link = str("https://api.whatsapp.com/send?phone="+lead1+"&text="+message)
    web.open(link)
    if first:
        time.sleep(6)
        first = False

    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    i = i+1
    time.sleep(8)
    engine.say(str(i))
    engine.say("Messages sent Successfully")
    engine.runAndWait()
    pg.hotkey('command','w')
    
engine.say("All The Messages sent successfully")
engine.runAndWait()
