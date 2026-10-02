base = {
  "nome":"Dra. Amanda Dias","nomeCurto":"Amanda","sobrenome":"Dias","selo":"AD",
  "cargo":"Cirurgiã-Dentista · Ortodontista",
  "especialidades":"Especialista em Ortodontia",
  "cidade":"Mauá, SP",
  "instagram":"dra.amanda.dias",
  "whatsapp":"5511974899283",
  "whatsMsg":"Olá, Dra. Amanda. Gostaria de agendar uma avaliação ortodôntica.",
  "cro":"CRO-SP 126311",
  "tema":"claro",
  "paleta":{"bg":"#FBFCFD","surface":"#EEF2F5","raise":"#E0E7EC","deep":"#FFFFFF",
            "ink":"#1E262B","muted":"#64717A","accent":"#5C7E9B","fill":"#3E5F80"},
  "fontes":"suave","formato":"suave",
  "sobre":{
    "titulo":"Ortodontia com planejamento e leveza",
    "textos":[
      "Especialista em ortodontia, atendendo crianças e adultos em Mauá. Trabalho com aparelhos e alinhadores invisíveis, sempre a partir de um planejamento que respeita o tempo de cada caso.",
      "Gosto de deixar tudo claro desde o começo: o que vai ser feito, quanto tempo leva e o que esperar em cada fase. O acompanhamento é de perto, consulta a consulta."
    ],
    "destaques":[
      {"t":"Ortodontia infantil","d":"Acompanhamento do crescimento na hora certa."},
      {"t":"Alinhadores invisíveis","d":"Correção discreta, para a rotina de adultos."},
      {"t":"Planejamento claro","d":"Você sabe cada etapa antes de começar."}
    ]
  },
  "passandoRotulo":"Resultados","passandoTitulo":"Sorrisos em movimento","passando":"procedimentos",
  "bannersLista":[
    {"linha":"Agende sua","destaque":"avaliação","acao":"whatsapp"},
    {"linha":"Conheça os","destaque":"tratamentos","acao":"#procedimentos"}
  ],
  "retrato":{"titulo":"Cada caso no seu tempo",
    "texto":"Ortodontia bem feita respeita o tempo de cada paciente. Planejo o tratamento do início ao fim e acompanho de perto, para você ver o sorriso evoluindo com segurança."},
  "procedimentos":[
    {"id":"aparelho","nome":"Aparelho Ortodôntico","resumo":"Aparelhos fixos para alinhar os dentes e corrigir a mordida, com ajustes periódicos.",
     "fotos":[{"src":"","t":"Aparelho","leg":"Alinhamento em andamento"},{"src":"","t":"Detalhe","leg":"Ajuste do aparelho"}]},
    {"id":"alinhadores","nome":"Alinhadores Invisíveis","resumo":"Placas transparentes e removíveis para corrigir o sorriso de forma discreta.",
     "fotos":[{"src":"","t":"Alinhadores","leg":"Placa transparente"},{"src":"","t":"Planejamento","leg":"Simulação do resultado"}]},
    {"id":"infantil","nome":"Ortodontia Infantil","resumo":"Acompanhamento do crescimento para prevenir e corrigir problemas de mordida cedo.",
     "fotos":[{"src":"","t":"Infantil","leg":"Acompanhamento na infância"},{"src":"","t":"Detalhe","leg":"Avaliação de crescimento"}]},
    {"id":"clareamento","nome":"Clareamento","resumo":"Clareamento dental para finalizar o tratamento com um sorriso mais claro.",
     "fotos":[{"src":"","t":"Clareamento","leg":"Sorriso mais claro"},{"src":"","t":"Detalhe","leg":"Resultado uniforme"}]}
  ],
  "duvidas":[
    {"p":"Qual a melhor idade para a primeira avaliação da criança?","r":"A recomendação é por volta dos 6 ou 7 anos, quando dá para acompanhar o crescimento e identificar cedo o que precisa de atenção. Mas cada caso é avaliado individualmente."},
    {"p":"Alinhadores funcionam igual ao aparelho fixo?","r":"Em muitos casos sim. Na avaliação eu explico se o seu caso é indicado para alinhadores, com as vantagens e os cuidados de usar as placas o tempo recomendado."},
    {"p":"Quanto tempo dura o tratamento?","r":"Varia conforme o caso. Depois da documentação ortodôntica consigo estimar o tempo e o tipo de aparelho mais indicado antes de começar."},
    {"p":"Preciso de encaminhamento para começar?","r":"Não. Você pode agendar direto a avaliação. Se já tiver radiografias recentes, é bom trazer; os exames necessários são solicitados na consulta."}
  ],
  "convenios":["Particular","[Convênio 1]"],
  "parcelamento":"[X]",
  "local":{"endereco":"[Endereço do consultório], Mauá","horario":"Segunda a sexta, mediante agendamento","agendamento":"Por WhatsApp, com retorno no mesmo dia"},
  "google":{"nota":"","total":"58","url":"","depoimentos":[]},
  "imagens":{"capa":"","retrato":"","sobre1":"","sobre2":"","banner1":"","banner2":"","post":""},
  "rodapeNota":"Página de demonstração para apresentação. Os espaços de imagem recebem fotos reais depois; a divulgação de casos clínicos segue a Resolução CFO 196/2019, com autorização do paciente."
}

site_over = {
  "produto":"site","efeitos":False,"nav":"centro","capa":"dividida","banners":"cheio",
  "bannersLista":[{"linha":"Marque sua","destaque":"primeira avaliação","acao":"whatsapp"}],
  "sobreLayout":"faixa","sobreLado":"esq","procLayout":"cartoes","faqLayout":"centro",
  "localLayout":"faixa","movimento":"fade",
  "secoes":["banners","sobre","procedimentos","avaliacoes","duvidas","local","posts"]
}
link_over = {
  "produto":"link","efeitos":True,"nav":"centro","capa":"limpa","banners":"lado",
  "sobreLayout":"faixa","sobreLado":"esq","procLayout":"cartoes","faqLayout":"centro",
  "localLayout":"faixa","movimento":"fade",
  "secoes":["banners","retrato","procedimentos","passando","duvidas","local","posts"]
}
gen_pair("10-amanda", base, site_over, link_over, "Dra. Amanda Dias")
