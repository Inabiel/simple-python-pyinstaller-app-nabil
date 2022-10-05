node{
    try{
        stage('Checkout') {
                checkout([$class: 'GitSCM', branches: [
                  [name: "master"]
                ], userRemoteConfigs: [
                  [url: "https://github.com/Inabiel/simple-python-pyinstaller-app-nabil.git"]
                ]])
            }
        stage('Build'){ 
                docker.image('python:2-alpine').inside{
                    sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                }
        }
        stage('Test'){
                docker.image('qnib/pytest').inside{
                    sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
                }
        }
        stage('Build Artifact'){
                sh "docker run --rm -v '/var/jenkins_home/workspace/Python App/sources:/src' 'cdrx/pyinstaller-linux:python2' 'pyinstaller -F add2vals.py'"
        }
        stage("Approval"){
            input("Lanjutkan ke tahap Deploy?")
        }
        stage("Deploy"){
                 sh '''
                    ls -la
                    heroku git:remote -a jenkins-python-flask
                    git remote -v
                    git fetch heroku 
                    git fetch origin
                    git branch -a
                    git push heroku HEAD:master --force
                 '''
                 sleep(60)
        }

    }
    catch(e){
       stage('Error') {
                echo "${e}"
        }
    }
    finally{
            sh "ls -la"
            junit 'test-reports/results.xml'
            archiveArtifacts 'sources/dist/add2vals'
    }
}


//I still cannot delete the artifact, any help? :(
