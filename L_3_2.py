def info(name, surname, data, city, email, telephone):
    return f'Вас зовут: {name}. ' \
            f'Ваша фамилия: {surname}. ' \
            f'Родились: {data},' \
            f' в городе: {city}. ' \
            f'Ваш электронный адрес: {email},' \
            f' а телефон: {telephone}.'

n = input('Введите ваше Имя: ')
ph = input('Введите вашу Фамилия: ')
dt = input('Введите вашу дату рождения: ')
ct = input('Введите ваш город: ')
ml = input('Введите ваш почтовый адрес: ')
tp = int(input('Введите ваше Телефон: '))

print(info(name=n, surname=ph, data=dt, city=ct, email=ml, telephone=tp))