pipeline {
  agent any
  options { timestamps(); ansiColor('xterm') }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build image') {
      steps {
        sh 'docker build -t allure-demo .'
      }
    }
    stage('Run tests') {
      steps {
        sh 'rm -rf allure-results || true && mkdir -p allure-results'
        sh 'docker run --rm -v "$PWD/allure-results":/app/allure-results allure-demo'
        sh 'ls -l allure-results || true'
      }
    }
  }
  post {
    always {
      allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
    }
  }
}
