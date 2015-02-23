#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
from piui import PiUi

ui = PiUi()
file_path = '/home/pi/snicam/videos'


def __init__(self, camera):
    pass

def create_download():
    pass

def start_recording():
    pass

def show_status_page():
    global ui
    stat_page = ui.new_ui_page(title="snipi01-Status", prev_text='Back', onprevclick=create_main)

def show_record_page():
    global ui
    record_page = ui.new_ui_page(title="snipi01-Aufzeichnung", prev_text='Back', onprevclick=create_main)
    img = record_page.add_image("/cam_red_filled.png")
    element = record_page.add_element('<br>')
    record_button = record_page.add_button(text="Record", on_click=start_recording)
    
def show_browser_page():
    global ui, file_path
    browser_page = ui.new_ui_page(title="snipi01-Dateibrowser", prev_text='Back', onprevclick=create_main)
    onlyfiles = [ f for f in listdir(file_path) if isfile(join(file_path,f)) ]
    filelist = browser_page.add_list()
    if count(onlyfiles)>0:
        for file in onlyfiles:
            filelist.add_item(item_text=file.name, chevron=True, toggle=False, onclick=create_download)
    else:
        filelist.add_item(item_text="Verzeichnis leer", chevron=False, toggle=False)
    
def show_settings_page():
    global ui
    settings_page = ui.new_ui_page(title="snipi01-Einstellungen", prev_text='Back', onprevclick=create_main)
    
def show_about_page():
    global ui
    about_page = ui.new_ui_page(title="snipi01-About", prev_text='Back', onprevclick=create_main)
    about_page.add_textbox('Über diese Applikation', element='h1')
    about_page.add_textbox('DIese Applikation ermöglicht es die Kamera des RaspberryPi zu steuern und eine Videoaufzeichnung zu starten', elment='p')

def create_main():
    global ui
    page = ui.new_ui_page(title="snipoint01", prev_text='Home', onprevclick=create_main)
    mainlist = page.add_list()
    mainlist.add_item("Status", chevron=True, toggle=False, onclick=show_status_page)
    mainlist.add_item("Aufzeichnung", chevron=True, toggle=False, onclick=show_record_page)
    mainlist.add_item("Dateiexplorer", chevron=True, toggle=False, onclick=show_browser_page)
    mainlist.add_item("Einstellungen", chevron=True, toggle=False, onclick=show_settings_page)
    mainlist.add_item("Über diese App", chevron=True, toggle=False, onclick=show_about_page)
    
        

#Main Loop
create_main()
ui.done()


