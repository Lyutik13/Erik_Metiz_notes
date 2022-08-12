bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Обращение к элементам списка  (Также можно использовать строковые методы из главы 2)
print(bicycles[0].title())

# последний элемент в списке: [-1]

# f-строка для построения сообщения:
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
