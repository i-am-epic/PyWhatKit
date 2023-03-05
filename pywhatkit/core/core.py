import os
import pathlib
import time
from platform import system
from urllib.parse import quote
from webbrowser import open
import spotify
import requests
from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite, write, keyDown , keyUp

from pywhatkit.core.exceptions import InternetException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip


driver = webdriver.Chrome(
    '/Users/nikhilav/Development/projects/whatsapp/chromedriver_mac_arm64 (1)/chromedriver')

time.sleep(2)
print("hss")

print("connected")
driver.get("https://web.whatsapp.com/#")
time.sleep(20)


WIDTH, HEIGHT = size()


def check_number(number: str) -> bool:
    """Checks the Number to see if contains the Country Code"""

    return "+" in number or "_" in number


def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    time.sleep(wait_time)
    _system = system().lower()
    if _system in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif _system == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{_system} not supported!")
    press("enter")


def findtextbox() -> None:
    """click on text box"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\pywhatkit_smile1.png")
    try:
        moveTo(location[0] + 150, location[1] + 5)
        click()
    except Exception:
        location = locateOnScreen(f"{dir_path}\\data\\pywhatkit_smile.png")
        moveTo(location[0] + 150, location[1] + 5)
        click()


def find_link():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\link.png")
    print(location)
    try:
        moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
        click()
    except Exception:
        location = locateOnScreen(f"{dir_path}\\data\\link2.png")
        moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
        print(location)
        click()


def find_document():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\document.png")
    print(location)
    moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
    click()


def find_photo_or_video():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\photo_or_video.png")
    print(location)
    moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
    click()


def check_connection() -> None:
    """Check the Internet connection of the Host Machine"""

    try:
        requests.get("https://google.com")
    except requests.RequestException:
        raise InternetException(
            "Error while connecting to the Internet. Make sure you are connected to the Internet!"
        )


def _web(receiver: str, message: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)


def send_message(message: str, receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""

    _web(receiver=receiver, message=message)
    time.sleep(7)
    click(WIDTH / 2, HEIGHT / 2 + 15)
    time.sleep(wait_time - 7)
    if not check_number(number=receiver):
        for char in message:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    findtextbox()
    press("enter")


def copy_image(path: str) -> None:
    """Copy the Image to Clipboard based on the Platform"""

    _system = system().lower()
    if _system == "linux":
        if pathlib.Path(path).suffix in (".PNG", ".png"):
            os.system(f"copyq copy image/png - < {path}")
        elif pathlib.Path(path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"copyq copy image/jpeg - < {path}")
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    elif _system == "windows":
        from io import BytesIO

        import win32clipboard  # pip install pywin32
        from PIL import Image

        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    elif _system == "darwin":
        if pathlib.Path(path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            os.system(
                f"osascript -e 'set the clipboard to (read (POSIX file \"{path}\") as JPEG picture)'"
            )
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    else:
        raise Exception(f"Unsupported System: {_system}")


def send_image(path: str, caption: str, receiver: str, wait_time: int) -> None:
    """Sends the Image to a Contact or a Group based on the Receiver"""

    _web(message=caption, receiver=receiver)
    time.sleep(7)
    click(WIDTH / 2, HEIGHT / 2 + 15)
    time.sleep(wait_time - 7)
    copy_image(path=path)
    if not check_number(number=receiver):
        for char in caption:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    else:
        typewrite(" ")
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    time.sleep(1)
    findtextbox()
    press("enter")


def change_about():
    print("hss")
    #element = driver.find_element(By.CLASS_NAME, "_3g4Pn _2HcPg")
    #elem1 = driver.findElement(By.xpath("//img[@class='_1jLYl _1PAkz _11JPr']"));
    press('tab',presses=4)
    press('enter')
    press('up',presses=2)
    press('enter')
    ele = driver.find_element(By.XPATH,"//div[contains(@class,'_199zF _3j691 _3uDlQ')]")
    ele.click()
    #imgResults = driver.find_element(By.XPATH,"//img[contains(@class,'_1jLYl _1PAkz _11JPr')]")

    #element = driver.find_element_by_class("_1jLYl _1PAkz _11JPr")
    #imgResults.click()
    #click(on_element=)
    time.sleep(1)
    #element2 = driver.find_element_by_class("_2wqji")

    while True:
        ele2 = driver.find_element(By.XPATH,"//button[contains(@title,'Click to edit About')]")

        about = spotify.get_current_play(spotify.SPOTIFY_ACCESS_TOKEN)
        about_pretty = "Listening to Spotify                                                            {} - {}".format(about['name'],about['artist'])
        print(about_pretty)
        pyperclip.copy(about_pretty)
        ele2.click()
        time.sleep(1)
        txtbx = driver.find_element(By.XPATH, "//div[contains(@contenteditable, 'true')]")
        txtbx.clear()

        """keyDown('command')
        press('a')
        keyUp('command')
        keyDown('command')
        press('v')
        keyUp('command')"""
        #pyperclip.paste()
        txtbx.send_keys(about_pretty)
        time.sleep(1)
        press('enter')
        time.sleep(10)
    
    #driver.quit()
"""def change_about_to_spotify():
    song = spotify.curr_play()
    print(song)
    change_about(str(song))
"""
    
print("start")
change_about()
