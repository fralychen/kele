from wxpy import *
import urllib3
import json

from apscheduler.schedulers.blocking import BlockingScheduler


'''
初始化登录状态，搜索的好友名称为自己通讯录中的备注名
返回结果为list
'''
bot = Bot(console_qr=True)
kele = bot.friends().search('可乐')[0]
#assistant = bot.friends().search('文件传输助手')[0]

sched = BlockingScheduler()


def send_message():
    '''
    通过API获取json格式诗词、并解析出对应的 标题、作者、内容
    title:  诗词名
    author: 作者
    origin: 内容
    '''
    http = urllib3.PoolManager()
    result = http.request('GET','https://v2.jinrishici.com/sentence', headers={'X-User-Token': 'nzOI8sgvniQZkptd8IGg6iq6KK0D9HOJ'})
    s = json.loads(result.data)
    title = s['data']['origin']['title']
    author = s['data']['origin']['dynasty'] + '--' + s['data']['origin']['author']
    origin = json.loads(result.data)['data']['origin']['content']
    message = "{}\n{}\n{}\n".format(title,author,origin)
    kele.send(message)   #发送消息

def keep_alive():
    single = ""
    kele.send(single)

def cron(event,keep_alive):
    '''
    周一至周五早上8：20执行任务
    '''
    sched = BlockingScheduler()
    sched.add_job(event, 'cron',  day_of_week='1-5', hour=16, minute=23)
    sched.add_job(keep_alive, 'interval', hours=1)
    sched.start()
    
if __name__ == "__main__":
    #send_message()
    cron(send_message,keep_alive)
