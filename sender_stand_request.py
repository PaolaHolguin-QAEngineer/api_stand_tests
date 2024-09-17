from requests import request

import configuration  # Importa las configuraciones (URL y ruta)
import requests  # Importa la librería requests para hacer solicitudes HTTP
import data # importa la base de datos de usuario

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())


def get_users_table():
    return None