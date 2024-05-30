#!/bin/bash

# Matar proceso en el puerto 80
sudo lsof -t -i:80 | sudo xargs kill

# Iniciar gunicorn
gunicorn -w 4 -b 0.0.0.0:80 --chdir /home/griferia app:app --access-logfile -