from urllib import request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #全局取消证书验证，否则会提示SSL证书错误

class Spider():

    
    def __init__(self, pqurl, expbig, expsmall1, expsmall2):
        '''
        实例化变量，爬取的地址、大范围正则表达式、小范围正则表达式
        '''
        self.pqurl = pqurl  # 爬取的网络地址
        self.expbig = expbig  # 正则表达式大范围
        self.expsmall1 = expsmall1 #正则表达式名字
        self.expsmall2 = expsmall2 #正则表达式人气


    def __openurl(self):
        '''
        打开页面-打开并且返回页面HTML代码
        '''
        r = request.urlopen(self.pqurl)
        html = r.read()
        html = str(html,encoding = 'utf-8')
        return html
        a = 1
    

    def __analysis(self,html):
        '''
        解析页面-提取有用信息并返回结果
        '''
        self.html = html
        newcountlist = []
        countlist = re.findall(self.expbig, self.html)
        for count in countlist:
            name = re.findall(self.expsmall1, count)
            num = re.findall(self.expsmall2, count)
            counts = {'name': name, 'number': num}
            newcountlist.append(counts)
        expmap = lambda countl:{'name': countl['name'][0].strip(),'number':countl['number'][0]} #辅助函数去掉数据中的空格
        return list(map(expmap, newcountlist)) #调用匿名函数，去掉空格和回车


    def __sort(self, listdata):
        '''
        排序函数-把数据进行高低排序 
        '''
        listdata = sorted(listdata, key =self.__sortsee, reverse=True)
        return (listdata)
    def __sortsee(self,bjdata): #辅助排序函数，返回字典中的value进行排序
        r = re.findall('\d*', bjdata['number'])
        num = float(r[0])
        if '万' in bjdata['number']:
            num *= 10000
        return num


    def __show(self,listdata):
        '''
        打印方法，把结果打印出来
        '''
        for mc in range(0,len(listdata)):
            print('第'+str(mc+1)+'名：'+listdata[mc]['name']+'----'+listdata[mc]['number'])

    
    def go(self):
        '''
        主方法，外部调用该方法执行所有操作（打开、解析、排序、展示）
        '''
        html = self.__openurl() #执行爬取页面HTML并返回保存到html
        listdata = self.__analysis(html) #执行内容解析，提取有用信息
        listdata = self.__sort(listdata) #执行排序功能
        self.__show(listdata) #把结果进行展示
