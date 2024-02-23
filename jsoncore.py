import json

#Функция обнуления количества баллов у всех факультетов#
#def write(data, filename):
#    data = json.dumps(data)
#    data = json.loads(str(data))
#    with open(filename, 'w', encoding='utf-8') as file:
#        json.dump(data, file, ensure_ascii=False, indent=4)


#def read(filename):
#    with open(filename, 'r', encoding='utf-8') as file:
#        return json.load(file)


data = {
    "Гриффиндор": 0,
    "Хаффлпафф": 0,
    "Рейвенкло": 0,
    "Слизерин": 0
}
#Функция обнуления количества баллов у всех факультетов#
#write(data, 'score.json')



#Функция записи количества баллов#
with open('score.json', 'r', encoding='utf-8') as json_file:
    change_score = json.load(json_file)


x = int(input("Введите количество баллов: "))

change_score["facultets"][0]['Баллов'] += x


with open('score.json', 'w', encoding='utf-8') as json_file:
    json.dump(change_score, json_file, ensure_ascii=False, indent=4)


