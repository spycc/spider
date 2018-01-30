from spider import Spider

pqurl = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.snv0sov93t'  # 爬取的网络地址
expbig = '<div class="video-info">[\s\S]*?</div>'  # 正则表达式大范围
expsmall1 = '</i>([\s\S]*?)</span>'  # 正则表达式取名字
exqsmall2 = '<span class="video-number">([\s\S]*?)</span>'  # 正则表达式取数字

a = Spider(pqurl, expbig, expsmall1, exqsmall2) #把爬取地址和正则表达式传入类进行内容爬出
a.go() #执行类功能
