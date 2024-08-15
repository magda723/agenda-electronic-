import sqlite3

connection = sqlite3.connect('diary.db')

cursor = connection.cursor()

sql = '''
create table if not exists progress
(
id integer primary key autoincrement,
subject text,
grade integer
);
'''
cursor.execute(sql)
connection.commit()

print('Salut de la Fox!')
print('Ce trebuie să facem?')

while True:
    x = input('Fox> ')
    if x == 'exit':
        break

    if x == 'help':
        print("help – lista de comenzi")
        print("show - arată lista de note")
        print("add [cod materie] [nota] - adaugă înregistrare")
        print("Codurile materiilor:")
        print("m - Matematică")
        print("g - Geometrie")
        print("i - Informatică")
        print("update [id] [nota nouă] - actualizează nota")
        print("del [id] - șterge înregistrare")
        print("exit - ieșire")

    elif x == 'show':
        cursor.execute('select * from progress;')
        y = cursor.fetchall()

        if len(y) == 0:
            print('Datele inca nu au fost adaugate')
        else:
            for i in y:
                print('id={} {} - {}'.format(i[0], i[1], i[2]))

    elif x[:3] == 'add':
        scode = x[4]
        subject = None
        if scode == 'm':
            subject = 'Matematica'
        elif scode == 'g':
            subject = 'Geografia'
        elif scode == 'i':
            subject = 'Informatica'
        else:
            print('Disciplina nu a fost adaugata')
            continue

        if len(x) == 8:
            grade = x[6] + x[7]
        else:
            grade = x[6]
        
        if int(grade) > 10:
            print('Nota nu trebuie sa fie mai mare decat 10')
        else:
            cursor.execute('insert into progress(subject, grade) values (?, ?)', (subject, grade))
            connection.commit()
        print('ok')
    elif x[:6] == 'update':
        id_nota = x[7]
        # if len(x[8:10]) == 2:
        #     id_nota = x[8] + x[9]
        # else:
        #     id_nota = x[8]

        if len(x) == 10:
            grade = x[9]
        elif len(x) == 11:
            grade = x[9] + x[10]
        elif len(x) == 13:
            grade = x[10] + x[11]

        sql = 'update progress set grade=? where id=?'
        cursor.execute(sql, (grade,id_nota))
        connection.commit()
        print('ok')

    elif x[:3] == 'del':
        id_nota = x[4]
        sql = 'delete from progress where id=?'
        cursor.execute(sql, (id_nota))
        connection.commit()        
        print('ok')
    else:
        print('Comanda nu este în lista!')
    
   
connection.close()
print('La revedere! Vă aștept din nou!')
        

