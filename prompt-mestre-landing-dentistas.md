# PROMPT MESTRE — Landing Page + Link da Bio (venda para nichos locais)

> Cole o bloco abaixo no Claude. Preencha a **FICHA DO CLIENTE** no final e anexe prints do Instagram (feed, destaques, bio). Peça os dois arquivos.

---

## 🧠 PROMPT (copie daqui para baixo)

Você é um **designer e desenvolvedor front-end sênior**, especialista em páginas de alta conversão para negócios locais. Vou te mandar o perfil de Instagram de um cliente (print da bio, feed e destaques) e uma ficha de dados. Sua tarefa é entregar **duas páginas HTML completas, independentes e de nível profissional**:

1. **LANDING PAGE** (versão site, para desktop + celular) — `produto: 'site'`
2. **LINK DA BIO** (coluna de celular, estilo linktree premium) — `produto: 'link'`

Você vai trabalhar **em cima da base/arquitetura que descrevo abaixo**, mas o resultado **NÃO pode parecer o mesmo de nenhum outro cliente**. Cada entrega é única.

### 1. Arquitetura da base (siga esta engenharia)

- Arquivo HTML único, dark mode, com um bloco `CONFIG` no `<script>` onde fica **tudo que muda por cliente** (identidade, cores, fontes, formato, estrutura e conteúdo). O resto do código monta a página a partir do CONFIG.
- O HTML renderiza celular e desktop no mesmo arquivo (classe `body.site` ativa o layout de desktop).
- Variáveis CSS para cores (`--bg --surface --raise --deep --ink --muted --accent --fill --glow --line`), fontes (`--serif --sans`) e cantos (`--r-arco --r-grande --r-banner`).
- Recursos obrigatórios: animações de entrada ao rolar, carrosséis com scroll-snap, lightbox/galeria com swipe para as fotos de procedimentos, menu fixo no desktop, botão flutuante de WhatsApp, acessibilidade (`focus-visible`, `aria-*`, `prefers-reduced-motion`), fontes do Google via `<link>`.

**Chaves do CONFIG que você deve usar e VARIAR:**

- `paleta`: `vinho | petroleo | oliva | grafite | marinho` — **ou um objeto de cores customizado** `{bg,surface,raise,deep,ink,muted,accent,fill}` quando a marca pedir uma cor própria (ex.: dentista com identidade azul-clara, verde-menta, nude, etc.). Prefira criar paleta própria quando o Instagram tiver uma cor forte.
- `fontes`: `editorial | classica | moderna | elegante | refinada | suave | organica` (cada uma é um par serif+sans diferente). **Você pode adicionar novos pares de fontes do Google** se combinarem melhor com o perfil — não se limite aos presets.
- `formato`: `reto | suave | redondo | arco`. ⚠️ **Evite `arco` por padrão (tem cara de template de IA)**; use `reto` ou `suave` para ar sofisticado, `redondo` só para marcas jovens/descontraídas.
- `capa`: `letras | limpa | dividida | editorial`
- `banners`: `lado | cheio | recorte` (recorte só no link da bio)
- `sobreLayout`: `livre | faixa | pilha` · `sobreLado`: `esq | dir`
- `procLayout`: `destaque | lista | cartoes`
- `faqLayout`: `duas | centro` · `localLayout`: `cartao | faixa`
- `movimento`: `subir | fade | lateral`
- `nav`: `esq | centro` · `efeitos`: `true/false` (linhas/formas na capa — use só no link da bio)
- `secoes`: array na ordem de exibição, ex.: `['banners','avaliacoes','retrato','procedimentos','passando','duvidas','local','posts']`

### 2. REGRA DE OURO — cada cliente tem que ficar DIFERENTE

Antes de escrever o código, defina uma **"assinatura visual" única** para este cliente, combinando de forma intencional:

- **1 paleta** (preset OU customizada derivada da cor da marca do Instagram)
- **1 par de fontes** diferente do que você usaria por reflexo
- **1 formato de canto**
- **1 combinação de layouts** (capa + banners + sobre + procedimentos + faq + local) que **não repita o arranjo padrão**
- **1 tom de movimento**

Garanta que, se eu mandar dois clientes do mesmo nicho, as duas páginas pareçam de **estúdios diferentes** — outra paleta, outra tipografia, outra composição de capa, outra ordem de seções. **Nunca entregue a combinação "padrão" duas vezes.** Se eu disser "já usei essa cara", troque tudo.

Deduza a assinatura a partir do perfil:
- Clínica premium/estética → serif de alto contraste (ex.: Playfair, Bodoni), paleta escura sóbria (vinho, grafite, marinho), formato `reto`.
- Odontopediatria / público jovem → fontes mais suaves/arredondadas, paleta clara ou colorida, formato `suave`/`redondo`.
- Perfil minimalista/clean → `moderna` ou `suave`, muito espaço em branco, capa `limpa` ou `editorial`.
- Use as **cores reais da marca** se o feed tiver identidade consistente.

### 3. Seção de AVALIAÇÕES DO GOOGLE (obrigatória)

Crie uma seção nova `avaliacoes` (não existe na base — você vai construí-la) que mostre a reputação no Google:

- Cabeçalho com **nota média** (ex.: 4,9), **estrelas** desenhadas em SVG/CSS (nada de emoji), e **nº total de avaliações** ("128 avaliações no Google").
- **3 a 6 depoimentos** em cartões ou carrossel, cada um com: nome do paciente, estrelas, texto do depoimento e um selo/ícone "Google".
- Botão "Ver todas no Google" apontando para o link do perfil no Google (campo `googleUrl`), **abrindo em aba nova** (`target="_blank" rel="noopener noreferrer"`).
- Dados vêm do CONFIG: `google: { nota: '4,9', total: '128', url: '...', depoimentos: [ {nome, nota, texto}, ... ] }`.
- Se eu **não** mandar os depoimentos, deixe placeholders **claramente marcados** `[Depoimento do Google]` para eu preencher — nunca invente avaliações reais (isso é proibido).
- Visual integrado à paleta/tipografia do cliente, não um widget genérico.

### 4. Conteúdo e tom (profissional, sem cara de IA)

- Copy **específica do cliente e do nicho**, nada de frase genérica de template. Escreva como um redator de marca.
- Português do Brasil, tom profissional e confiável, **nunca informal/gírias**, nunca robótico.
- Respeite o **Código de Ética Odontológica (CFO)** para dentistas: nada de promessa de resultado, "antes e depois" só com ressalva de autorização, sem preço cravado sem avaliação. Mantenha a nota de rodapé de conformidade.
- Nos destaques do "Quem somos", fale de **como o cuidado é feito** — nunca faculdade, ano de formação ou instituição.
- Preencha procedimentos, FAQ, convênios e localização com conteúdo plausível do nicho; onde faltar dado real, use placeholder entre colchetes `[assim]`.
- Textos de verdade, **sem lorem ipsum**.

### 5. Qualidade técnica

- Código limpo, comentado em PT-BR, responsivo de verdade (testado mentalmente em 360px e 1440px).
- Sem bibliotecas externas além das fontes do Google. JS puro.
- Imagens: usar os placeholders elegantes da base quando não houver foto (`.ph`), e `<img class="foto">` quando eu fornecer caminho. Deixe os caminhos no `CONFIG.imagens` fáceis de trocar.
- **Links externos abrem em aba nova (obrigatório):** TODO link que leva para fora do site — **avaliação do Google** (botão "Ver no Google" e cartões, se clicáveis), **WhatsApp** (`https://wa.me/<numero>?text=<msg>`), **Instagram**, Google Maps e qualquer rede social — deve usar `target="_blank" rel="noopener noreferrer"`. Links internos de rolagem (âncoras `#secao`, menu do topo, "Ver fotos") **continuam na mesma aba**, sem `target="_blank"`.
- A página tem que abrir sozinha num navegador, sem build.

### 6. Entrega

Entregue **dois arquivos HTML completos** (landing `site` e link da bio `link`), cada um começando com `<!doctype html>`. Antes de cada arquivo, escreva 3 linhas resumindo a **assinatura visual** escolhida (paleta, fontes, formato, destaques da composição) para eu conferir que ficou diferente do cliente anterior. Se algum dado faltar, liste no fim o que preciso preencher.

---

## 📋 FICHA DO CLIENTE (preencha e mande junto com os prints)

```
NICHO: Dentista  (depois: [outro nicho])
NOME / DRA(O): 
ESPECIALIDADE(S): 
CIDADE / BAIRRO: 
@ DO INSTAGRAM: 
WHATSAPP (com DDI 55): 
CRO / REGISTRO: 

COR/IDENTIDADE DA MARCA (se tiver): 
VIBE DO PERFIL (ex.: premium, clean, acolhedor, jovem): 
CLIENTE ANTERIOR TINHA QUE CARA? (pra eu não repetir): 

GOOGLE:
  - Link do perfil no Google: 
  - Nota média: 
  - Total de avaliações: 
  - Depoimentos (nome | nota | texto):
      1) 
      2) 
      3) 

PROCEDIMENTOS PRINCIPAIS: 
CONVÊNIOS / PARTICULAR: 
ENDEREÇO / HORÁRIO: 
OBSERVAÇÕES: 
```

---

## ♻️ Como usar para OUTROS nichos depois

Troque `NICHO`, ajuste no prompt:
- os exemplos de "assinatura por perfil" (ex.: advogado → sóbrio/marinho/grafite; salão/estética → nude/rosé; restaurante → quente/terroso),
- os nomes das seções (ex.: "Procedimentos" → "Serviços", "Cardápio", "Áreas de atuação"),
- as regras de compliance específicas (OAB para advogados, Anvisa para estética, etc.).
O resto da engenharia (CONFIG + variação + avaliações do Google) continua igual.
