from app import create_app
from instance import config

if __name__ == "__main__":
    app = create_app(config.DevelopmentConfig)
    app.run()