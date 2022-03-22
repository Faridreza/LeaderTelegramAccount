from pyrogram import Client, filters
from pyrogram.types import Message
import jdatetime
import time

API_ID = 000000
API_HASH = ""
client = Client("GrayHat", API_ID, API_HASH)

@client.on_message(filters.me)
async def Admin_Message(_: Client, e: Message):
    try:
        Text = e.text
        Chat_Id = e.chat.id
        User_Id = e.from_user.id
        if Text == "تاریخ":
            Date = jdatetime.datetime.now().strftime("%Y/%m/%d")
            Clock = jdatetime.datetime.now().strftime("%H:%M")
            Wekeand = jdatetime.datetime.now().strftime("%A")
            if Wekeand == "Saturday":
                Wekeand = "شنبه"
            elif Wekeand == "Sunday":
                Wekeand = "یکشنبه"
            elif Wekeand == "Monday":
                Wekeand = "دوشنبه"
            elif Wekeand == "Tuesday":
                Wekeand = "سه شنبه"
            elif Wekeand == "Wednesday":
                Wekeand = "چهارشنبه"
            elif Wekeand == "Thursday":
                Wekeand = "پنجشنبه"
            elif Wekeand == "Friday":
                Wekeand = "جمعه"
            Result = "امروز: {0}\nتاریخ: {1}\nساعت: {2}".format(
                Wekeand, Date, Clock)
            await e.edit(Result)
        if Text == "شماره کارت":
            await e.edit("6273 8111 7508 9140 \n فریدرضا بیدخام")
        if Text == "آف":
            files = open("./State.txt", "w")
            files.write("off")
            files.close()
            await e.edit("برو من حواسم هست🔒")
        if Text == "آن":
            files = open("./State.txt", "w")
            files.write("on")
            files.close()
            await e.edit("سلام خوشومدی🔓")
    except AttributeError:
        pass


@client.on_message(filters.private)
async def Other_Message(_: client, e: Message):
    try:
        Text = e.text
        Chat_Id = e.chat.id
        User_Id = e.from_user.id
        #I am off sened a message check in file txt
        DataFileCheckOnIsOff=open("State.txt","r").read()
        if DataFileCheckOnIsOff == "on":
            await e.reply_text("بفرمایید؟")
        elif DataFileCheckOnIsOff == "off":
            await e.reply_text("سلام وقت کردم جواب میدم🖤",Chat_Id)
    except AttributeError:
        pass

client.run()
