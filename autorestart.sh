while true; do
    if sudo lsof -t -i:80 > /dev/null; then
        echo "El puerto 80 está arriba, no se hace nada."
    else
        echo "El puerto 80 no está arriba, reiniciando el servicio..."
        gunicorn -w 4 -b 0.0.0.0:80 --chdir /home/griferia app:app --access-logfile -
    fi
    sleep 5
done