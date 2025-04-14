
from fastapi import FastAPI
from pydantic import BaseModel

from transformers import RobertaForQuestionAnswering, RobertaTokenizer
# Load the model
model = RobertaForQuestionAnswering.from_pretrained(".")

# Load the tokenizer
tokenizer = RobertaTokenizer.from_pretrained(".")


# Definir la aplicación FastAPI
app = FastAPI()

# Modelo de entrada para la API
class QARequest(BaseModel):
    question: str
    context: str

# Ruta de prueba
@app.get("/")
def home():
    return {"message": "API de modelo de BERT para Question Answering"}

# Ruta para hacer predicciones
@app.post("/predict")
def predict(request: QARequest):
    # Usar el pipeline de Hugging Face para responder la pregunta
    inputs=tokenizer(request.question,request.context,return_tensors="pt")
    # Perform inference
    outputs = model(**inputs)
    start_logits = outputs.start_logits
    end_logits = outputs.end_logits

    # Decode the answer
    start_index = start_logits.argmax()
    end_index = end_logits.argmax()
    answer = tokenizer.decode(inputs["input_ids"][0][start_index:end_index+1])
    return {"answer": answer}
