# Decisões (ADR-lite)

## D1 — Re-ranking condicional
**Contexto:** Re-ranking melhora precisão, mas aumenta custo/latência.  
**Decisão:** Aplicar re-ranking apenas quando:
- base grande ou
- baixa confiança do retrieval ou
- consulta “complexa”.
**Consequências:** Melhor qualidade com custo controlado.

## D2 — Chunking dinâmico
**Contexto:** Documentos variam (normativos vs narrativos).  
**Decisão:** Chunk menor para textos normativos; maior para narrativos.
**Consequências:** Melhor grounding e menos ruído.
