from wxpy import *
import datetime
from threading import Timer


bot = Bot()

def send_message():
    kele = bot.friends().search('可乐')[0]
    kele.send('终于等到你，还好你没放弃')
    print(datetime.datetime.now())
    Timer(15.0, send_message).start()

def main():
    t = Timer(5.0,send_message())
    t.start()

if __name__ == "__main__":
    main()