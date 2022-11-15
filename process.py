from wxauto import *
import get_pdf_file

def run_process(wx,who):
    wx.ChatWith(who)
    #转到文件传输窗口
    wx.LoadMoreMessage
    msgs = wx.GetAllMessage
    #获取消息
    msg = msgs[-1][1]
    #获取最新消息的，消息部分
    #分割
    msg_split = msg.split()
    get_pdf_file.get_pdf_name(str(msg_split[0]),str(msg_split[1]))
    wx.ChatWith(who)
    reply = 'https://fr0zenwatter.github.io/My_pdf/Matrix_Computition/'+str(msg_split[1])+'.pdf'
    wx.SendMsg(reply)
    


wx = WeChat()
who = "文件传输助手"
run_process(wx,who)




