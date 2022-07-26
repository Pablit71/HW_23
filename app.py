import os

from flask import Flask, request
from flask_restx import abort

from func import func_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST', 'GET'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    cmd_1 = request.args.get('cmd_1')
    value_1 = request.args.get('value_1')
    cmd_2 = request.args.get('cmd_1')
    value_2 = request.args.get('value_1')
    file_name = request.args.get('file_name')

    if not (cmd_1 and value_1) and (cmd_2 and value_2):
        abort(400)

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, "ошибка с файлом")

    with open(file_path) as file:
        res = func_query(cmd_1, value_1, file)
        res = '\n'.join(res)
        if cmd_2 and value_2:
            res = func_query(cmd_2, value_2, res)
        print(res)

    return app.response_class(res, content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
