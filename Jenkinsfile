node{
    try{
        stage('Build'){
            sh(script:'ls -la', returnStdout:true).trim()
            docker.image('python:2-alpine').inside{
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage('Test'){
            docker.image('qnib/pytest').inside{
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        }
        stage('Deliver'){
            docker.image('cdrx/pyinstaller-linux:python2').inside{
                sh 'pyinstaller --onefile sources/add2vals.py'
            }
        }
    }
    catch(e){
        echo(e)
    }
    finally{
        junit 'test-reports/results.xml'
        archiveArtifacts 'dist/add2vals'
    }
}