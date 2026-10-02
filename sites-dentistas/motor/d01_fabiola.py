base = {
  "nome":"Dra. Fabíola Rosvita","nomeCurto":"Fabíola","sobrenome":"Rosvita","selo":"FR",
  "cargo":"Cirurgiã-Dentista · Ortodontia e Implantes",
  "especialidades":"Odontologia Especializada",
  "cidade":"São Bernardo do Campo, SP",
  "instagram":"drafabiolarosvita",
  "whatsapp":"551143311157",
  "whatsMsg":"Olá, Dra. Fabíola. Gostaria de agendar uma avaliação.",
  "cro":"CRO-SP [número]",
  "tema":"claro",
  "paleta":{"bg":"#FFFFFF","surface":"#F1F6F5","raise":"#E6EFEE","deep":"#FFFFFF",
            "ink":"#15302E","muted":"#5E6E6C","accent":"#15817B","fill":"#15817B"},
  "fontes":"moderna","formato":"suave",
  "sobre":{
    "titulo":"Odontologia especializada, com atendimento próximo",
    "textos":[
      "Cirurgiã-dentista em São Bernardo do Campo, com atuação em ortodontia, implantes, próteses e harmonização orofacial. Cada atendimento começa por uma avaliação cuidadosa, com explicação clara do que será feito, dos prazos e das opções disponíveis.",
      "O acompanhamento é pessoal em todas as etapas, em consultório próprio e de fácil acesso, com agenda reservada para cada paciente."
    ],
    "destaques":[
      {"t":"Ortodontia e implantes","d":"Correção do sorriso e reposição de dentes com planejamento."},
      {"t":"Harmonização orofacial","d":"Procedimentos faciais para equilíbrio e autoestima."},
      {"t":"Atendimento humanizado","d":"Acompanhamento pessoal da profissional em cada etapa."}
    ]
  },
  "passandoRotulo":"Em imagens","passandoTitulo":"De perto","passando":"procedimentos",
  "bannersLista":[
    {"linha":"Agende sua","destaque":"avaliação","acao":"whatsapp"},
    {"linha":"Conheça os","destaque":"tratamentos","acao":"#procedimentos"}
  ],
  "retrato":{"titulo":"Como eu trabalho",
    "texto":"Cada plano nasce de uma avaliação individual, pensada para a condição e os objetivos de cada paciente. O acompanhamento é feito pessoalmente em todas as etapas, com orientação clara em cada retorno."},
  "procedimentos":[
    {"id":"orto","nome":"Ortodontia","resumo":"Correção do posicionamento dental e da mordida, com aparelho fixo ou alinhadores.",
     "fotos":[{"src":"","t":"Ortodontia","leg":"Alinhamento em destaque"},{"src":"","t":"Detalhe","leg":"Aparelho"},{"src":"","t":"Resultado","leg":"Sorriso alinhado"}]},
    {"id":"reab","nome":"Implantes e Próteses","resumo":"Reposição de dentes e reabilitação oral para devolver função, saúde e estética.",
     "fotos":[{"src":"","t":"Implantes","leg":"Planejamento do caso"},{"src":"","t":"Reabilitação","leg":"Prótese concluída"},{"src":"","t":"Detalhe","leg":"Acabamento natural"}]},
    {"id":"hof","nome":"Harmonização Orofacial","resumo":"Procedimentos faciais que buscam equilíbrio, naturalidade e mais autoestima.",
     "fotos":[{"src":"","t":"Harmonização","leg":"Avaliação facial"},{"src":"","t":"Resultado","leg":"Equilíbrio e naturalidade"}]},
    {"id":"estetica","nome":"Estética do Sorriso","resumo":"Clareamento, lentes e restaurações estéticas, planejados conforme o rosto e o sorriso.",
     "fotos":[{"src":"","t":"Estética","leg":"Resultado em destaque"},{"src":"","t":"Clareamento","leg":"Sorriso após clareamento"},{"src":"","t":"Lentes","leg":"Resultado com lentes"}]}
  ],
  "duvidas":[
    {"p":"Como funciona o orçamento?","r":"O orçamento sai depois da avaliação, porque depende do que cada caso precisa. Você recebe o plano completo por escrito, com valores e formas de pagamento, e decide com calma."},
    {"p":"Os procedimentos causam dor?","r":"Os procedimentos são feitos com anestesia local quando indicado, o que elimina a dor durante o atendimento. Em tratamentos ortodônticos pode haver sensibilidade nos primeiros dias após cada ajuste, situação esperada e temporária."},
    {"p":"Preciso levar algum exame?","r":"Se você tiver radiografias recentes, recomenda-se trazê-las. Caso contrário, os exames necessários são solicitados durante a avaliação."},
    {"p":"Atende por convênio?","r":"O atendimento é particular, com parcelamento, e alguns convênios podem ser aceitos. A cobertura é confirmada no agendamento."}
  ],
  "convenios":["[Convênio 1]","[Convênio 2]","Particular"],
  "parcelamento":"[X]",
  "local":{"endereco":"[Endereço do consultório], área central de São Bernardo do Campo","horario":"Segunda a sexta, mediante agendamento","agendamento":"Por WhatsApp, com retorno no mesmo dia útil"},
  "imagens":{"capa":"","retrato":"","sobre1":"","sobre2":"","banner1":"","banner2":"","post":""},
  "rodapeNota":"Página de demonstração para apresentação. Os espaços de imagem recebem fotos reais depois; a divulgação de casos clínicos segue a Resolução CFO 196/2019."
}

site_over = {
  "produto":"site","efeitos":False,"nav":"esq","capa":"dividida","banners":"lado",
  "sobreLayout":"faixa","sobreLado":"esq","procLayout":"destaque","faqLayout":"duas",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["banners","sobre","procedimentos","duvidas","local","posts"]
}
link_over = {
  "produto":"link","efeitos":True,"nav":"esq","capa":"limpa","banners":"lado",
  "sobreLayout":"faixa","sobreLado":"esq","procLayout":"cartoes","faqLayout":"centro",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["banners","retrato","procedimentos","passando","duvidas","local","posts"]
}
gen_pair("01-fabiola", base, site_over, link_over, "Dra. Fabíola Rosvita")
