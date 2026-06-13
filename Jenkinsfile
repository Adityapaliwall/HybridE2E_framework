pipeline {
agent any

```
environment {
    PYTHON_HOME = "C:\\Users\\ADITYA\\AppData\\Local\\Programs\\Python\\Python312"
}

stages {

    stage('Install Dependencies') {
        steps {
            bat '''
            "%PYTHON_HOME%\\python.exe" -m pip install -r requirements.txt
            '''
        }
    }

    stage('Run Tests') {
        steps {
            bat '''
            if exist allure-results rmdir /s /q allure-results
            if exist reports rmdir /s /q reports

            mkdir allure-results
            mkdir reports

            "%PYTHON_HOME%\\python.exe" -m pytest -vs ^
            --html=reports/report.html ^
            --self-contained-html ^
            --alluredir=allure-results
            '''
        }
    }

    stage('Publish HTML Report') {
        steps {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }
    }

    stage('Publish Allure Report') {
        steps {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }

    stage('Archive Artifacts') {
        steps {
            archiveArtifacts artifacts: 'reports/**,allure-results/**,screenshots/**,logs/**',
                             allowEmptyArchive: true,
                             fingerprint: true
        }
    }
}

post {
    success {
        echo 'All Tests Passed Successfully'
    }

    failure {
        echo 'Some Tests Failed'
    }

    always {
        echo 'Pipeline Execution Completed'
    }
}
```

}
