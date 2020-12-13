#dictionaries
user1={'name':'abhi','age':23}
print(user1)
print(type(user1))

print()

user2=dict(name='karki',age=27)
print(user2)

print(user1['name'])
print(user1['age'])



user3={
    'name':'abhi',
    'age':26,
    'qualification':['10th','12th','diploma','B.Tech','m.Tech']
    }
print(user3)
u=input("which attribute you want to find : ")
print(user3[u])

print()


if 'name' in user3 :
    print('present')
else:
    print('not present')



if 'abhi' in user3.values():
    print('present')
else:
    print('not present')


for i in user3:
    print(i)

for i in user3.values():
    print(i)



user3_items = user3.items()
print(user3_items)
print(type(user3_items))


print()



new_a = user3.pop('qualification')
print("popped items is  ",new_a)
print(user3)




for i,j in user3.items():
    print("key is ",{i})
    print("value is ",{j})

print("\n\n")

user4 = {
    'name':'abhi',
    'age':29,
    'address':'new delhi',
    'qualification':['diploma','b.tech','m.tech']
    }
m_data = {'state':'haryana','city':'faridabad'}
print("\n",user4)
print("\n",m_data)
user4.update(m_data)
print("\n",user4)


print()



d=dict.fromkeys(['name','age','address','class'],'unknown')


print(d)




print(user4.get('name'))

print(user4.get('names','not found'))


d1=user4.copy()
print(d1)

d1.clear()
print(d1)

