base = {
  "nome":"Mavian Odontologia","nomeCurto":"Mavian","sobrenome":"Odontologia","selo":"M",
  "cargo":"Odontologia Integrada · Saúde e Estética",
  "especialidades":"Odontologia Integrada",
  "cidade":"Diadema, SP",
  "instagram":"mavianodontologia",
  "whatsapp":"5511988997479",
  "whatsMsg":"Olá! Gostaria de agendar uma avaliação na Mavian.",
  "cro":"CRO-SP [número]",
  "tema":"claro",
  "paleta":{"bg":"#FCFAF5","surface":"#F3EEE4","raise":"#E8DFCF","deep":"#FFFFFF",
            "ink":"#201B14","muted":"#786E5E","accent":"#A17E3C","fill":"#8A6B2E"},
  "fontes":"classica","formato":"redondo",
  "sobre":{
    "titulo":"Mais que tratamentos, criamos relações",
    "textos":[
      "Clínica de odontologia integrada em Diadema, que une saúde e estética em um atendimento feito com calma e atenção aos detalhes. A ideia é simples: cuidar de cada paciente como gente, não como um número.",
      "Cada plano começa por uma avaliação completa, com explicação clara das etapas e acompanhamento ao longo de todo o tratamento."
    ],
    "destaques":[
      {"t":"Atendimento acolhedor","d":"Confiança e cuidado em cada detalhe."},
      {"t":"Saúde e estética","d":"Tratamentos que cuidam do sorriso por inteiro."},
      {"t":"Acompanhamento próximo","d":"Perto de você em cada etapa."}
    ]
  },
  "passandoRotulo":"Na clínica","passandoTitulo":"A Mavian de perto","passando":"procedimentos",
  "bannersLista":[
    {"linha":"Agende sua","destaque":"avaliação","acao":"whatsapp"},
    {"linha":"Conheça a","destaque":"clínica","acao":"#procedimentos"}
  ],
  "retrato":{"titulo":"De portas abertas",
    "texto":"Confiança, acolhimento e resultados que transformam vidas. Aqui cada tratamento começa por ouvir você, com um plano pensado para a sua saúde e o seu sorriso."},
  "procedimentos":[
    {"id":"estetica","nome":"Estética do Sorriso","resumo":"Clareamento, lentes e facetas para um sorriso mais harmônico e natural.",
     "fotos":[{"src":"","t":"Estética","leg":"Resultado em destaque"},{"src":"","t":"Detalhe","leg":"Acabamento natural"},{"src":"","t":"Sorriso","leg":"Resultado final"}]},
    {"id":"orto","nome":"Ortodontia","resumo":"Aparelhos e alinhadores para corrigir o posicionamento dos dentes e a mordida.",
     "fotos":[{"src":"","t":"Ortodontia","leg":"Alinhamento em destaque"},{"src":"","t":"Detalhe","leg":"Aparelho"}]},
    {"id":"reab","nome":"Implantes e Próteses","resumo":"Reposição de dentes e reabilitação para devolver função e estética ao sorriso.",
     "fotos":[{"src":"","t":"Implantes","leg":"Planejamento do caso"},{"src":"","t":"Reabilitação","leg":"Resultado concluído"}]},
    {"id":"geral","nome":"Clínica Geral","resumo":"Prevenção, limpeza e restaurações para manter a saúde bucal em dia.",
     "fotos":[{"src":"","t":"Clínica Geral","leg":"Cuidado preventivo"},{"src":"","t":"Detalhe","leg":"Restauração"}]}
  ],
  "duvidas":[
    {"p":"Como é a primeira consulta?","r":"A primeira consulta é de avaliação. Conversamos sobre o que você precisa, examinamos e apresentamos o plano de tratamento, com etapas, prazos e valores, sem compromisso de fechar na hora."},
    {"p":"A clínica atende por convênio?","r":"O atendimento é particular, com parcelamento, e alguns convênios podem ser aceitos. A cobertura é confirmada no agendamento."},
    {"p":"Os tratamentos causam dor?","r":"Os procedimentos são feitos com anestesia local quando indicado. Algum desconforto leve nos primeiros dias é esperado e controlável com a orientação da equipe."},
    {"p":"Vocês atendem crianças?","r":"Sim. A clínica atende diferentes idades, com cuidado e acolhimento também no atendimento infantil."}
  ],
  "convenios":["Particular","[Convênio 1]","[Convênio 2]"],
  "parcelamento":"[X]",
  "local":{"endereco":"[Endereço da clínica], Diadema","horario":"Segunda a sábado, mediante agendamento","agendamento":"Por WhatsApp, com retorno no mesmo dia"},
  "imagens":{"capa":"","retrato":"","sobre1":"","sobre2":"","banner1":"","banner2":"","post":""},
  "rodapeNota":"Demonstração para apresentação. Imagens provisórias nos espaços indicados; casos clínicos conforme a Resolução CFO 196/2019."
}

site_over = {
  "produto":"site","efeitos":False,"nav":"esq","capa":"editorial","banners":"cheio",
  "sobreLayout":"livre","sobreLado":"esq","procLayout":"destaque","faqLayout":"centro",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["sobre","procedimentos","duvidas","local","posts"]
}
link_over = {
  "produto":"link","efeitos":True,"nav":"esq","capa":"limpa","banners":"cheio",
  "sobreLayout":"livre","sobreLado":"esq","procLayout":"cartoes","faqLayout":"centro",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["banners","retrato","procedimentos","passando","duvidas","local","posts"]
}
gen_pair("06-mavian", base, site_over, link_over, "Mavian Odontologia")
