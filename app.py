from flask import Flask, request
from markupsafe import escape
from prometheus_client import start_http_server, Summary

app = Flask(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Tiempo procesando peticiones')

@app.after_request
def add_security_headers(response):
    """
    Inyecta cabeceras de seguridad HTTP en todas las respuestas para mitigar XSS, Clickjacking y fugas de información.
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Permissions-Policy'] = "geolocation=(), microphone=(), camera=()"
    response.headers['Cross-Origin-Embedder-Policy'] = "require-corp"
    response.headers['Cross-Origin-Opener-Policy'] = "same-origin"
    response.headers['Server'] = "SecureServer"
    return response

@app.route('/')
def index():
    """
    Ruta raíz de estado de la aplicación.
    """
    return "<h1>Servicio DevSecOps Operativo</h1>"

@app.route('/metrics')
def metrics():
    """
    Endpoint que expone métricas básicas para Prometheus.
    """
    return "custom_metric 1\n"

@app.route('/hello')
@REQUEST_TIME.time()
def hello():
    """
    Endpoint de saludo seguro al usuario (Vulnerabilidad XSS mitigada).
    """
    name = escape(request.args.get('name', 'Invitado'))
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000, debug=False)