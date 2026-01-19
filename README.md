# rag-production-blueprint
Blueprint de RAG para ambiente crítico: foco em qualidade, custo, rastreabilidade e operação em produção.

# RAG Production Blueprint (Banco/Enterprise)

Blueprint de RAG para ambientes críticos, com foco em:
- Qualidade (redução de hallucination)
- Custo e latência (controle de tokens e fallback)
- Rastreabilidade (fontes citadas)
- Operação (monitoramento, runbook e decisões registradas)

## Contexto
RAG para base de documentos longos e heterogêneos (PDF/Word/texto),
onde respostas imprecisas geram risco e retrabalho.

## Arquitetura (visão geral)
1) Ingestão -> normalização -> extração de texto
2) Chunking (dinâmico por tipo de documento)
3) Embeddings + indexação (vector store)
4) Retrieval (top-k) + re-ranking (quando necessário)
5) Prompt com grounding + citações
6) Guardrails + fallback + monitoramento

## Decisões principais
- Chunking dinâmico por tipo de conteúdo (ver docs/DECISIONS.md)
- Re-ranking apenas acima de um limiar de complexidade/volume
- Limite de contexto para controlar custo/latência
- Resposta sempre com trechos e fontes (rastreabilidade)

## Métricas (LLMOps)
- Latência p50/p95
- Custo estimado por requisição
- Taxa de respostas com fonte
- Qualidade (judge/avaliação offline)
- Falhas por categoria (retrieval, rerank, prompt, modelo)

## Como rodar (MVP)
1) Copie `.env.example` para `.env`
2) Rode ingestão e indexação
3) Suba a API e faça consultas

## Documentação
- Arquitetura: docs/ARCHITECTURE.md
- Decisões: docs/DECISIONS.md
- Avaliação: docs/EVALUATION.md
- Runbook: docs/RUNBOOK.md
- Segurança: docs/SECURITY.md

## Roadmap
- [ ] Dataset de exemplos e avaliação offline
- [ ] Re-ranking opcional e thresholds
- [ ] Observabilidade (logs/metrics/traces)
- [ ] Guardrails e políticas de segurança
