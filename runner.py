#from GenerationController.GenControl import GControl
from telegram.ext import Updater
from GenerationController.GenerationController import GenerationController
import telegram

def main():
    bot = telegram.Bot(token='557166714:AAFxqnpOvzgpN9q1_8ATJIK2d_qxioTgOjM')
    updater = Updater(token='557166714:AAFxqnpOvzgpN9q1_8ATJIK2d_qxioTgOjM')
    updates = bot.get_updates(limit=2)
    chat_id = updates[0].message.chat._id_attrs[0]
    print(bot.get_me())
    bot.send_message(chat_id=chat_id, text="\n\n----Start---\n")
    g = GenerationController("/work/MagicCubeLib/db","TestDB004")
    for x in range(25):
        msg = "Starting Make Generation : {gen}"
        bot.send_message(chat_id=chat_id,
                            text=msg.format(gen=x)
                         )
        size =g.start_gen(x)
        msg1 = "Elemt count of Generation : {gen} | is : {size}"
        bot.send_message(chat_id=chat_id,
                            text=msg1.format(gen=x,size=size)
                         )
    bot.send_message(chat_id=chat_id, text="\n\n----Done---\n")



if __name__ == "__main__":
    main()
locals()
