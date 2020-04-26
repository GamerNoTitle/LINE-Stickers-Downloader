import requests as r
import ctypes
import time
import sys
ctypes.windll.kernel32.SetConsoleTitleW("LINE表情包下载 - GamerNoTitle")
print('======================================================================================')
print('本程序仅供开发者本人方便下载LINE表情包使用，因使用本程序造成的法律责任开发者概不负责！')
print('======================================================================================')
while True:
    stickers_id = input('请输入要下载的表情包ID：')
    if stickers_id == '':
        print('非法参数！即将退出程序！！！')
        time.sleep(5)
        sys.exit()
    url='http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/stickers.zip'.format(stickers_id)
    zipper = r.get(url).content
    try:
        with open( stickers_id + '.zip', 'wb') as f:
            f.write(zipper)
        print('下载ID为{}的表情包完成，已存储为{}.zip'.format(stickers_id,stickers_id))
    except:
        print('下载失败！请检查网络连接！')
    exitornot=input('是否继续下载（Y/N）')
    if exitornot != 'Y' or exitornot != 'y':
        sys.exit()