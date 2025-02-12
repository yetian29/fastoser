import uvicorn
from fastapi import FastAPI

from src.app.presentation.rest.v1.router import router as rest_router


def init_app() -> FastAPI:
    app = FastAPI(debug=True, title="Fastoser", docs_url="/api/v1/docs")
    app.include_router(rest_router)
    return app


if __name__ == "__main__":
    config = uvicorn.Config(init_app, port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
