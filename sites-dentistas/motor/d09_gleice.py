base = {
  "nome":"Dra. Gleice Gomes","nomeCurto":"Gleice","sobrenome":"Gomes","selo":"GG",
  "cargo":"Cirurgiã-Dentista · Ortodontia e Lentes",
  "especialidades":"Transforme o seu sorriso",
  "cidade":"Mauá, SP",
  "instagram":"dra.gleicegomes_",
  "whatsapp":"5511963665493",
  "whatsMsg":"Olá, Dra. Gleice. Gostaria de agendar uma avaliação.",
  "cro":"CRO-SP 148576",
  "tema":"claro",
  "paleta":{"bg":"#FAF8F6","surface":"#F0ECE8","raise":"#E5DED8","deep":"#FFFFFF",
            "ink":"#282320","muted":"#746B64","accent":"#B07A6B","fill":"#96584A"},
  "fontes":"organica","formato":"suave",
  "sobre":{
    "titulo":"Ajudo você a transformar o seu sorriso",
    "textos":[
      "Cirurgiã-dentista em Mauá, com foco em ortodontia e lentes de resina. Cada tratamento parte de uma avaliação individual e de uma conversa honesta sobre o que dá para alcançar no seu caso.",
      "O atendimento é próximo e sem pressa, com acompanhamento pessoal da avaliação ao resultado final."
    ],
    "destaques":[
      {"t":"Ortodontia","d":"Correção do sorriso com acompanhamento de perto."},
      {"t":"Lentes de resina","d":"Mais harmonia e naturalidade para o seu sorriso."},
      {"t":"Avaliação individual","d":"Plano honesto, feito para o seu caso."}
    ]
  },
  "passandoRotulo":"Antes e depois","passandoTitulo":"Sorrisos de perto","passando":"procedimentos",
  "bannersLista":[
    {"linha":"Quero transformar","destaque":"meu sorriso","acao":"whatsapp"},
    {"linha":"Veja os","destaque":"resultados","acao":"#procedimentos"}
  ],
  "retrato":{"titulo":"Honestidade primeiro",
    "texto":"Prefiro te mostrar o que dá para alcançar de verdade, com um plano feito para o seu caso. Acompanho cada etapa de perto, até o resultado que a gente combinou."},
  "procedimentos":[
    {"id":"lentes","nome":"Lentes de Resina","resumo":"Facetas em resina para corrigir forma, cor e espaços, com resultado natural.",
     "fotos":[{"src":"","t":"Lentes","leg":"Antes e depois"},{"src":"","t":"Detalhe","leg":"Acabamento natural"},{"src":"","t":"Sorriso","leg":"Resultado final"}]},
    {"id":"orto","nome":"Ortodontia","resumo":"Aparelho e alinhadores para corrigir o posicionamento dos dentes e a mordida.",
     "fotos":[{"src":"","t":"Ortodontia","leg":"Alinhamento em destaque"},{"src":"","t":"Detalhe","leg":"Aparelho"}]},
    {"id":"clareamento","nome":"Clareamento","resumo":"Clareamento dental para um sorriso mais claro, com acompanhamento profissional.",
     "fotos":[{"src":"","t":"Clareamento","leg":"Sorriso mais claro"},{"src":"","t":"Detalhe","leg":"Resultado uniforme"}]},
    {"id":"geral","nome":"Odontologia Geral","resumo":"Prevenção, limpeza e restaurações para manter o sorriso saudável.",
     "fotos":[{"src":"","t":"Odontologia","leg":"Cuidado preventivo"},{"src":"","t":"Detalhe","leg":"Restauração"}]}
  ],
  "duvidas":[
    {"p":"As lentes de resina ficam naturais?","r":"Sim. As lentes são planejadas conforme o seu rosto e o formato dos dentes. Na avaliação eu mostro o que dá para alcançar antes de começar."},
    {"p":"Dá para ver o resultado antes?","r":"Na avaliação conversamos sobre expectativas e, quando possível, mostro referências e uma prévia do que é viável no seu caso."},
    {"p":"O orçamento é fechado na avaliação?","r":"Sim, na avaliação você já sai com o orçamento do seu caso, por escrito e com as formas de pagamento. Sem compromisso de fechar ali."},
    {"p":"Precisa de cuidado depois?","r":"Sim, cuidados simples de higiene e manutenção mantêm o resultado por mais tempo. Tudo é explicado ao fim do tratamento."}
  ],
  "convenios":["Particular","[Convênio 1]"],
  "parcelamento":"[X]",
  "local":{"endereco":"[Endereço do consultório], Mauá","horario":"Segunda a sexta, mediante agendamento","agendamento":"Por WhatsApp, com retorno no mesmo dia"},
  "google":{"nota":"","total":"68","url":"","depoimentos":[]},
  "imagens":{"capa":"","retrato":"","sobre1":"","sobre2":"","banner1":"","banner2":"","post":""},
  "rodapeNota":"Página demonstrativa. As fotos reais substituem os espaços indicados; a divulgação de casos segue a Resolução CFO 196/2019."
}

site_over = {
  "produto":"site","efeitos":False,"nav":"esq","capa":"limpa","banners":"lado",
  "sobreLayout":"faixa","sobreLado":"esq","procLayout":"lista","faqLayout":"duas",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["sobre","procedimentos","avaliacoes","duvidas","local","posts"]
}
link_over = {
  "produto":"link","efeitos":False,"nav":"esq","capa":"limpa","banners":"lado",
  "sobreLayout":"faixa","sobreLado":"esq","procLayout":"cartoes","faqLayout":"duas",
  "localLayout":"cartao","movimento":"subir",
  "secoes":["banners","retrato","procedimentos","passando","duvidas","local","posts"]
}
gen_pair("09-gleice", base, site_over, link_over, "Dra. Gleice Gomes")
