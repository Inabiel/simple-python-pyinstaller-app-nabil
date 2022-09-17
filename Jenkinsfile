node{
    try{
        stage('Build').inside{
            docker.image('python:2-alpine'){
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage('Test').inside{
            docker.image('qnib/pytest'){
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        }
        stage('Deliver').inside{
            docker.image('cdrx/pyinstaller-linux:python2'){
                sh 'pyinstaller --onefile sources/add2vals.py'
            }
        }
    }
    catch(e){
        echo(e)
    }
    finally{
        sh "ls"
        junit 'test-reports/results.xml'
        archiveArtifacts 'dist/add2vals'
    }
}