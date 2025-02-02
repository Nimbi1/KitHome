from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Здесь можно подключить HTML-шаблон для интерфейса мини-приложения

if __name__ == "__main__":
    app.run(debug=True)
