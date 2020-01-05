
from lxml import html
import requests
import time
def stack_crawl(link):
    question_list = []
    answer_list = []

    sup_list = []
    head = []
    head.append(link)
    #head = ['https://stackoverflow.com/questions/59233720/time-complexity-of-binary-tree-traversal-pre-order']
    for link in head:
        dict1 = {}
        question_list = []
        answer_list = []
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        question = tree.xpath('//div[@class="container"]//*/a[@class="question-hyperlink"]/text()')
        #print(question)
        if len(question) != 0:
            question = question[0]

            name  = tree.xpath('//div[@id="answers"]//*/a/@href')
            if len(name) != 0:
                token = []
                for j in name:
                    if '/a/' in j:
                        token.append((j[3:]))

                #answer_list.append(question)
                print(token)
                for a in token:
                    #name  = tree.xpath('//div[@id="answer-{}"]//*/pre/code/text()'.format(a))
                    subject  = tree.xpath('//div[@id="answer-{}"]//*/div[@itemprop="text"]//text()'.format(a))

                    #app = App(name)
                    #question_list.append(name)

                    answer_list.append(subject)
            dict1['question'] = question
            if len(answer_list) == 0:
                dict1['answer'] = 'No answer yet !!'
            else:
                dict1['answer'] = answer_list
            sup_list.append(dict1)
            #print(name)

            # print(question)
            # for i in answer_list:
            #     for j in i:
            #         print(j)
            #         #print()
            #     print('-----------------------------------')
    x = dict1['answer']
    #print(x)
    y = []
    for i in x:
        for j in i:
            y.append(j)

    y = "".join(y)
    #print(y)
    x = y
    x=x.replace('\xa0','')
    x = x.replace('\r','')
    y = x.split('\n')
    return (y)
