base = {
  "nome":"Dra. Lidiane Rizzutto","nomeCurto":"Lidiane","sobrenome":"Rizzutto","selo":"LR",
  "cargo":"Cirurgiã-Dentista · Implantodontia",
  "especialidades":"Implantes e Harmonização",
  "cidade":"Santo André, SP",
  "instagram":"lidianerizzutto",
  "whatsapp":"5511974766300",
  "whatsMsg":"Olá, Dra. Lidiane. Gostaria de agendar uma avaliação.",
  "cro":"CRO-SP 116258",
  "tema":"claro",
  "paleta":{"bg":"#FAFAF6","surface":"#EEF0E8","raise":"#E0E4D7","deep":"#FFFFFF",
            "ink":"#232620","muted":"#696E5E","accent":"#79876A","fill":"#566348"},
  "fontes":"editorial","formato":"suave",
  "sobre":{
    "titulo":"Reabilitar o sorriso com segurança e naturalidade",
    "textos":[
      "Cirurgiã-dentista em Santo André, com atuação em implantodontia e harmonização orofacial. Cada reabilitação começa por um estudo cuidadoso do caso, com exames de imagem e um plano pensado para devolver função e estética.",
      "O atendimento acontece em consultório próprio, com agenda reservada e acompanhamento da profissional em cada etapa do tratamento."
    ],
    "destaques":[
      {"t":"Implantodontia","d":"Reposição de dentes com planejamento por imagem."},
      {"t":"Harmonização orofacial","d":"Equilíbrio do rosto com naturalidade."},
      {"t":"Consultório próprio","d":"Estrutura reservada e atendimento individual."}
    ]
  },
  "passandoRotulo":"No consultório","passandoTitulo":"Um pouco de perto","passando":"procedimentos",
  "bannersLista":[
    {"linha":"Agende sua","destaque":"avaliação","acao":"whatsapp"},
    {"linha":"Conheça os","destaque":"tratamentos","acao":"#procedimentos"}
  ],
  "retrato":{"titulo":"Estudo antes de agir",
    "texto":"Cada reabilitação começa por entender o caso a fundo, com exames e planejamento. Prefiro explicar tudo com clareza e acompanhar pessoalmente cada etapa até o resultado."},
  "procedimentos":[
    {"id":"implantes","nome":"Implantes","resumo":"Reposição de dentes perdidos com planejamento por imagem e acompanhamento do caso.",
     "fotos":[{"src":"","t":"Implantes","leg":"Planejamento do caso"},{"src":"","t":"Resultado","leg":"Reabilitação concluída"},{"src":"","t":"Detalhe","leg":"Acabamento natural"}]},
    {"id":"proteses","nome":"Próteses","resumo":"Próteses fixas e sobre implante para devolver mastigação, fala e estética.",
     "fotos":[{"src":"","t":"Próteses","leg":"Prótese sobre implante"},{"src":"","t":"Detalhe","leg":"Ajuste e acabamento"}]},
    {"id":"hof","nome":"Harmonização Orofacial","resumo":"Procedimentos faciais que buscam equilíbrio e naturalidade, respeitando o seu rosto.",
     "fotos":[{"src":"","t":"Harmonização","leg":"Avaliação facial"},{"src":"","t":"Resultado","leg":"Equilíbrio e naturalidade"}]}
  ],
  "duvidas":[
    {"p":"O implante é um procedimento demorado?","r":"O tratamento tem etapas e o tempo total depende do caso. O planejamento por imagem, feito no início, permite estimar prazos e explicar cada fase antes de começar."},
    {"p":"Coloca o dente no mesmo dia?","r":"Em alguns casos é possível, dependendo da condição do osso e da avaliação. Isso é definido após os exames, com segurança, e explicado na consulta."},
    {"p":"Como funciona a avaliação inicial?","r":"Na avaliação examinamos o caso e, quando necessário, solicitamos exames de imagem. A partir disso você recebe o plano com etapas, prazos e valores."},
    {"p":"Preciso trazer exames?","r":"Se tiver tomografias ou radiografias recentes, ajuda bastante. Caso contrário, orientamos os exames necessários durante a avaliação."}
  ],
  "convenios":["Particular","[Convênio 1]"],
  "parcelamento":"[X]",
  "local":{"endereco":"Rua Gonçalo Fernandes, 318, sala 601, Jardim Bela Vista, Santo André","horario":"Segunda a sexta, mediante agendamento","agendamento":"Por WhatsApp, com retorno no mesmo dia útil"},
  "google":{"nota":"","total":"37","url":"","depoimentos":[]},
  "imagens":{"capa":"","retrato":"","sobre1":"","sobre2":"","banner1":"","banner2":"","post":""},
  "rodapeNota":"Material de demonstração para apresentação. As imagens são provisórias; a divulgação de casos clínicos segue a Resolução CFO 196/2019, com autorização do paciente."
}

site_over = {
  "produto":"site","efeitos":False,"nav":"esq","capa":"dividida","banners":"lado",
  "bannersLista":[{"linha":"Agende sua","destaque":"avaliação","acao":"whatsapp"}],
  "sobreLayout":"pilha","sobreLado":"esq","procLayout":"destaque","faqLayout":"duas",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["banners","sobre","procedimentos","avaliacoes","duvidas","local","posts"]
}
link_over = {
  "produto":"link","efeitos":False,"nav":"esq","capa":"limpa","banners":"lado",
  "sobreLayout":"pilha","sobreLado":"esq","procLayout":"cartoes","faqLayout":"duas",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["banners","retrato","procedimentos","passando","duvidas","local","posts"]
}
gen_pair("11-lidiane", base, site_over, link_over, "Dra. Lidiane Rizzutto")
