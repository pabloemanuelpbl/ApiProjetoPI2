import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

server_port = int(os.getenv('SERVER_PORT'))

if __name__ == "__main__":
    uvicorn.run("application:app", port=server_port, reload=True)