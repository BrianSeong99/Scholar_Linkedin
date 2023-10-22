import json,time
from bs4 import BeautifulSoup
from selenium import webdriver
if __name__ == '__main__':
    executable_path = 'G:\\Study_Study\\CS_4th\\soa\\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=executable_path)
    person2id = {}
    field_name = []
    field_name.append("Data_Mining")
    field_name.append("Web_Services")
    field_name.append("Bayesian_Networks")
    field_name.append("Web_Mining")
    field_name.append("Semantic_Web")
    field_name.append("Machine_Learning")
    field_name.append("Database_Systems")
    field_name.append("Information_Retrieval")
    authors_name = set()
    for field in field_name:
        with open(field+".json")as f:
            data = json.load(f)
            authors = data["author"]
            for author in authors:
                authors_name.add(author[1])
    index = 0
    for author in authors_name:
        index += 1
        # if index > 1:
        #     break
        try:
            print(author)
            browser.get('https://www.aminer.cn/search/person?t=b&q='+author)
            time.sleep(2) 
            
            page = browser.page_source.encode("utf-8", "ignore")
            bs = BeautifulSoup(page, "html.parser")
            t_list = bs.find_all(class_="titleName")
            print(t_list[0].attrs['href'].split("/"))
            id = t_list[0].attrs['href'].split("/")[3]
            print(id)
            person2id[author] = id
        except:
            print("sorry but some error occurs when crawling this person's page")
    browser.quit()
    with open("person2id.json",'w')as f:
        f.write(json.dumps(person2id))
