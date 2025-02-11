import uvicorn
from fastapi import FastAPI


def init_app():
    app = FastAPI(debug=True, title="Fastoser")
    return app


if __name__ == "__main__":
    config = uvicorn.Config(init_app, port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
