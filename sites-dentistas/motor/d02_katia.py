base = {
  "nome":"Dra. Katia Teixeira","nomeCurto":"Katia","sobrenome":"Teixeira","selo":"KT",
  "cargo":"Cirurgiã-Dentista · Estética do Sorriso",
  "especialidades":"Odontologia Estética e Lentes",
  "cidade":"Mauá, SP",
  "instagram":"_drakatiateixeira",
  "whatsapp":"5511949192010",
  "whatsMsg":"Olá, Dra. Katia. Gostaria de agendar uma avaliação.",
  "cro":"CRO-SP [número]",
  "tema":"escuro",
  "paleta":{"bg":"#1C0E17","surface":"#271320","raise":"#341A2B","deep":"#120810",
            "ink":"#FBEFF5","muted":"#CBA7BA","accent":"#F2779F","fill":"#C23E72"},
  "fontes":"elegante","formato":"suave",
  "sobre":{
    "titulo":"Um sorriso que combina com você",
    "textos":[
      "Cirurgiã-dentista em Mauá, com foco em estética do sorriso e lentes de resina. Cada tratamento parte de uma conversa sobre o que você quer mudar, com um plano desenhado para o seu rosto e o seu jeito.",
      "O atendimento é próximo e sem pressa, do planejamento ao resultado, com acompanhamento em cada etapa."
    ],
    "destaques":[
      {"t":"Projeto do sorriso","d":"Planejamento feito para o seu rosto, antes de começar."},
      {"t":"Lentes de resina","d":"Mais harmonia e autoestima, com naturalidade."},
      {"t":"Atendimento próximo","d":"Acompanhamento pessoal do começo ao fim."}
    ]
  },
  "passandoRotulo":"Antes e depois","passandoTitulo":"Resultados de perto","passando":"procedimentos",
  "bannersLista":[
    {"linha":"Quero meu","destaque":"sorriso novo","acao":"whatsapp"},
    {"linha":"Veja os","destaque":"resultados","acao":"#procedimentos"}
  ],
  "retrato":{"titulo":"Do seu jeito",
    "texto":"Cada sorriso é planejado a partir do que você quer mudar, com naturalidade e harmonia. Acompanho você pessoalmente em cada etapa, até o resultado que a gente combinou."},
  "procedimentos":[
    {"id":"lentes","nome":"Lentes de Resina","resumo":"Facetas em resina para corrigir forma, cor e espaços, com resultado natural.",
     "fotos":[{"src":"","t":"Lentes","leg":"Antes e depois"},{"src":"","t":"Detalhe","leg":"Acabamento natural"},{"src":"","t":"Sorriso","leg":"Resultado final"}]},
    {"id":"clareamento","nome":"Clareamento","resumo":"Clareamento dental para um sorriso mais claro, com acompanhamento profissional.",
     "fotos":[{"src":"","t":"Clareamento","leg":"Sorriso mais claro"},{"src":"","t":"Detalhe","leg":"Resultado uniforme"}]},
    {"id":"harmonia","nome":"Harmonia do Sorriso","resumo":"Pequenos ajustes que equilibram o sorriso e valorizam o seu rosto.",
     "fotos":[{"src":"","t":"Harmonia","leg":"Equilíbrio do sorriso"},{"src":"","t":"Resultado","leg":"Mais autoestima"}]},
    {"id":"geral","nome":"Odontologia Geral","resumo":"Cuidado preventivo e restaurador para manter a saúde do sorriso em dia.",
     "fotos":[{"src":"","t":"Odontologia","leg":"Cuidado preventivo"},{"src":"","t":"Detalhe","leg":"Restauração"}]}
  ],
  "duvidas":[
    {"p":"As lentes de resina ficam naturais?","r":"Sim. As lentes são planejadas conforme o seu rosto e o formato dos seus dentes, buscando um resultado natural. Na avaliação é possível mostrar uma prévia do que dá para alcançar."},
    {"p":"Quanto tempo leva para ficar pronto?","r":"Depende do caso e é estimado na avaliação. Muitos tratamentos de estética são concluídos em poucas sessões."},
    {"p":"Quanto custa um tratamento estético?","r":"Depende do que você quer mudar. Na avaliação eu monto o plano e passo os valores e as formas de parcelamento, sem pressão para fechar na hora."},
    {"p":"Precisa de algum cuidado depois?","r":"Sim, cuidados simples de higiene e manutenção mantêm o resultado por mais tempo. Tudo é explicado no fim do tratamento."}
  ],
  "convenios":["Particular","[Convênio 1]"],
  "parcelamento":"[X]",
  "local":{"endereco":"[Endereço do consultório], Mauá","horario":"Segunda a sábado, mediante agendamento","agendamento":"Por WhatsApp, com retorno no mesmo dia"},
  "google":{"nota":"","total":"67","url":"","depoimentos":[]},
  "imagens":{"capa":"","retrato":"","sobre1":"","sobre2":"","banner1":"","banner2":"","post":""},
  "rodapeNota":"Demonstração para apresentação. As fotos reais entram nos espaços marcados; casos clínicos divulgados conforme a Resolução CFO 196/2019."
}

site_over = {
  "produto":"site","efeitos":False,"nav":"centro","capa":"editorial","banners":"cheio",
  "sobreLayout":"livre","sobreLado":"dir","procLayout":"lista","faqLayout":"centro",
  "localLayout":"faixa","movimento":"lateral",
  "secoes":["banners","sobre","procedimentos","avaliacoes","duvidas","local","posts"]
}
link_over = {
  "produto":"link","efeitos":True,"nav":"centro","capa":"editorial","banners":"cheio",
  "sobreLayout":"livre","sobreLado":"dir","procLayout":"cartoes","faqLayout":"centro",
  "localLayout":"faixa","movimento":"lateral",
  "secoes":["banners","retrato","procedimentos","passando","duvidas","local","posts"]
}
gen_pair("02-katia", base, site_over, link_over, "Dra. Katia Teixeira")
