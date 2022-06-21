import os

secret_key = (
    os.environ["FLASK_SECRET_KEY"] if "FLASK_SECRET_KEY" in os.environ else "secret"
)