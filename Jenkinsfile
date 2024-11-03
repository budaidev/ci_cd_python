pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        NEXUS_URL = 'http://nexus:8081'
        DOCKER_REGISTRY = 'localhost:8082'
        PYTHONPATH = "${WORKSPACE}/src"
        POETRY_HOME = "/opt/poetry"
        POETRY_VERSION = "1.5.1"
        PATH = "$POETRY_HOME/bin:$PATH"
    }

    stages {
        stage('Setup Poetry') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} POETRY_VERSION=${POETRY_VERSION} python -
                    poetry config virtualenvs.create false
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'poetry install --no-interaction --no-ansi'
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    poetry run black --check src tests
                    poetry run isort --check-only src tests
                    poetry run flake8 src tests
                    poetry run mypy src
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'poetry run pytest'
            }
            post {
                always {
                    junit 'test-results.xml'
                    cobertura coberturaReportFile: 'coverage.xml'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker build -f Dockerfile.api -t ${DOCKER_REGISTRY}/character-counter-api:${BUILD_NUMBER} .
                    docker build -f Dockerfile.worker -t ${DOCKER_REGISTRY}/character-counter-worker:${BUILD_NUMBER} .

                    docker tag ${DOCKER_REGISTRY}/character-counter-api:${BUILD_NUMBER} ${DOCKER_REGISTRY}/character-counter-api:latest
                    docker tag ${DOCKER_REGISTRY}/character-counter-worker:${BUILD_NUMBER} ${DOCKER_REGISTRY}/character-counter-worker:latest
                '''
            }
        }

        stage('Publish') {
            environment {
                NEXUS_CREDS = credentials('nexus-credentials')
            }
            steps {
                sh '''
                    # Build and publish Python package
                    poetry build
                    poetry config repositories.nexus ${NEXUS_URL}/repository/pypi-internal/
                    poetry config http-basic.nexus ${NEXUS_CREDS_USR} ${NEXUS_CREDS_PSW}
                    poetry publish -r nexus

                    # Publish Docker images
                    docker login ${DOCKER_REGISTRY} -u ${NEXUS_CREDS_USR} -p ${NEXUS_CREDS_PSW}
                    docker push ${DOCKER_REGISTRY}/character-counter-api:${BUILD_NUMBER}
                    docker push ${DOCKER_REGISTRY}/character-counter-api:latest
                    docker push ${DOCKER_REGISTRY}/character-counter-worker:${BUILD_NUMBER}
                    docker push ${DOCKER_REGISTRY}/character-counter-worker:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    helm upgrade --install character-counter ./helm/character-counter \
                        --set api.image.tag=${BUILD_NUMBER} \
                        --set worker.image.tag=${BUILD_NUMBER} \
                        --namespace character-counter \
                        --create-namespace
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
