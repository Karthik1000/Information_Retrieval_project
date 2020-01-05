from bson import ObjectId
from pymongo import MongoClient
import re
import itertools
#client = MongoClient()

client = MongoClient('localhost', 27017)

mydatabase = client['urldata']

urls = mydatabase.urls

def splitfun(u):
    common = ["is", "the", "a", "an", "and", "or", "have", "of", "for", "was", "this", "that", "in", "it", "to", "by", "its", "on", "from", "with", "what", "when", "where", "which" ]
    s = re.split('[^a-zA-Z]', u.split("/")[3])
    p = list(filter(lambda a: a != '', s))
    return [term.lower() for term in p if term.lower() not in common ]

def all_case(s):
    return list(map(''.join, itertools.product(*zip(s.upper(), s.lower()))))

def create():
    a=['url_files/gfg_a.csv','url_files/gfg_c.csv','url_files/gfg_cpp.csv','url_files/gfg_ds.csv','url_files/gfg_j.csv','url_files/gfg_p.csv','url_files/pc.csv','url_files/pcp.csv','url_files/pdsa.csv','url_files/pj.csv','url_files/pp.csv','url_files/stack_dsa.csv','url_files/stack_algo.csv']
    temp = []
    #t = ""
    for num in range(len(a)):
        # if num==0 or num==3 or num==8 or num==11:
        #     t="gen"
        # elif num==1 or num==6:
        #     t="c"
        # elif num==2 or num==7:
        #     t="cpp"
        # elif num==4 or num==9:
        #     t="j"
        # elif num==5 or num==10:
        #     t="p"

        f = open(a[num])
        for url in f.readlines():
            if num>5 and num<11:
                if "example".casefold() in url:
                    keywords = splitfun(url)
                else:
                    url2 = "/" + url
                    keywords = splitfun(url2)
                url = "https://www.programiz.com" + url
            elif num>=11:
                keywords = splitfun(url)
                url = "https://www.stackoverflow.com" + url
            else:
                keywords = splitfun(url)
            if num == 1 or num == 6:
                keywords.append("c")
            elif num == 2 or num==7:
                keywords.append("c++")
                keywords.append("cpp")
            elif num==4 or num==9:
                keywords.append("java")
            elif num==5 or num==10:
                keywords.append("python")
            entry = {
                'url': url.rstrip('\n'),
                'keywords':keywords
            }
            temp.append(entry)

    result = urls.insert_many(temp)
    return
#create()
# keywords = {"c", "C", "cpp", "Cpp","CPP", "c++", "C++", "python", "Python", "PYTHON", "java", "Java", "JAVA"}
def find(query):
    all_urls = []
    q1 = query
    lwords = set(q1.split())
    # if len(lwords.intersection(keywords)) == 0:
        # print(lwords.intersection(keywords))
    for i in urls.find({}):
        all_urls.append(i)
    # else:
    #     if "c" in all_case(list(lwords.intersection(keywords))[0]):
    #         for i in urls.find({"type": "c"}):
    #             if i in all_urls:
    #                 continue
    #             all_urls.append(i)
    #     if "c++" in all_case(list(lwords.intersection(keywords))[0]) or "cpp" in all_case(list(lwords.intersection(keywords))[0]):
    #         for i in urls.find({"type": "cpp"}):
    #             if i in all_urls:
    #                 continue
    #             all_urls.append(i)
    #     if "java" in all_case(list(lwords.intersection(keywords))[0]):
    #         for i in urls.find({"type": "j"}):
    #             if i in all_urls:
    #                 continue
    #             all_urls.append(i)
    #     if "python" in all_case(list(lwords.intersection(keywords))[0]):
    #         for i in urls.find({"type": "p"}):
    #             if i in all_urls:
    #                 continue
    #             all_urls.append(i)
    return all_urls


# ans = find("BST implementation in python")
# print(len(ans), type(ans))
#count = urls.find({'_id': ObjectId('5deccd92ae0da42841785461')})
#print(list(count))

def geturl(docid):
    required_url= urls.find({'_id': ObjectId(docid)})
    return list(required_url)
# print(check)
# file = open('geeksforgeeks_C.csv')
# l=[]
# for url in file.readlines():
#     entry = {
#         'url':url.rstrip('\n'),
#         'type':'c'
#     }
#     l.append(entry)
# print()


# q1 = {
#     'question': 'Why IR project?',
#     'Answer': 'FUN',
#     'author': 'RP'
# }
#
# q2 = {
#     'question': 'Why SOAD project?',
#     'Answer': ["ans1","ans2"],
#     'author': 'Subu'
# }
# q3 = {
#     'question': 'Why SOAD project?',
#     'Answer': ["ans1","ans2"],
#     'author': 'Karthik'
# }


# #check=posts.find_one({'author': 'Karthik'})
# #print(check)
# print(check['question'])
# print("answers for this question are:\n")
# for a in check['Answer']:
#     print(a)
#     print('------------------------------------------------------------------')
