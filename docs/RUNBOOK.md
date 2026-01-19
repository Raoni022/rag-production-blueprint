# Runbook

## Alarmes comuns
- Latência p95 acima de X
- Aumento de custo por request
- Queda na taxa de respostas com fonte
- Aumento de “não encontrei evidência no contexto”

## Diagnóstico rápido
1) Verificar volume e tipo de consulta
2) Checar retrieval top-k e similaridade
3) Checar chunking do documento
4) Checar re-ranking e thresholds
5) Checar prompt e limite de contexto

## Mitigação
- Ativar fallback para modelo menor
- Diminuir top-k / contexto
- Ajustar chunking por tipo de documento
