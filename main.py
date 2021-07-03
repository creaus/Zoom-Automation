from datetime import datetime

import keyboard
import pandas as pd
import pyautogui
import subprocess
import time

# reading the meeting details
df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()

while True:
    # Check the current system time
    timestr = datetime.now().strftime("%H:%M")
    # Check if the current time is mentioned in the Dataframe
    if timestr in df.Time.values:
        df_new = df[df['Time'].astype(str).str.contains(timestr)]
        # Open the Zoom app
        subprocess.Popen("***Put the location of the Zoom app here***")
        time.sleep(9)
        # clicks the join button
        join_btn = pyautogui.locateCenterOnScreen('join_button.png')
        pyautogui.moveTo(join_btn)
        pyautogui.click()
        time.sleep(5)

        # Write the meeting ID from the dataframe onto the Zoom App
        keyboard.write(str(df_new.iloc[0, 1]))
        pyautogui.press('enter')
        time.sleep(6)

        # Reads the Meeting Passcode from the dataframe and enters into the zoom app
        keyboard.write(str(df_new.iloc[0, 2]))

        # For finally joining the meeting
        pyautogui.press('enter')

        # Automatically killing the program
        # time.sleep(180)
        # subprocess.call(["taskkill", "/F", "/IM", "Zoom.exe"])/*

        # Wait for one minute before the next iteration starts
        time.sleep(60)
