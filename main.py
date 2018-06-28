#!/usr/bin/python
# -*- coding: UTF-8 -*-
from wxpy import *
from kugou_utils import *


def main():
    print("开始运行")
    bot = Bot(True, True)
    bot.auto_mark_as_read = False
    tuling = Tuling("63d066dabdb5429c85997f0f4716c36f")
    xiaoI = XiaoI("TAb0e7tKgYDg", "Rts9o2E5RwxUtP9R8wtu")
    leave_msg_list = []
    tuling_auto_reply_list = []
    xiaoI_auto_reply_list = []
    kugou_utils_list = []
    kugou_search_return_list = []

    @bot.register(Friend, TEXT)
    def auto_reply(msg):
        print(msg)
        text = msg.text
        sender = msg.sender
        # 退出操作
        if sender in leave_msg_list:
            if text == "结束":
                leave_msg_list.remove(sender)
                msg.reply("好的，我将会尽快把你的信息转告给主人。")
        elif sender in tuling_auto_reply_list:
            if text == "结束":
                tuling_auto_reply_list.remove(sender)
                msg.reply("已退出图灵机器人回复模式")
            else:
                tuling.do_reply(msg)
        elif sender in xiaoI_auto_reply_list:
            if text == "结束":
                xiaoI_auto_reply_list.remove(sender)
                msg.reply("已退出小i机器人回复模式")
            else:
                xiaoI.do_reply(msg)
        elif sender in kugou_utils_list:
            try:
                i = int(text)
                if not i > len(kugou_search_return_list) or i <= 0:
                    item=kugou_search_return_list[i - 1]
                    details=get_music_details(item["FileHash"])
                    msg.reply(details["data"]["play_url"])
                else:
                    msg.reply("错误的下标哦")
            except Exception:
                if text == "结束":
                    kugou_utils_list.remove(sender)
                    msg.reply("已退出酷狗工具")
                else:
                    kugou_search_return_list.clear()
                    search_return = search_music(text, tag="")
                    reply_text = "找到以下结果:\n  "
                    for i in range(len(search_return["data"]["lists"])):
                        item = search_return["data"]["lists"][i]
                        kugou_search_return_list.append(item)
                        reply_text = reply_text + str(i + 1) + "." + item["FileName"] + "\n  "
                    print(reply_text)
                    msg.reply(reply_text)
        # 选择操作
        else:
            if text == "0":
                msg.reply("已退出自动程序")
                bot.logout()
            if text == "1":
                leave_msg_list.append(sender)
                msg.reply("好了，开始留言吧，回复结束退出")
            elif text == "2":
                tuling_auto_reply_list.append(sender)
                msg.reply("已进入图灵机器人自动回复模式，回复结束退出")
            elif text == "3":
                xiaoI_auto_reply_list.append(sender)
                msg.reply("已进入小i机器人自动回复模式，回复结束退出")
            elif text == "4":
                msg.reply("没看见菜单上没有4吗，你怎么这么皮？")
                return
            elif text == "5":
                kugou_utils_list.append(sender)
                msg.reply("请输入搜索关键字")
                return
            elif text == "6":
                return
            elif text == "7":
                return
            else:
                msg.reply('''我能为你做什么？
1.留言
2.图灵机器人
3.小i机器人
5.酷狗解析''')

    embed()


if __name__ == '__main__':
    main()
