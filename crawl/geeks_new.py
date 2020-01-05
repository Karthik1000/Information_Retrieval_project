from lxml import html
import requests
#from. import mcheck
import time

def geeks_crawl(link):
    question_list = []
    answer_list = []
    #link = 'https://www.geeksforgeeks.org/taking-input-from-console-in-python/'
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


    # for i in answer_list:
    #     print("".join(i))
    que = "".join(answer_list[0])
    if 'No information yet!! ' in que or 'No information yet!! ' in question_list[0]:
        x = ("".join(question_list[0]))
        # print('\n\n',x)
        # print('\n\n',type(x))
        # print(x)
        x = x.replace('\xa0', '')
        x = x.replace('\r', '        ')
        y = x.split('\n')
        return y
    else:
        question_list[0].insert(0,que)
        #else:

        #print(question_list)

        x = ("".join(question_list[0]))
        #print('\n\n',x)
        #print('\n\n',type(x))
        #print(x)
        x=x.replace('\xa0','')
        x = x.replace('\r','        ')
        y = x.split('\n')
        return y
