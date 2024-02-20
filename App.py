from backend.application import app
import backend.controllers

if __name__ == '__main__':
    app.run(port=5000, debug=True)
