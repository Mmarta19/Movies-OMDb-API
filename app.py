from flask import Flask, request, Blueprint
import api_config
config = api_config.API_Config()


# function to create basic flask app


def create_app():
    app = Flask(__name__)
    from view.routes import routes
    app.register_blueprint(routes)
    return app


if __name__ == '__main__':

    app = create_app()
    app.run('0.0.0.0', port=config.PORT,
            debug=config.DEBUG)
