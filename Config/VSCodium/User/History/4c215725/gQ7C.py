#============================================================списки/словарь===============================================================

#//*    "Имя": "Виктор"
#//*    "Возраст": "30"
#? словари содержут пары( ключь: значение)

my_dict1 = {}
my_dict2 = dict()
print(type(my_dict1))
print(type(my_dict2))

#============================================================списки/словарь===============================================================

my_dict = {
	"user": "Thomas Anderson",
	"nickname": "Neo",
	"tean": ("Morpheus", "Trinity"),
	#![1,2,3]: "Hello" - нельзя передавать spiskki
	#todo Ипспользовать for key("user") можно только НЕ ИЗМЕНЯЙМЫЕ ТИПЫ ДАННЫХ#
	#? число, строку или даже кортедж(лучше str or int)
	1:"Marix",
	"has":"you",
	(1,2,3):"Hello"
	}
	#? значениями могут быть ЛЮБЫЕ обьекты
print(my_dict)
print(f"-"*143)
#todo чтобы обратиться к конкретрной части словаря мы используем не индексы, а тут мы обращаемся к нему...
print(my_dict["user"])
#! через ключ("user")
print(f"-"*20)
print(my_dict[1])
print(f"-"*20)
print(f"{my_dict[(1,2,3)]}")
print(f"-"*143)

#============================================================списки/словарь===============================================================

monts = {1:"january", 2:"February"}

print(monts[2])
print(f"-"*143)

#============================================================списки/словарь===============================================================

person = {"Name":"Виктор", "age":27, "рост":180}
print(person["рост"])
print(f"-"*143)

#============================================================списки/словарь===============================================================
#                                                        !добовляем новые пары!

print(person)
person["вес"]=93
# todo для этого нужно обратиться к словарю, в [ ] указать ключ пары, а после = значение
person["любимое блюдо"]= "карбонара"
print(person)
print(f"-"*143)

#============================================================списки/словарь===============================================================
#                                                   !изменение значение пар в словоре! 

person["вес"]= 109
#todo указываем ключ значение которого мы хотим изменить [ ], а потом присваеваем ему новое значение 
print(person)
print(f"-"*143)


#============================================================списки/словарь===============================================================
#                                                            !удаляем пары!

#todo use функцию "del", затем передаём имя словоря и удаляймый КЛЮЧ

'''del person["любимое блюдо"]
print(person)
print(f"-"*143)'''

#============================================================списки/словарь===============================================================
#                                                         !перебераем все пары!
#?сначала добавим пару с автомобилем
#? k - key, v - value(ценность)

person["машина"]="Porshe"

#todo .items- возращает список пар ключ:значение(переберает всё)

for k, v in person.items():
	print(f"{k} >>> {v}") 
print(f"-"*143)
#                                            !это было с указанием метода, то-есть(.items)!

#============================================================списки/словарь===============================================================
#                                                         !теперь без .items!

for key in person:
	print(f"{key}")
#? если не исользовать for и переберать словарь без метода(.items), перебор по ключам используется по defolt
print(f"-"*143)

#============================================================списки/словарь===============================================================
#                                      !мы получим тоже самое применив метод keys к нашему словарю!

for key in person.keys():
	print(f"{key}")

#============================================================списки/словарь===============================================================
#todo перебор по ключам может быть полезен для того, чтобы понять, исопльзовался ли данный ключ или нет

if "язык" in person.keys():
	print(f"is used")
else:
	print(f"no problem")
print(f"-"*143)

#============================================================списки/словарь===============================================================
#                                           !values нужен чтобы перебрать только ЗНАЧЕНИЯ!

for v in person.values():
	print(f"{v}")

print(f"-"*143)
#============================================================списки/словарь===============================================================
#? добавим больше любимых блюд
#todo для этого удобнее всего будет обьеденить блюда в list

person = {
	'Name': 'Виктор',
	'возраст': 27, 
	'рост': 180, 
	'вес': 109, 
	'любимое блюдо': ['карбонара','пельмешки','картошка с грибами'], 
	'машина': 'Porshe'
}

#todo чтобы вывысести блюда, нужно пробежаться циклом по 'любимое блюдо'
for v in person['любимое блюдо']:
	print(f'{v}')
print(f'-'*143)

#============================================================списки/словарь===============================================================
#                                       !часто можно встретить конструкцию словарь в соловаре!

persons = {
	"Александр":{
	'возраст': 27, 
	'рост': 180, 
	'вес': 109, 
	'любимое блюдо': ['карбонара','пельмешки','картошка с грибами'], 
	'машина': 'Porshe'
},
	"Ольга":{
	'возраст': 28, 
	'рост': 165, 
	'вес': 148, 
	'любимое блюдо': ['кукуруза','креветки'], 
	'машина': 'BMV'
}
}

for username, userinfo in person.items():
	print(f'Имя пользователя:{username},')
	age = userinfo["возраст"]
	car = userinfo["машина"]
	print(userinfo)
	print(f"Возраст пользователя {username} :{age} лет.")
	rpint(f"Avto пользователя {username} : {car}\n")

















