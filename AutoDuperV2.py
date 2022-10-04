from ctypes.wintypes import SIZE
import keyboard
import webbrowser
import win32api, win32con
import threading
import pyautogui
import time
import PySimpleGUI as sg
import numpy as np
#delayLeft = 2
#delayRight = 0.1
delay = 0.5
startDelay = 5
pickupDelay = 0.75
script_running = False

def main():
    def dupingClicker():
        
        # def rightClicker():
            # print("rightClicker activated")
            # time.sleep(10)
            # while keyboard.is_pressed('alt') == False and script_running == True:
                # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                # time.sleep(0.1)
                # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                # time.sleep(delayRight)

        # def leftClicker():
            # print("leftClicker activated")
            # time.sleep(12)
            # while keyboard.is_pressed('alt') == False and script_running == True:
                # pyautogui.click()
                # time.sleep(delayLeft)
        
        def leftClick():
            pyautogui.click()
        def rightClick():
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        
        def clicker():
            time.sleep(startDelay)
            rightClick()
            time.sleep(delay)
            while keyboard.is_pressed('alt') == False and script_running == True:
                leftClick()
                time.sleep(pickupDelay)
                rightClick()
                time.sleep(delay)
            
            
        
        t1 = threading.Thread(target=clicker)
        t1.start()

        t1.join() 
        print("Script Finished Clicking")
        sg.popup_ok('Finished Duping', title=('Script Stopped'))
    menu = ['&GitHub', ['Visit GitHub Project Page',]],
    layout = [  
                [sg.Menu(menu)],
                [sg.Text('Click delay: '), sg.Spin(initial_value=0.5, values=tuple(np.arange(0.1,4.0,0.1)),size=(5, 5)), sg.Text('seconds')],
                [sg.Text('Item pickup delay: '), sg.Spin(initial_value=0.75, values=tuple(np.arange(0.1,4.0,0.1)),size=(5, 5)), sg.Text('seconds')],
                [sg.Text('Default delay is recommended')],
                [sg.Button('Start Duping'),sg.Button("Help"),sg.Text('', size=(22, 0)), sg.Button('Exit')],
                [sg.StatusBar('Script not running', key='-STATUS-')]]
    window = sg.Window('Item Frame Duper v2 by nimaid', layout, size=(450, 180), font='bold', icon=r"item_frame.ico")
   
    while True:
        event, values = window.read()
        if event == 'Help':
            sg.popup('Instructions','I recommend leaving the delays as they are.\nWhen you start the script you have {} seconds to switch to Minecraft and get into position. To stop the script hold the ALT key for a few seconds.'.format(startDelay))
        if event == 'Start Duping':
            window['Start Duping'].update(disabled=True)
            print('pressed button - activate script')
            window['-STATUS-'].update('Script is now running...')
            delay = float(values[1])
            pickupDelay = float(values[2])
            script_running = True
            sg.popup_notify('Hold ALT to stop duping') 
            dupingClicker() 
            script_running = False 
            window['-STATUS-'].update('Script is not running')
            window['Start Duping'].update(disabled=False)
        if event == 'Visit GitHub Project Page':
            webbrowser.open('https://github.com/nimaid/Item-Frame-Duper-for-6b6t')    
        if event == sg.WIN_CLOSED or event == 'Exit':
            script_running = False
            break
        

    window.close()   


if __name__ ==  '__main__':
    main()
