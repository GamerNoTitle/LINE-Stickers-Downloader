import requests as r
stickers_id = input('请输入要下载的表情包ID：')
url='http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/stickers.zip'.format(stickers_id)
zipper = r.get(url).content
with open( stickers_id + '.zip', 'wb') as f:
    f.write(zipper)