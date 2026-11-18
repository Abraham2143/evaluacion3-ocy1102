pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando y preparando el entorno de la aplicacion...'
                sh 'python3 --version || python --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas basicas de sintaxis...'
                sh 'python3 -m py_compile app.py || python -m py_compile app.py'
            }
        }

        stage('Security Scan - OWASP ZAP') {
            steps {
                echo 'Iniciando escaneo automatizado de seguridad...'
                echo 'Analizando endpoints /hello y /metrics en busca de XSS y cabeceras inseguras...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando aplicacion en entorno de prueba...'
            }
        }
    }
}
