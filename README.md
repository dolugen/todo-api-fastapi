# Todo API with FastAPI

A toy Todo API implemented using FastAPI.

(VS Code) Currently known issue: If there's some syntax/import error during test setup, VS Code shows error that says `Test result not found [name of test]`. Check back later with new version [vscode-python](https://github.com/microsoft/vscode-python/).

Setup:
```
python -m venv .env
. .env/bin/activate
pip install -r requirements.txt
```

Testing:
```
pytest
```

Build a container image:
```
docker build --tag todo-api .
```

Running in a container (use `--detach` to run in background):
```
docker run --publish 8000:8000 todo-api
```

Create todo item:
```
curl -H "Content-Type: application/json" \
    -X POST http://localhost:8000/ \
    -d '{"id": 1, "title": "just testing"}'
```

