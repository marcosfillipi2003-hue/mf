base = {
  "nome":"Dra. Adriana Siqueira","nomeCurto":"Adriana","sobrenome":"Siqueira","selo":"AS",
  "cargo":"Biomédica e Dentista · Estética",
  "especialidades":"Saúde Integrativa e Estética",
  "cidade":"Diadema, SP",
  "instagram":"draadrisiqueira",
  "whatsapp":"5511973158722",
  "whatsMsg":"Olá, Dra. Adriana. Gostaria de agendar uma avaliação.",
  "cro":"CRO-SP [número] · CRBM [número]",
  "tema":"claro",
  "paleta":{"bg":"#FBF8F3","surface":"#F3ECE2","raise":"#E8DCCD","deep":"#FFFFFF",
            "ink":"#2B2318","muted":"#7C6F5E","accent":"#9C7A35","fill":"#876829"},
  "fontes":"refinada","formato":"suave",
  "sobre":{
    "titulo":"Cuidar da sua saúde de dentro para fora",
    "textos":[
      "Biomédica e dentista, especialista em estética, atendendo em Diadema. Une odontologia, harmonização e bem-estar em um acompanhamento que olha o conjunto, não só o detalhe.",
      "Cada plano começa por uma avaliação individual, com explicação clara de cada etapa e acompanhamento pessoal ao longo do tratamento."
    ],
    "destaques":[
      {"t":"Olhar integrativo","d":"Estética e bem-estar pensados em conjunto."},
      {"t":"Avaliação individual","d":"O plano parte do que você precisa e deseja."},
      {"t":"Acompanhamento pessoal","d":"Da avaliação ao resultado, com a profissional."}
    ]
  },
  "passandoRotulo":"Em imagens","passandoTitulo":"De perto","passando":"procedimentos",
  "bannersLista":[
    {"linha":"Agende sua","destaque":"avaliação","acao":"whatsapp"},
    {"linha":"Conheça os","destaque":"tratamentos","acao":"#procedimentos"}
  ],
  "retrato":{"titulo":"Do meu jeito de cuidar",
    "texto":"Acredito em cuidar da saúde e da estética em conjunto, com um olhar individual para cada paciente. Acompanho cada etapa de perto, com clareza e sem pressa."},
  "procedimentos":[
    {"id":"facial","nome":"Harmonização Facial","resumo":"Procedimentos faciais que buscam equilíbrio e naturalidade, respeitando o seu rosto.",
     "fotos":[{"src":"","t":"Facial","leg":"Avaliação facial"},{"src":"","t":"Resultado","leg":"Equilíbrio e naturalidade"}]},
    {"id":"labios","nome":"Lábios","resumo":"Preenchimento labial com foco em proporção e resultado natural.",
     "fotos":[{"src":"","t":"Lábios","leg":"Antes e depois"},{"src":"","t":"Detalhe","leg":"Contorno natural"}]},
    {"id":"odonto","nome":"Odontologia Estética","resumo":"Clareamento, lentes e cuidado do sorriso, pensados junto com a estética do rosto.",
     "fotos":[{"src":"","t":"Sorriso","leg":"Resultado em destaque"},{"src":"","t":"Detalhe","leg":"Acabamento"}]},
    {"id":"saude","nome":"Saúde Integrativa","resumo":"Acompanhamento de bem-estar para somar saúde, disposição e autoestima.",
     "fotos":[{"src":"","t":"Bem-estar","leg":"Cuidado integrativo"},{"src":"","t":"Avaliação","leg":"Plano individual"}]}
  ],
  "duvidas":[
    {"p":"Como funciona a primeira avaliação?","r":"Na avaliação conversamos sobre seus objetivos e seu histórico, e a partir disso definimos o plano mais indicado, com explicação de cada etapa, prazos e valores."},
    {"p":"Os procedimentos estéticos são seguros?","r":"Sim, quando feitos com avaliação e técnica adequadas. Tudo é explicado antes, incluindo cuidados e expectativas realistas de resultado."},
    {"p":"Como são os valores?","r":"Cada plano é individual, então os valores são passados na avaliação, já com as opções de pagamento. A ideia é você entender tudo antes de decidir."},
    {"p":"Precisa de algum preparo antes?","r":"Depende do procedimento. Na avaliação você recebe todas as orientações de preparo e de cuidados posteriores."}
  ],
  "convenios":["Particular","[Convênio 1]"],
  "parcelamento":"[X]",
  "local":{"endereco":"Rua Rossini, 37 (confirmar), Diadema","horario":"Segunda a sexta, mediante agendamento","agendamento":"Por WhatsApp, com retorno no mesmo dia útil"},
  "google":{"nota":"","total":"45","url":"","depoimentos":[]},
  "imagens":{"capa":"","retrato":"","sobre1":"","sobre2":"","banner1":"","banner2":"","post":""},
  "rodapeNota":"Modelo de apresentação. As imagens são provisórias e a divulgação de resultados segue a Resolução CFO 196/2019, com autorização do paciente."
}

site_over = {
  "produto":"site","efeitos":False,"nav":"esq","capa":"editorial","banners":"lado",
  "sobreLayout":"pilha","sobreLado":"dir","procLayout":"cartoes","faqLayout":"duas",
  "localLayout":"faixa","movimento":"fade",
  "secoes":["sobre","procedimentos","avaliacoes","duvidas","local","posts"]
}
link_over = {
  "produto":"link","efeitos":True,"nav":"esq","capa":"editorial","banners":"lado",
  "sobreLayout":"pilha","sobreLado":"dir","procLayout":"cartoes","faqLayout":"duas",
  "localLayout":"faixa","movimento":"fade",
  "secoes":["banners","retrato","procedimentos","passando","duvidas","local","posts"]
}
gen_pair("05-adriana", base, site_over, link_over, "Dra. Adriana Siqueira")
