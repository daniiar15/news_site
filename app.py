from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Пример списка новостей с комментариями
news = [
    {
        'id': 1,
        'title': 'Мэрия Бишкека продолжает демонтировать рекламные баннеры',
        'description': "В Ленинском районе Бишкека демонтируют рекламные конструкции. Об этом сообщает пресс-служба муниципалитета."
                        "По ее данным, на улице Фрунзе от улицы Барпы Алыкулова до улицы Пограничной демонтировано 70 конструкций и 7 штендеров, снято 132 баннера."
                        "Все они установлены без разрешений и нарушали правила размещения наружной рекламы."
                        "Напомним, Садыр Жапаров поручил мэрии Бишкека до 31 августа полностью убрать старые рекламные щиты в городе. Президент предложил вместо баннеров установить в соответствующих облику столицы местах led-экраны.",
        'image': 'news1.jpg',
        'date': '2024-07-16',
        'comments': [
            {'author': 'Аноним', 'text': 'Хорошая новость!', 'is_visible': True},
            {'author': 'Вася', 'text': 'Отлично написано!', 'is_visible': True}
        ]
    },
    {
        'id': 2,
        'title': 'Температурные рекорды. Самым жарким в Бишкеке было 20 июля 2019 года',
        'description': 'Самым жарким в Бишкеке было 20 июля 2019 года. Такие данные приводит ресурс «Погода и климат».'
                        'В тот день в столице зафиксировали +40,1 градуса.'
                        'Самым холодным — 20 июля 1985-го, когда температура составила +11,1 градуса.'
                        'Ресурс «Погода и климат» предоставляет сведения о погоде в разных уголках мира.' 
                        'Температурные рекорды для каждого дня определены как самое низкое и самое высокое значения по ряду данных суточного разрешения.' 
                        'Для мониторинга погоды в Бишкеке суточные сведения взяты с 1936 по 2020 год, а погодных аномалий — с 1898-го.'
                        'Норма среднемесячной температуры июля для столицы составляет +25,5 градуса.'
                        'За все время наблюдений самым теплым был июль 2019 года со средней температурой +28,7 градуса.'
                        'Самым холодным — июль 1898-го со среднемесячной температурой +21,8 градуса.'
                        'Согласно прогнозу синоптиков, 20 июля ночью в Бишкеке без осадков. Воздух прогреется до +22 градусов.'
                        'Днем в столице солнечно и жарко. Температура поднимется до +32 градусов.',
        'image': 'news2.jpg',
        'date': '2024-07-15',
        'comments': [
            {'author': 'Петя', 'text': 'Интересная информация!', 'is_visible': True}
        ]
    }
]

# Функция для отметки комментария как нежелательного
def mark_comment_as_unwanted(news_id, comment_index):
    news[news_id]['comments'][comment_index]['is_visible'] = False

# Главная страница со списком новостей
@app.route('/')
def index():
    return render_template('index.html', news=news)

# Страница с деталями новости и комментариями
@app.route('/news/<int:id>/', methods=['GET', 'POST'])
def news_detail(id):
    # Найти новость по id
    selected_news = None
    for n in news:
        if n['id'] == id:
            selected_news = n
            break
    
    if selected_news:
        if request.method == 'POST':
            author = request.form['author']
            text = request.form['text']
            new_comment = {'author': author, 'text': text, 'is_visible': True}
            selected_news['comments'].append(new_comment)
            return redirect(url_for('news_detail', id=id))
        return render_template('news_detail.html', news=selected_news)
    else:
        return render_template('404.html'), 404

# Маршрут для отметки комментария как нежелательного
@app.route('/news/<int:id>/mark-unwanted/<int:comment_index>/', methods=['POST'])
def mark_unwanted_comment(id, comment_index):
    mark_comment_as_unwanted(id, comment_index)
    return redirect(url_for('news_detail', id=id))

if __name__ == '__main__':
    app.run(debug=True)
