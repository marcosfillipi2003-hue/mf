# Sites para dentistas — ABC/SP

Duas versões por profissional: **Site** (desktop + celular) e **Links** (página de bio do Instagram).
Cada uma com identidade própria (tema, paleta, fonte, capa, layout e movimento) puxada da vibe real do feed.

Os arquivos finais estão em [`paginas/`](paginas) — é só abrir o `.html` no navegador. O motor que gera tudo está em [`motor/`](motor).

## Links publicados (artifacts)

| # | Dentista | @ | Site | Links (bio) |
|---|----------|---|------|-------------|
| 1 | Dra. Fabíola Rosvita | @drafabiolarosvita | https://claude.ai/artifact/7Ynhbx1PugYEEMDoT2WeAS | https://claude.ai/artifact/HjasNa8A1XaMWeWfQRkAJ7 |
| 2 | Dra. Katia Teixeira | @_drakatiateixeira | https://claude.ai/artifact/52caPsM5erusSPgRkjLKNn | https://claude.ai/artifact/1BJd7Hm2dKuq56aNC1Hx6J |
| 3 | Dra. Adriana Siqueira | @draadrisiqueira | https://claude.ai/artifact/Cdy2zsShsNaJFeMXgvoJQX | https://claude.ai/artifact/75BGL6tQU7DTDHdGmNwQLu |
| 4 | Mavian Odontologia | @mavianodontologia | https://claude.ai/artifact/5uG2doXg3nXF9ZAH2YkgLy | https://claude.ai/artifact/PcwwJjK22ANXgkF86ww6eK |
| 5 | Dra. Gleice Gomes | @dra.gleicegomes_ | https://claude.ai/artifact/MHzkRySehWD7WRiwWGYjNY | https://claude.ai/artifact/RqBVKgwqXN8U4Lv9iU3DWc |
| 6 | Dra. Amanda Dias | @dra.amanda.dias | https://claude.ai/artifact/9hvXQJ8GC18yfjyVMzecJN | https://claude.ai/artifact/YUDbuHf7ngXVeCqM1x2t5d |
| 7 | Dra. Lidiane Rizzutto | @lidianerizzutto | https://claude.ai/artifact/2f26ZAiQSmbk2wsha9dvD7 | https://claude.ai/artifact/3p65HJNnqh8TfVGvn949kK |

## Falta (aguardando prints do Instagram)
- Lumi Odontologia (Santo André)
- Dra. Jéssica Souza (Diadema)
- Clínica Essenza Odontologia (Santo André)

## Ainda é placeholder (depende de cada dentista)
@ do Instagram confirmado, endereço, número do CRO, convênios, número de WhatsApp e **as fotos reais** (hoje há espaços-reservados nos lugares das fotos).

## Como regerar
```
cd motor
python3 gen.py d01_fabiola.py   # gera paginas/01-fabiola-site.html e -link.html
```
Tudo que muda de uma dentista para outra está no bloco `CONFIG` de cada arquivo `dNN_*.py`.
Veja `motor/REQUISITOS.md` para os padrões fixos e a matriz de diferenciação.
