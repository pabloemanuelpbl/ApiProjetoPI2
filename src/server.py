import os
import uvicorn
from dotenv import load_dotenv
from application import app

load_dotenv()

server_port = int(os.getenv('SERVER_PORT'))

if __name__ == "__main__":
    uvicorn.run(app, port=server_port)