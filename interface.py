from dearpygui.core import *
from dearpygui.simple import *
import bot

set_main_window_size(540,720)
set_global_font_scale(1.25)

envUsername = bot.getAccountLoginDetails("USERNAME")
envPassword = bot.getAccountLoginDetails("PASSWORD")

def button_click():
    username_value = get_value("Username")
    password_value = get_value("Password")
    bot.main(username_value, password_value)

with window("PoC Instagram Bot", width=540, height=720):
    set_window_pos("PoC Instagram Bot", 0,0)
    add_input_text("Username", default_value=envUsername)
    add_input_text("Password", default_value=envPassword)
    add_button("Run Bot", callback=button_click)

    
start_dearpygui()
