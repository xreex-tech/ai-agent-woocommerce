
# AI Agent WooCommerce

Esempio di agente AI esterno con FastAPI che utilizza OpenAI e le API REST di WooCommerce.

## Setup

1. Copia `.env.example` in `.env` e inserisci le tue chiavi API.
2. Installa le dipendenze:

```
pip install -r requirements.txt
```

3. Avvia il server:

```
uvicorn main:app --reload
```

4. Usa l'endpoint POST `/generate-description/` per generare descrizioni prodotti.

## Deploy su Render.com

Segui la guida nel README per collegare questa repo a Render.com e configurare le variabili d'ambiente.
