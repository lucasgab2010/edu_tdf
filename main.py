import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

# Ruta del archivo JSON
file_path = os.path.join(os.path.dirname(__file__), "edu.json")

# Cargar el archivo JSON una vez al iniciar el servidor
try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"El archivo {file_path} no se encontró.")
    data = {}

# Variables globales para el estado de la conversación
current_intelligence_index = 0
current_question_index = 0

@app.get("/", response_class=HTMLResponse)
async def get_chat_interface():
    # Cargar el archivo HTML para la interfaz
    html_file_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    with open(html_file_path, "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

@app.get("/entries")
async def get_entries():
    try:
        # Devuelve la lista de entries
        return {"entries": data.get("entries", [])}
    except Exception as e:
        print("Error al leer el archivo JSON:", str(e))
        raise HTTPException(status_code=500, detail="Error al cargar los datos.")

@app.post("/chat")
async def chat(user_response: str):
    global current_intelligence_index, current_question_index

    try:
        # Obtener la inteligencia y las preguntas actuales
        intelligence = data["entries"][current_intelligence_index]
        props = intelligence["props"]

        # Mensaje de respuesta inicial
        response_message = ""

        # Manejo de respuesta "No"
        if user_response.lower() == "no":
            if current_question_index == len(props) - 1:
                # Si es la última pregunta y responde "No", mostrar description_no y reiniciar
                response_message = f"Recomendación para {intelligence['name']}: {intelligence['description_no']}"
                current_intelligence_index = 0
                current_question_index = 0
                return {"message": response_message + " Reiniciando el proceso."}
            else:
                # Avanzar a la siguiente pregunta si no es la última
                current_question_index += 1
                return {"message": props[current_question_index]}

        # Manejo de respuesta "Sí"
        elif user_response.lower() == "sí":
            current_question_index += 1
            if current_question_index < len(props):
                return {"message": props[current_question_index]}
            else:
                # Confirmación de afinidad si responde "Sí" a todas las preguntas
                response_message = f"¡Felicitaciones! Parece que tienes afinidad con {intelligence['name']}: {intelligence['description']}"
                current_intelligence_index = 0
                current_question_index = 0
                return {"message": response_message}

        else:
            return {"message": "Por favor, responde 'Sí' o 'No'."}

    except Exception as e:
        print("Error en la conversación:", str(e))
        raise HTTPException(status_code=500, detail="Error en el procesamiento de la conversación.")
