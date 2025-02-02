from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

# Настройка Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Имя базы данных
DB_NAME = "KitHome.db"


def init_db():
    """Инициализация базы данных."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                KIT INTEGER DEFAULT 0,
                KOT INTEGER DEFAULT 0
            )
        """)
        conn.commit()


def add_user(user_id):
    """Добавление нового пользователя в базу данных."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO users (id) VALUES (?)
        """, (user_id,))
        conn.commit()


def get_balance(user_id):
    """Получение баланса пользователя."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT KIT, KOT FROM users WHERE id = ?
        """, (user_id,))
        return cursor.fetchone() or (0, 0)


def update_balance(user_id, kit=0, kot=0):
    """Обновление баланса пользователя."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users
            SET KIT = KIT + ?, KOT = KOT + ?
            WHERE id = ?
        """, (kit, kot, user_id))
        conn.commit()


# Инициализация базы данных
init_db()


# Стартовая страница
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    kit, kot = get_balance(user_id)
    return render_template('index.html', kit=kit, kot=kot)


# Страница логина (имитация входа пользователя)
@app.route('/login')
def login():
    # Симуляция авторизации (пользователь с ID 1)
    user_id = 1
    session['user_id'] = user_id
    add_user(user_id)
    return redirect(url_for('index'))


# Задания
@app.route('/tasks')
def tasks():
    """Страница с заданиями"""
    return render_template('tasks.html')


@app.route('/task/subscribe', methods=['POST'])
def task_subscribe():
    """Задание: Подписка на канал"""
    user_id = session['user_id']
    if check_user_subscription(user_id):
        update_balance(user_id, kit=20)
        message = "Вы успешно подписались на канал и получили 20 KIT!"
    else:
        message = "Вы не подписаны на канал. Пожалуйста, подпишитесь, чтобы получить 20 KIT."

    kit, kot = get_balance(user_id)
    return render_template('index.html', kit=kit, kot=kot, message=message)


@app.route('/task/reaction', methods=['POST'])
def task_reaction():
    """Задание: Поставить реакцию"""
    user_id = session['user_id']
    if check_reaction(user_id):
        update_balance(user_id, kit=10)
        message = "Вы поставили реакцию и получили 10 KIT!"
    else:
        message = "Вы не поставили реакцию. Пожалуйста, поставьте реакцию, чтобы получить 10 KIT."

    kit, kot = get_balance(user_id)
    return render_template('index.html', kit=kit, kot=kot, message=message)


@app.route('/task/repost', methods=['POST'])
def task_repost():
    """Задание: Сделать репост"""
    user_id = session['user_id']
    if check_repost(user_id):
        update_balance(user_id, kit=15)
        message = "Вы сделали репост и получили 15 KIT!"
    else:
        message = "Вы не сделали репост. Пожалуйста, сделайте репост, чтобы получить 15 KIT."

    kit, kot = get_balance(user_id)
    return render_template('index.html', kit=kit, kot=kot, message=message)


# Задание: Проверка подписки на канал
def check_user_subscription(user_id):
    # Логика для проверки подписки на канал
    # Например, использовать API Telegram
    return True  # Для теста всегда возвращаем True


# Задание: Проверка реакции
def check_reaction(user_id):
    # Логика для проверки реакции
    return True  # Для теста всегда возвращаем True


# Задание: Проверка репоста
def check_repost(user_id):
    # Логика для проверки репоста
    return True  # Для теста всегда возвращаем True


# Главная страница
if __name__ == '__main__':
    app.run(debug=True)
