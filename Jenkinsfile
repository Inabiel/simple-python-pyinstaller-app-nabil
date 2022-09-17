node{
    try{
        stage('Build'){
            docker.image('python:2-alpine'){
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage('Test'){
            docker.image('qnib/pytest'){
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        }
        stage('Deliver'){
            docker.image('cdrx/pyinstaller-linux:python2'){
                sh 'pyinstaller --onefile sources/add2vals.py'
            }
        }
    }
    catch(e){
        echo(e)
    }
    finally{
    }
}