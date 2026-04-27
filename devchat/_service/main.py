from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from devchat._service.config import config
from devchat._service.route import router
from devchat._service.uvicorn_logging import setup_logging

api_app = FastAPI(
    title="DevChat Local Service",
)
# é…�ç½® CORS
api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # å…�è®¸æ‰€æœ‰æº�è¿›è¡Œè·¨åŸŸè¯·æ±‚
    allow_credentials=True,
    allow_methods=["*"],  # å…�è®¸æ‰€æœ‰ HTTP æ–¹æ³•ï¼ˆå¦‚ GETã€�POST ç­‰ï¼‰
    allow_headers=["*"],  # å…�è®¸æ‰€æœ‰è¯·æ±‚å¤´
)

api_app.include_router(router)


# app = socketio.ASGIApp(sio_app, api_app, socketio_path="devchat.socket")

# NOTE: some references if we want to use socketio with FastAPI in the future

# https://www.reddit.com/r/FastAPI/comments/170awhx/mount_socketio_to_fastapi/
# https://github.com/miguelgrinberg/python-socketio/blob/main/examples/server/asgi/fastapi-fiddle.py


def main():
    # Use uvicorn to run the app because gunicorn doesn't support Windows
    pass


if __name__ == "__main__":
    main()
