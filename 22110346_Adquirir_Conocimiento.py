import json

# Archivo donde se guardará la base de conocimientos del chatbot
DATA_FILE = "knowledge_base.json"

# Intentar cargar la base de conocimientos desde un archivo JSON existente
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        knowledge_base = json.load(f)  # Se carga el diccionario con preguntas y respuestas guardadas
except FileNotFoundError:
    # Si el archivo no existe, se crea una base de conocimientos predeterminada
    knowledge_base = {
        "hola": "Hola! ¿Cómo estás?",
        "cómo estás?": "Estoy bien, gracias por preguntar. ¿Y tú?",
        "de qué te gustaría hablar?": "Puedo hablar de lo que quieras. Pregunta lo que desees.",
    }

# Respuesta predeterminada cuando el chatbot no conoce la respuesta
default_response = "No sé la respuesta a eso. ¿Puedes enseñarme qué debería responder?"

# Función para guardar nuevas respuestas en el archivo JSON
def save_knowledge():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, indent=4, ensure_ascii=False)  # Se guarda el diccionario en el archivo

# Función principal para la interacción con el chatbot
def chatbot():
    print("Bienvenido al Chatbot. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ").strip().lower()  # Se obtiene la entrada del usuario en minúsculas y sin espacios extra
        
        if user_input == "salir":  # Si el usuario escribe 'salir', termina la conversación
            print("Chatbot: ¡Hasta luego!")
            break
        
        if user_input in knowledge_base:  # Si la pregunta está en la base de conocimientos, se responde directamente
            print(f"Chatbot: {knowledge_base[user_input]}")
        else:
            # Si el chatbot no conoce la respuesta, pide que el usuario la enseñe
            print("Chatbot: No sé la respuesta a eso. ¿Puedes enseñarme qué debería responder?")
            new_response = input("Escribe la respuesta que debería aprender o 'no' para omitir: ").strip()
            
            if new_response.lower() != "no":  # Si el usuario ingresa una nueva respuesta, se guarda en la base de datos
                knowledge_base[user_input] = new_response
                save_knowledge()
                print("Chatbot: ¡Gracias! Ahora lo recordaré.")

# Ejecutar el chatbot si el script se ejecuta directamente
if __name__ == "__main__":
    chatbot()
