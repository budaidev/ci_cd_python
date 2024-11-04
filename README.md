# Character Counter

A simple and efficient Python utility for counting characters in text files. This project provides both a command-line interface and a containerized solution for character counting operations.

## Features

- Count characters in text files
- Handle various file encodings (UTF-8)
- Robust error handling for missing or invalid files
- Docker support for containerized execution
- CI/CD pipeline with Jenkins
- Comprehensive test coverage

## Installation

### Using Poetry (Recommended)

1. Ensure you have Python 3.9 or later installed
2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Clone the repository:
   ```bash
   git clone <repository-url>
   cd character-counter
   ```
4. Install dependencies:
   ```bash
   poetry install
   ```

### Using Docker

Build the Docker image:
```bash
docker build -t character-counter .
```

## Usage

### Command Line Interface

Count characters in a file:
```bash
# Using Poetry
poetry run charcount path/to/your/file.txt

# After installing the package
charcount path/to/your/file.txt
```

### Docker Container

Run the character counter in a container:
```bash
docker run -v /path/to/local/files:/data character-counter /data/your-file.txt
```

## Development

### Setup Development Environment

1. Install development dependencies:
   ```bash
   poetry install
   ```

2. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Running Tests

```bash
poetry run pytest
```

### Code Quality Checks

Run linting and type checks:
```bash
poetry run black src tests
poetry run isort src tests
poetry run flake8 src tests
poetry run mypy src
```

## CI/CD Pipeline

The project includes a Jenkins pipeline that:
1. Installs dependencies
2. Runs code quality checks
3. Executes tests
4. Builds Docker images
5. Publishes to Nexus repository
6. Deploys to Kubernetes

### Pipeline Configuration

Required Jenkins credentials:
- `nexus-credentials`: Username/password for Nexus repository

Environment variables:
- `NEXUS_URL`: Nexus repository URL
- `DOCKER_REGISTRY`: Docker registry URL

## Project Structure

```
character-counter/
├── src/
│   └── character_counter/
│       ├── __init__.py
│       └── counter.py
├── tests/
│   ├── __init__.py
│   ├── test_counter.py
│   └── test_files/
├── Dockerfile
├── Jenkinsfile
├── pyproject.toml
└── README.md
```

## Troubleshooting

### Common Issues

1. **Permission Denied in Docker**
   - Ensure the mounted volume has correct permissions
   - Run the container with appropriate user permissions

2. **Poetry Installation Issues**
   - Clear poetry cache: `poetry cache clear . --all`
   - Ensure Python version matches project requirements (>=3.9)

3. **Pre-commit Hook Failures**
   - Run `pre-commit clean` to reset the environment
   - Ensure all dependencies are installed: `poetry install`
   - Check mypy type hints and fix any type-related issues

4. **Jenkins Pipeline Failures**
   - Verify Nexus credentials are properly configured
   - Ensure Docker socket is accessible to Jenkins
   - Check workspace permissions for pip and poetry installation

### Type Checking Issues

If you encounter mypy errors:
1. Ensure you're using the correct Python version
2. Check import paths in your code
3. Verify mypy configuration in pre-commit config
4. Run mypy manually to debug: `poetry run mypy src`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and quality checks
5. Submit a pull request

## License

MIT License - see LICENSE file for details
