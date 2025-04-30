from api import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(host=os.getenv("HOST", default="127.0.0.1"), port=5000, debug=True)
    