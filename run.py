
# run.py

from app import create_app  # Importa la función create_app desde la carpeta app

app = create_app()  # Llama a create_app para inicializar la aplicación

if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicación en modo debug


