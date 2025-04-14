To run this rag in memory you need to have ollama running and download the model that want. I did this with the follow commands:

```
ollama run gemma3:4
OLLAMA_HOST=0.0.0.0:8080 ollama serve
```

Then you can run the this file `rag-in-memory.ipynb`