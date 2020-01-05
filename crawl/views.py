from django.shortcuts import render
from django.http import HttpResponse
from . import mcheck,geeks_new,programiz_new,stacks_new

# Create your views here.
def home(request):
    return render(request, "index.html")

def jaccard(results, query):
    query = query.split()
    score_dict = {}
    for i in range(len(results)):
        score = (len(set(results[i]['keywords']).intersection(set(query)))) / (len(set(results[i]['keywords']).union(set(query))))
        score_dict[i] = score
    score_dict = sorted(score_dict.items(), key=lambda kv: kv[1], reverse=True)[:10]

    print(score_dict)
    return score_dict

def tf(results, query):
    query = query.split()
    score_dict = {}
    for i in range(len(results)):
        score = (len(set(results[i]['keywords']).intersection(set(query))))
        score_dict[i] = score
    score_dict = sorted(score_dict.items(), key=lambda kv: kv[1], reverse=True)[:10]

    print(score_dict)
    return score_dict

def searched(request):
    if request.method == 'POST':
        query = request.POST.get("query").lower()
        #print(query)
        results=[]
        all_results = mcheck.find(query)
        #print(len(all_results))
        # scores = jaccard(all_results, query)
        scores = tf(all_results, query)
        for i in scores:
            a=[]
            d={}
            d['id']=all_results[i[0]]['_id']
            d['url']=all_results[i[0]]['url']
            if "programiz" in d['url']:
                d['keywords']=" ".join(all_results[i[0]]['keywords'])+" from programiz"
            elif "geeksforgeeks" in d['url']:
                d['keywords'] = " ".join(all_results[i[0]]['keywords']) + " from geeksforgeeks"
            else:
                d['keywords'] = " ".join(all_results[i[0]]['keywords']) + " from stackoverflow"
            a.append(d)
            results.append(a)
            #results.append([all_results[i[0]]['_id'], all_results[i[0]]['url']])
        print(query, type(query))

        #print(results)
        return render(request, 'index.html', {'q':query, 'all_data':results})

    return HttpResponse("It is working!!")

def code(request, slug):
    print(slug)
    finalurl = mcheck.geturl(slug)[0]['url']
    print(finalurl)
    if 'programiz' in finalurl:
        code_array=programiz_new.programiz_crawl(finalurl)

    elif 'geeks' in finalurl:
        code_array=geeks_new.geeks_crawl(finalurl)
    else:
        code_array= stacks_new.stack_crawl(finalurl)

    return render(request,"code.html",{"code":code_array})
    #return HttpResponse("You know that it is working!!")

def test(request):
    l=["#include<stdio.h>","int main(){","","","print(cvbn);}"]
    return render(request,"test.html",{"list":l})
