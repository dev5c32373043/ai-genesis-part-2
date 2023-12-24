# 🤖 The first shot in the leg with an AI (Llama Index, Ollama, Mistral)

This project serves as a basic HTTP service facilitating communication with the Mistral AI model. The `/api/generate` endpoint is available via [POST] and accepts a JSON body containing a 'text' field. Submitting data to this endpoint prompts the Mistral AI model to generate a response based on the provided input.

## 🚀 Getting started

To start the project install all dependencies in the requirements section.

Then download `mistral:instruct` model:

```bash
ollama pull mistral:instruct
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

And finally start the dev server:

```bash
flask run --debug
```

## Requirements

- [Python][python] 3.8.10+
- [Ollama][ollama] 0.2.17+

[python]: https://www.python.org/
[ollama]: https://ollama.ai/
