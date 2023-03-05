import pywhatkit

# Send a WhatsApp Message to a Contact at 1:30 PM
#pywhatkit.sendwhatmsg("+918884112999", "Hi", 00, 14)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+918884112999", "Hi", 00, 17,2, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("me", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+918884112999", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("me", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("me", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("PyWhatKit")