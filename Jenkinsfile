pipeline {
  agent any
  options { timestamps() }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build image') {
      steps {
        bat 'docker build -t allure-demo .'
      }
    }
    stage('Run tests') {
      steps {
        bat '''
          if exist allure-results rmdir /s /q allure-results
          mkdir allure-results
          docker run --rm -v "%cd%\\allure-results":/app/allure-results allure-demo
          dir allure-results
        '''
      }
    }
  }
  post {
    always {
      allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
    }
  }
}
