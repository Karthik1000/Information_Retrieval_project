from lxml import html
import requests
import time


question_list = []
answer_list = []

class AppCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        
    
    def crawl(self):
        self.get_app_from_link(self.starting_url)
    
        return 
    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)
        
        
        #name  = tree.xpath('//div[@id="main"]//*/a/@href')
        #subject  = tree.xpath('//div[@id="answer-{}"]//*/div[@itemprop="text"]//text()'.format(a))
        subject  = tree.xpath('//div[@id="main"]//*/div[@class="entry-content"]/p/text()')
        question  = tree.xpath('//div[@id="main"]//*/div[@class="container"]//text()')
        #app = App(name)
        if len(question) !=0:
            question_list.append(question)
        else:
            question_list.append('No information yet!! ')
        if len(subject)!=0:
            answer_list.append(subject)
        else:
            answer_list.append('No information yet!! ')

        #print(subject)
        return


crawler = AppCrawler('https://www.geeksforgeeks.org/taking-input-from-console-in-python/',0)
for i in range(1):
    crawler.crawl()
    time.sleep(2)
# print(question_list)
# for i in question_list:
#     for j in i:
#         print(j)
#         print()
#     print('-----------------------------------')
#     print()
# print(answer_list)


# for i in answer_list:
#     print("".join(i))
que = "".join(answer_list[0])
print(que)

#print(question_list)

x = ("".join(question_list[0]))
#print('\n\n',x)
#print('\n\n',type(x))
#print(x)
x=x.replace('\xa0','')
x = x.replace('\r','')
y = x.split('\n')
print(y)

# for i in question_list:
#     print("".join(i))
#     for j in i:
# #        if 'iterator' in j:
#        print(j)
        #print()
    #print('-----------------------------------')
    #print()
