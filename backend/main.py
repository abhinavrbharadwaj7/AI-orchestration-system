from fastapi import FastAPI

from backend.api.routes import router


APP_TITLE = "Simple AI Orchestrator"
APP_VERSION = "0.1.0"

app = FastAPI(title=APP_TITLE, version=APP_VERSION)
app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "ok", "service": APP_TITLE}

