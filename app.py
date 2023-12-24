from llama_index.llms import Ollama
from flask import Flask, request, jsonify

llm = Ollama(model="mistral:instruct")

app = Flask(__name__)

@app.route('/api')
def health_check():
  return ''

@app.route('/api/generate', methods=['POST'])
def generate():
  question = request.json["text"];
  if (len(question.strip()) < 1):
    return jsonify({ 'error': "The text field shouldn't be empty 😉" }), 400
  
  app.logger.debug('[question]: ' + question)
  try: 
    answer = str(llm.complete(question))
    app.logger.debug('[answer]: ' + answer)

    return jsonify({ 'answer': answer })
  except Exception as ex:
    return jsonify({ 'error': 'Oops... Our AI needs some rest. Please try again later 👨‍🔧' }), 500