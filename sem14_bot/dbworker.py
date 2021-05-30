import sqlite3

# этот файл нужно выполнить один раз :)

# подключаем базу данных
conn = sqlite3.connect('planner_hse.db')

# курсор для работы с таблицами
cursor = conn.cursor()

# sql запрос для создания таблицы
query = "CREATE TABLE \"planner\" (\"ID\" INTEGER UNIQUE, \"user_id\" INTEGER, \"plan\" TEXT, PRIMARY KEY (\"ID\"))"
# исполняем его –> ура, теперь у нас есть таблица, куда будем все сохранять!
cursor.execute(query)