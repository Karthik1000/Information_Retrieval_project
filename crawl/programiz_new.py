from lxml import html
import requests
import time
import fnmatch
def programiz_crawl(link):
    question_list = []
    answer_list = []


    #link = 'https://www.programiz.com/c-programming/examples/add-numbers'
    start_page = requests.get(link)
    tree = html.fromstring(start_page.text)


    #name  = tree.xpath('//div[@id="main"]//*/a/@href')
    #subject  = tree.xpath('//div[@id="answer-{}"]//*/div[@itemprop="text"]//text()'.format(a))
    #subject  = tree.xpath('//div[@id="main"]//*/div[@class="entry-content"]/p/text()')
    question  = tree.xpath('//div[@id="programiz-main-content"]//*/div[@class="field-items"]//text()')
    if len(question) != 0:
        question_list.append(question)
    else:
        question_list.append('No information yet!! ')

    # for i in range(1):
    #     crawler.crawl()
    #     time.sleep(2)


    for i in question_list[0]:
        if 'div' in i:
            question_list[0].remove(i)

    #print(question_list)
    # for i in question_list[0]:
    #     print(question_list[0][i].split('\n'))
    # for i in question_list:
    #     print("".join(i))
    x = ("".join(question_list[0]))
    #print('\n\n',x)
    #print('\n\n',type(x))
    #print(x)
    x=x.replace('\xa0','')
    x = x.replace('\r','      ')
    y = x.split('\n')
    #print(y)
    return y
