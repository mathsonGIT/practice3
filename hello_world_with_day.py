from flask import Flask
from datetime import datetime
import os


weekdays = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга', 'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')

def html_wrapper(text):
    html = f'''
        <div style="text-align: center;">
        <h1>{text}</h1>
        </div>
    '''
    return html

app = Flask(__name__)


@app.route('/hello-world/<string:name>')
def hello_function(name):
    weekday_string = weekdays[datetime.today().weekday()]
    html = html_wrapper(f'Привет, {name}. {weekday_string}')
    return html

if __name__ == '__main__':
    app.run(debug=True)