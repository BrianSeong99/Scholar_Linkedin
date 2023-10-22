import json
import re
if __name__ == '__main__':
    with open("part_info.json", encoding='UTF-8')as f:
        data = json.load(f)
    print("load done...")
    pattern = re.compile(r'persons=(.*), query=.*')
    with open('log.data','w',encoding='UTF-8')as f:
        f.write("person\tpaper\trating\ttimestamp\n")
        for record in data:
            if record["type"] == "lab.nd.search":
                user_id = record['id']
                created_time = record["created_time"]
                m = pattern.match(record['payload'])
                # print(m.group(1))
                persons = json.loads(m.group(1))
                publist = []
                for person in persons:
                    if "pubs" in person:
                        for pub in person['pubs']:
                            publist.append(pub)
                for pub in publist:
                    f.write(user_id+"\t"+pub["id"] +"\t5\t"+created_time+'\n')
                    # print(user_id+"\t"+pub["id"] +"\t5\t"+created_time+'\n')
