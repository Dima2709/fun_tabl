import sqlite3 as sq
#conn = sq.connect('data.db')
#cr = conn.cursor()
#cr.execute('''CREATE TABLE students (id serial primary key, name varchar(255), last_name varchar (255), course varchar(255))''')
#cr.execute("""INSERT into students values (1, 'Arkasha', 'Ivanov', 'Java')""")
#cr.execute("""INSERT into students values (2, 'Anna', 'Grusheva', 'Python')""")
#conn.commit()
#cr.execute('''select * from students''')
#a = cr.fetchall()
b = {'id': 11, 'name': 'Arkasha', 'last_name':'Korneev', 'course': 'Python'}
c = {'id': 12, 'name': 'Anna', 'last_name':'Pavlovna', 'course': 'Python'}
d = {'id': 13, 'name': 'Snezhana', 'last_name':'Hersonskay', 'course': 'Python'}
def the (cm, tb, *args):
    import sqlite3 as sq
    conn = sq.connect('data.db')
    cr = conn.cursor()
    if cm == 'select':
        if len(args) == 0:
           cr.execute(str("SELECT * from "+tb))
           res = cr.fetchall()
           print(res)
           return res
        elif len(args) > 0:
            for i in args:
                cr.execute("SELECT "+str(i) + " from " + tb)
                res = cr.fetchall()
                print(res)

    elif cm == 'insert':

        if tb == 'students':
             info = ['id', 'name', 'last_name', 'course']
             print('input id')
             q = int(input())
             mass = [q]
             for i in info[1:]:
                print('input', i)
                q = input()
                mass.append(q)
             mass = tuple(mass)
             cr.execute('insert into '+ tb + ' values ' + str(mass))
             conn.commit()
        elif tb == 'test':
            print(tb)

        elif len(args) > 0:
            for i in args:
                mass = []
                for j in list(i.keys()):
                      mass.append(i[j])
                mass = tuple(mass)
                cr.execute('insert into ' + tb + ' values ' + str(mass))
                conn.commit()

    elif cm == 'create':
        cr.execute('CREATE TABLE '+ tb + str( args))
        conn.commit()

the('insert', 'test')
