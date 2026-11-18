from flask import Flask, request
from prometheus_client import start_http_server, Summary

app = Flask(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Tiempo procesando peticiones')

@app.route('/metrics')
def metrics():
    """
    Endpoint que expone métricas básicas para Prometheus.
    Retorna:
        str: Métrica personalizada en texto plano.
    """
    return "custom_metric 1\n"

@app.route('/hello')
@REQUEST_TIME.time()
def hello():
    """
    Endpoint de saludo al usuario (Contiene vulnerabilidad XSS reflejado intencional).
    Parámetros:
        name (str): Nombre ingresado por parámetro GET.
    Retorna:
        str: Saludo HTML sin sanitizar.
    """
    name = request.args.get('name', 'Invitado')
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000, debug=True)