![politec](https://github.com/lucasgab2010/edu_tdf/raw/main/img/poli.jpg)


---

# Sistema Experto para Elección de Estudios Superiores en Tierra del Fuego

**Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial**  
**Politécnico Malvinas Argentinas**  
**Desarrollo de Sistemas de IA**  
**Año: 2024**

**Profesor**: Martin Mirabete  
**Alumno**: Gabriel García

---
[Descargar video](https://github.com/lucasgab2010/edu_tdf/video/sp_gg.mp4?raw=true)
---

## Descripción del Proyecto

Este proyecto tiene como objetivo el desarrollo de un **Sistema Experto de Orientación Vocacional** dirigido a estudiantes de secundaria en la **Provincia de Tierra del Fuego**. Muchos estudiantes enfrentan dificultades al elegir una carrera terciaria o universitaria debido a la falta de información sobre las opciones académicas disponibles o la incapacidad para identificar las carreras que mejor se alinean con sus intereses y habilidades.

El sistema experto propone una solución a este problema proporcionando **orientación académica personalizada**. Se basa en las ocho **inteligencias múltiples** propuestas por el Dr. **Howard Gardner**:

1. Lingüística
2. Lógica-matemática
3. Espacial
4. Corporal
5. Musical
6. Interpersonal
7. Intrapersonal
8. Naturalista

El sistema captura el perfil cognitivo y los intereses de los estudiantes a través de un cuestionario y, con base en sus respuestas, sugiere las carreras más adecuadas. A través de una **plataforma web**, los estudiantes podrán acceder al sistema y recibir recomendaciones precisas que consideren tanto sus habilidades como las oportunidades educativas y laborales disponibles en Tierra del Fuego.

## Relevancia del Proyecto

Este proyecto es relevante porque aborda directamente la **problemática educativa local**. En Tierra del Fuego, los estudiantes secundarios, especialmente los de último año, a menudo no saben qué carrera elegir debido a la falta de información adecuada sobre las opciones disponibles. Esto puede llevar a decisiones poco informadas y, en algunos casos, a la deserción académica.

Con este sistema, no solo se facilita una **elección académica más informada**, sino que también se contribuye a fortalecer el vínculo entre las habilidades de los estudiantes y las oportunidades profesionales disponibles en la región. Además, al alinear las habilidades de los jóvenes con las necesidades del mercado local, se promueve una mayor **satisfacción académica** y **desarrollo económico** en la provincia.

## Objetivos del Proyecto

El objetivo principal de este proyecto es desarrollar un **sistema experto** que ayude a los estudiantes de secundaria a elegir una carrera terciaria o universitaria. El sistema proporcionará recomendaciones personalizadas basadas en los intereses, habilidades y estilo de aprendizaje de cada estudiante, y tomará en cuenta las oportunidades educativas y laborales locales.

---

## Instalación del Sistema Experto (FastAPI)

Para ejecutar el **Sistema Experto** en tu máquina local, sigue estos pasos:

### 1. Abrir el Símbolo del Sistema como Administrador
- Abre el **Símbolo del Sistema** en modo administrador.

### 2. Navegar a la Carpeta del Proyecto
- Dirígete a la carpeta donde descargaste el repositorio desde GitHub:

  ```bash
  cd C:\Users\Downloads\Edu
  ```

### 3. Crear un Entorno Virtual
- Ejecuta el siguiente comando para crear un entorno virtual:

  ```bash
  python -m venv fastapi-env
  ```

  > **Nota**: Si el comando no se reconoce, asegúrate de tener **Git** instalado desde [aquí](https://git-scm.com/downloads/win).

### 4. Activar el Entorno Virtual
- Activa el entorno virtual con el siguiente comando:

  ```bash
  env\Scripts\activate
  ```

  > Verás que el prompt cambia y ahora tendrás algo como esto:

  ```bash
  (env) C:\Users\Downloads\Edu>
  ```

### 5. Instalar Dependencias
- Para instalar **FastAPI** y **Uvicorn**, ejecuta los siguientes comandos:

  ```bash
  pip install "fastapi[standard]"
  pip install "uvicorn[standard]"
  ```

### 6. Abrir el Proyecto en Visual Studio Code
- Abre **VSCode** y selecciona la carpeta **"Edu"** que contiene el archivo `main.py`.

### 7. Levantar el Servidor
- Abre la terminal de **VSCode** y ejecuta los siguientes comandos:

  ```bash
  env\Scripts\activate
  uvicorn main:app --reload
  ```

### 8. Acceder al Sistema
- Una vez que el servidor esté en funcionamiento, abre tu navegador y accede a la siguiente dirección:

  ```
  http://localhost:8000/
  ```

  > Si la base de conocimiento no está cargada, presiona **F5** o abre una nueva pestaña con la misma URL.

---

Si tienes alguna duda o necesitas ayuda adicional, no dudes en consultar la documentación oficial de [FastAPI](https://fastapi.tiangolo.com) o contactar al equipo del proyecto.

---

# Sistema Experto en Python con FastAPI

## Instalación

Para instalar las dependencias necesarias, se recomienda usar **pipenv**:

```bash
pipenv install
```

## Ejecución

Para ejecutar el proyecto, utiliza el siguiente comando:

```bash
pipenv run main.py
```

## Explicación de la Implementación con FastAPI

### 1. Creación de la Aplicación

La aplicación se crea con la siguiente línea de código:

```python
app = FastAPI()
```

Esto genera una instancia de **FastAPI**, que será la base para gestionar las solicitudes HTTP y las rutas de la aplicación web.

### 2. Definición de Rutas y Modelos

**FastAPI** permite definir rutas para manejar solicitudes HTTP. En este sistema experto, se definen dos rutas principales:

- `@app.get("/")`: Ruta para la solicitud GET en la raíz del sistema, que devuelve el archivo HTML con la interfaz del chatbot.
  
- `@app.post("/next-question")`: Ruta POST que maneja las respuestas del usuario y avanza al siguiente síntoma. Esta ruta utiliza el modelo `UserResponse`, definido con **Pydantic** (`BaseModel`), para asegurar que las respuestas del usuario tengan la estructura correcta.

### 3. Manejo de la Lógica de Inferencia

FastAPI maneja las solicitudes a través de funciones vinculadas a las rutas. La lógica de inferencia se implementa en la función `next_question`, que usa el **estado global** (`user_state`) para almacenar el progreso del usuario. Esto permite que el chatbot avance secuencialmente por cada síntoma y entrada en la base de conocimiento.

### 4. Respuesta en Formato JSON

FastAPI convierte automáticamente los diccionarios devueltos, como `{"edu": edu}` o `{"question": next_question}`, en respuestas JSON. Esto facilita la interacción entre el **frontend** y el **backend**.

## Descripción del Sistema de Inferencia


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.



Este código implementa un sistema de inferencia secuencial, en el cual se ejecuta un motor de preguntas basado en una lista de carreras predefinida. El sistema avanza por cada carrera y, cuando se cumplen todos los requisitos de la inteligencia de una entrada en la base de conocimiento, ofrece una carrera.

---
