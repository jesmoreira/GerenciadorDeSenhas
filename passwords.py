import sqlite3

MASTER_PASSWORD = '123456'

senha = input('Insira sua senha master:')
if senha != MASTER_PASSWORD:
    print('Senha inválida! encerrando ...')
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username  TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print('*' * 20)
    print('* i: Inserir nova senha *')
    print('* l: listar serviços salvos *')
    print('* r: recuperar um senha *')
    print('* s: sair *')
    print('*' * 20)


def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')


    if cursor.rowcount == 0:
        print('Serviço não cadastrado (use 1 para verificar os serviços). ')
    else:
        for user in cursor.fetchall():
            print(user)
    


def insert_password(service, username, password):
    cursor.execute(f''' 
        INSERT INTO users (Service, username, password)
        Values ('{service}', '{usarname}', '{password}')''')
    conn.commit()


def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input('O que deseja ? ')
    if op not in ['i','l', 'r','s']:
        print('\n(Opção invalida, tente novamente!)')
        continue

    if op == 's':
        print('Saindo...')
        break

    if op == 'i':
        service = input('Qual o nome do serviço? ')
        usarname = input('Qual o nome de usuario? ')
        password = input('Qual a senha? ')
        insert_password(service, usarname, password)


    if op == 'l':
        show_services()


    if op == 'r':
        service = input('Qual o serviço para qual quer a senha? ')
        get_password(service)


conn.close()