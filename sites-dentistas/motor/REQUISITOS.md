# Requisitos fixos (projeto sites dentistas)

Padrões que valem para TODAS as dentistas, salvos a pedido do cliente:

1. **Duas versões por dentista**: `link` (bio do Instagram, coluna de celular) e `site` (desktop largo + compatível com celular).
2. **Tema por marca**: claro ou escuro conforme o feed real da dentista (não forçar escuro).
3. **Cada uma genuinamente diferente**: variar paleta, fonte, capa, layout das seções, ordem e movimento. Nunca repetir a mesma diagramação. Manter uma BASE comum (mesmo motor), mas o esqueleto deve mudar.
4. **Animações obrigatórias em todas**:
   - Entrada animada do **nome** no hero (letra a letra / reveal).
   - **Menu do topo** entra animado (obrigatório).
   - Pode variar um pouco de uma para outra, mas sempre presentes.
5. **Sem fugir da vibe dentista** (saúde + estética, elegante, confiável).
6. **Qualidade real**: renderizar e conferir (desktop + celular) antes de publicar; nada feio/sobreposto; contraste legível.
7. **Placeholders marcados** (o que depende da dentista): @ Instagram, endereço, CRO, convênios, WhatsApp e fotos reais.
8. **Entrega final**: salvar todos os arquivos no projeto `mf` e fornecer os links (cada um também é um artifact).

## Matriz de diferenciação (recipe por dentista)
| # | Dentista | @ | Tema | Fonte | Capa | Proc | Sobre | FAQ | Local | Mov |
|---|----------|---|------|-------|------|------|-------|-----|-------|-----|
| 1 | Fabíola Rosvita | drafabiolarosvita | claro petróleo | moderna | dividida | destaque | faixa | duas | cartao | subir |
| 2 | Katia Teixeira | _drakatiateixeira | escuro magenta | elegante | editorial | lista | livre | centro | faixa | lateral |
| 5 | Adriana Siqueira | draadrisiqueira | claro nude/ouro | refinada | editorial | cartoes | pilha | duas | faixa | fade |
| 6 | Mavian | mavianodontologia | claro creme/ouro | classica | letras | destaque | livre | centro | cartao | subir |
| 9 | Gleice Gomes | dra.gleicegomes_ | claro neutro | organica | limpa | lista | faixa | duas | cartao | subir |
| 10 | Amanda Dias | dra.amanda.dias | claro minimal/azul | suave | dividida | cartoes | faixa | centro | faixa | fade |
| 11 | Lidiane Rizzutto | lidianerizzutto | claro sage/madeira | classica | limpa | destaque | pilha | duas | cartao | subir |

(3, 4, 7, 8 pendentes de print)

## Atualizações (regras novas)
- **Seção "Avaliações do Google"**: nota média + estrelas em SVG, total e depoimentos em cartões, botão "Ver todas no Google" (campo `google:{nota,total,url,depoimentos}`). Depoimentos/nota que faltam ficam como placeholder `[Depoimento do Google]`/`[nota]` — nunca inventar avaliação real. Total usa o número real levantado no Google Maps.
- **Avaliações SOMENTE no site, NUNCA no link** (bio).
- **Links externos** (WhatsApp, Instagram, Google, Maps) sempre `target="_blank" rel="noopener noreferrer"`. Âncoras internas permanecem na mesma aba.

- **Efeitos (linhas decorativas da capa)**: usar só nos temas escuros/dourados; evitar nos claros/clean. Vale para o link.

- **Link da bio é enxuto (não é site)**: hero + botões + apresentação + algumas fotos + localização + Instagram. Sem FAQ e sem a lista detalhada de procedimentos. (Aplicado em Mavian, Gleice, Amanda, Lidiane.)
