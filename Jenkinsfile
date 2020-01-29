pipeline {
    agent any
    parameters {
        string(name: 'BadGitHash',
          defaultValue: '--Required--',
          description: 'A known bad Hash')
        string(name: 'GoodGitHash',
          defaultValue: '--Required--',
          description: 'A known good Hash')
        string(name: 'CommandToRun',
          defaultValue: '--Required--',
          description: 'The CMD to run to Verify Success/Failure')
    }

    stages {
        stage('Initialize Git Bisect') {
            steps {
                git bisect start
                git bisect good "${params.GoodGitHash}"
                git bisect bad "${params.BadGitHash}"
            }
        }
        stage('Run CMD') {
            steps {
                git bisect run "${params.CommandToRun}"
            }
        }
    }
}
