node{
    try{
        stage('Checkout') {
              echo "Create directory for source code"
              sh 'rm code -r && echo "OK" || echo "FAIL"'
              sh "mkdir code"
              dir('code') {
                checkout([$class: 'GitSCM', branches: [
                  [name: "master"]
                ], userRemoteConfigs: [
                  [url: "https://github.com/Inabiel/simple-python-pyinstaller-app-nabil.git"]
                ]])
              }
            }
        stage('Build'){
            dir('code'){
                docker.image('python:2-alpine').inside{
                    sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                }
            }         
        }
        stage('Test'){
            dir('code'){
                docker.image('qnib/pytest').inside{
                    sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
                }
            }        
        }
        stage('Deliver'){
            dir('code'){
                sh "docker run --rm -v '/var/jenkins_home/jobs/submission-cicd-pipeline-nabiel/workspace/code/sources:/src' 'cdrx/pyinstaller-linux:python2' 'pyinstaller -F add2vals.py'"
                sh "ls -la"
            }            
        }
    }
    catch(e){
       stage('Error') {
                echo "${e}"
                deleteDir()
        }
    }
    finally{
        dir('code'){
            sh "ls -la"
            junit 'test-reports/results.xml'
            archiveArtifacts 'sources/dist/add2vals'
            deleteDir()
        }
    }
}