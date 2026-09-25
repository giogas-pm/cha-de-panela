# -*- coding: utf-8 -*-
# Conteúdo das páginas de SEO do Kit do Chá. Cada página entrega conteúdo grátis de verdade + CTA pro gerador.
GUIAS = [
  ("brincadeiras-cha-de-panela-para-imprimir", "Brincadeiras de chá de panela para imprimir"),
  ("bingo-cha-de-panela-para-imprimir", "Bingo de chá de panela para imprimir"),
  ("bingo-cha-de-panela-como-funciona", "Como funciona o bingo do chá de panela"),
  ("perguntas-quem-conhece-a-noiva", "Perguntas: quem conhece a noiva"),
  ("stop-cha-de-panela", "Stop do chá de panela"),
  ("prendas-cha-de-panela", "Prendas de chá de panela"),
  ("brincadeiras-cha-de-cozinha", "Brincadeiras de chá de cozinha"),
  ("brincadeiras-cha-bar", "Brincadeiras de chá bar"),
  ("brincadeiras-cha-de-casa-nova", "Brincadeiras de chá de casa nova"),
  ("brincadeiras-cha-de-panela-evangelico", "Chá de panela evangélico: brincadeiras"),
  ("lista-de-cha-de-panela-completa", "Lista de chá de panela completa"),
]

def cta(slug, kind, titulo, texto, botao, extra=""):
    href = f"/cha-de-panela/?src=seo&amp;p={slug}{extra}"
    return f'''<aside class="cta cta-{kind}">
  <p class="ct">{titulo}</p>
  <p>{texto}</p>
  <a class="btn btn-main" href="{href}" data-cta="{kind}">{botao}</a>
  <p class="price">Prévia grátis · o Stop do Chá sai de graça · kit completo R$24,90, pagamento único</p>
</aside>'''

def L(slug, text):
    return f'<a href="/cha-de-panela/{slug}/">{text}</a>'

def ul(items, cls="l"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def ol(items):
    return '<ol class="l">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

CONTENT = []

# ---------------------------------------------------------------- 1
s = "brincadeiras-cha-de-panela-para-imprimir"
CONTENT.append(dict(slug=s, crumb="Brincadeiras para imprimir",
  title="Brincadeiras de Chá de Panela para Imprimir (Kit Completo)",
  desc="As 8 brincadeiras de chá de panela que mais funcionam, com regras, tempo de cada uma e o que imprimir. Inclui modelo grátis de Stop do Chá.",
  h1="Brincadeiras de chá de panela para imprimir: o kit que funciona de verdade",
  body=f"""<p class="lead">Chá de panela bom tem ritmo: uma brincadeira pra quebrar o gelo enquanto as convidadas chegam, outra durante a abertura dos presentes e uma pra fechar com risada. Abaixo estão as brincadeiras que mais dão certo, quanto tempo cada uma leva e exatamente o que você precisa imprimir.</p>
{cta(s,"top","Quer tudo pronto, com o nome da noiva?","Digite o nome da noiva, escolha as cores do chá e veja o kit completo na hora: bingo com até 40 cartelas diferentes, quem conhece a noiva, stop, adivinhe o presente e prendas.","Montar o kit do meu chá")}
<div class="toc"><b>Nesta página</b><ol><li><a href="#roteiro">Roteiro de 2 horas</a></li><li><a href="#lista">As 8 brincadeiras</a></li><li><a href="#imprimir">O que imprimir e quantas cópias</a></li><li><a href="#dicas">Dicas de impressão</a></li></ol></div>
<h2 id="roteiro">Roteiro sugerido para um chá de 2 horas</h2>
<div class="tbl"><table><tr><th>Horário</th><th>Momento</th><th>Brincadeira</th></tr>
<tr><td>0:00–0:30</td><td>Chegada das convidadas</td><td>Quem conhece a noiva (cada uma responde sozinha)</td></tr>
<tr><td>0:30–1:20</td><td>Abertura dos presentes</td><td>Bingo do chá + adivinhe o presente, com prendas a cada erro</td></tr>
<tr><td>1:20–1:40</td><td>Lanche</td><td>Correção do "quem conhece" em voz alta</td></tr>
<tr><td>1:40–2:00</td><td>Encerramento</td><td>Stop do chá e entrega dos prêmios</td></tr></table></div>
<p>O segredo é rodar duas brincadeiras ao mesmo tempo durante a abertura dos presentes, que é o momento mais longo do chá. Bingo e adivinhe o presente combinam perfeitamente porque usam o mesmo gatilho: cada presente aberto.</p>
<h2 id="lista">As 8 brincadeiras que mais funcionam</h2>
<h3>1. Bingo do chá de panela</h3>
<p>Cada convidada recebe uma cartela com 16 presentes. Conforme a noiva abre os pacotes, quem tiver o item marca. Ganha quem fechar uma linha. A regra de ouro: <b>as cartelas precisam ser diferentes</b>, senão várias pessoas gritam bingo juntas. Veja {L("bingo-cha-de-panela-como-funciona","como funciona o bingo passo a passo")}.</p>
<h3>2. Quem conhece mais a noiva?</h3>
<p>Uma folha com 10 a 12 perguntas sobre a noiva (comida preferida, onde conheceu o noivo, maior medo). Quem acertar mais ganha. Temos {L("perguntas-quem-conhece-a-noiva","mais de 60 perguntas prontas")}.</p>
<h3>3. Adivinhe o presente</h3>
<p>Antes de abrir, a noiva chacoalha a caixa e tenta adivinhar o que é. Errou, paga prenda. As convidadas também anotam palpites numa folha e quem acertar mais ganha.</p>
<h3>4. Stop do chá</h3>
<p>O clássico stop com categorias do tema: utensílio de cozinha, comida, nome de casal, lugar pra lua de mel. Rende 15 minutos de risada. {L("stop-cha-de-panela","Modelo e categorias aqui")}.</p>
<h3>5. Prendas da noiva</h3>
<p>Cartõezinhos dobrados num pote. A noiva sorteia um a cada erro. Veja {L("prendas-cha-de-panela","50 prendas divertidas e sem apelação")}.</p>
<h3>6. Túnel do tempo</h3>
<p>Peça às convidadas que tragam uma foto antiga com a noiva. Monte um varal e peça pra noiva contar a história de cada uma. Não precisa imprimir nada, só prendedores e barbante.</p>
<h3>7. Conselhos para os noivos</h3>
<p>Cartões em branco onde cada convidada escreve um conselho ou uma receita de família. A noiva guarda como lembrança. Imprima em papel mais grosso.</p>
<h3>8. Batata quente das perguntas</h3>
<p>Um objeto passa de mão em mão com música; quando a música para, quem estiver com ele responde uma pergunta sobre o casal. Bom pra chás menores, de até 15 pessoas.</p>
<h2 id="imprimir">O que imprimir e quantas cópias</h2>
<div class="tbl"><table><tr><th>Item</th><th>Formato</th><th>Quantidade</th></tr>
<tr><td>Cartela de bingo</td><td>4 por folha A4</td><td>1 por convidada</td></tr>
<tr><td>Quem conhece a noiva</td><td>2 por folha A4</td><td>1 por convidada + gabarito</td></tr>
<tr><td>Adivinhe o presente</td><td>2 por folha A4</td><td>1 por convidada</td></tr>
<tr><td>Stop do chá</td><td>2 por folha A4</td><td>1 por convidada</td></tr>
<tr><td>Prendas</td><td>24 por folha A4</td><td>1 folha</td></tr></table></div>
<p>Para um chá de 20 convidadas isso dá umas 26 folhas. Em papelaria, a impressão colorida sai entre R$1 e R$2 por folha.</p>
<h2 id="dicas">Dicas de impressão</h2>
{ul(["Imprima sempre em <b>tamanho real (100%)</b>, sem 'ajustar à página', pra não cortar as bordas.","Papel 180g deixa as cartelas firmes; sulfite comum também funciona se tiver prancheta ou revista pra apoiar.","Quer economizar tinta? Escolha uma paleta clara ou a versão preto e branco.","Leve o PDF no celular: qualquer papelaria imprime direto do WhatsApp ou pendrive."])}
{cta(s,"end","Kit completo com a cara do chá","Capa com os nomes, guia da madrinha, bingo com cartelas únicas, quem conhece a noiva com gabarito, stop, adivinhe o presente e 24 prendas — tudo na paleta da decoração.","Ver a prévia grátis")}""",
  faq=[("Quantas brincadeiras fazer num chá de panela?","Entre 3 e 5. Mais que isso cansa. O combo mais seguro é quem conhece a noiva, bingo com adivinhe o presente durante a abertura dos presentes e stop no final."),
       ("Qual a brincadeira mais tradicional do chá de panela?","Adivinhar o presente e pagar prenda quando errar. O bingo virou o segundo clássico porque envolve todas as convidadas ao mesmo tempo."),
       ("Onde imprimir as brincadeiras?","Em casa ou em qualquer papelaria. Salve o PDF, leve no celular e peça impressão em A4, tamanho real.")]))

# ---------------------------------------------------------------- 2
s = "bingo-cha-de-panela-para-imprimir"
CONTENT.append(dict(slug=s, crumb="Bingo para imprimir",
  title="Bingo de Chá de Panela Pronto para Imprimir (PDF grátis)",
  desc="Bingo de chá de panela pronto pra imprimir: 60 palavras de presentes, modelo de cartela 4x4 e como gerar até 40 cartelas diferentes com o nome da noiva",
  h1="Bingo de chá de panela pronto para imprimir",
  body=f"""<p class="lead">O bingo é a brincadeira que segura o chá durante a abertura dos presentes. Aqui você encontra a lista de palavras, o modelo de cartela e o jeito mais rápido de ter cartelas todas diferentes em PDF.</p>
{cta(s,"top","Cartelas prontas, todas diferentes","Digite o nome da noiva, escolha quantas cartelas (10 a 40) e as cores. A gente embaralha e confere uma por uma pra não repetir nenhuma combinação.","Gerar as cartelas do meu chá")}
<h2>Por que as cartelas precisam ser diferentes</h2>
<p>A maioria dos PDFs grátis traz 4 ou 6 cartelas que você imprime várias vezes. Resultado: três convidadas com a mesma cartela gritam bingo no mesmo presente, e a madrinha precisa inventar desempate. Com 20 convidadas, você precisa de 20 combinações únicas. Fazer isso à mão leva uma tarde; um gerador faz em segundos.</p>
<h2>Modelo de cartela</h2>
<p>O formato que melhor funciona é <b>4 x 4 (16 casas)</b>, com 4 cartelas por folha A4. Cartela 5 x 5 fica com letra pequena e demora demais pra fechar. Coloque no topo o nome dos noivos e a data, e no rodapé o número da cartela (ajuda na conferência).</p>
<h2>60 palavras para o bingo do chá de panela</h2>
{ul(["Jogo de panelas","Panela de pressão","Frigideira","Liquidificador","Batedeira","Air fryer","Sanduicheira","Pipoqueira","Chaleira","Cafeteira","Garrafa térmica","Jogo de copos","Jogo de taças","Jogo de pratos","Faqueiro","Tábua de corte","Jogo de facas","Escorredor de louça","Escorredor de macarrão","Ralador","Abridor de latas","Concha","Espátula","Colher de pau","Pegador de massa","Peneira","Forma de bolo","Assadeira","Travessa de vidro","Potes herméticos","Porta-temperos","Açucareiro","Fruteira","Pano de prato","Avental","Luva térmica","Descanso de panela","Jogo americano","Toalha de mesa","Leiteira","Mixer","Espremedor de alho","Fouet","Forma de gelo","Porta-talheres","Jarra de suco","Jogo de xícaras","Tigelas","Balança de cozinha","Lixeira de pia","Porta-guardanapo","Bule","Cuscuzeira","Wok","Grill","Moedor de pimenta","Saladeira","Petisqueira","Pote de mantimentos","Kit churrasco"],"cols")}
<p class="note">Dica: misture a lista de presentes real da noiva com itens clássicos. Se a lista dela tem 30 itens, use esses 30 + uns 10 clássicos. Assim o bingo anda rápido e ninguém fica com a cartela parada.</p>
<h2>Como montar as cartelas à mão (se preferir)</h2>
{ol(["Escreva cada palavra num papelzinho e coloque num pote.","Para cada cartela, sorteie 16 papéis e copie na ordem em que saírem.","Devolva os papéis ao pote antes da próxima cartela.","Confira se nenhuma cartela ficou com os mesmos 16 itens de outra."])}
<p>Para 20 cartelas, conte umas 2 horas. No gerador, 40 cartelas saem em 1 minuto, já com a folha de controle da madrinha.</p>
<h2>Folha de controle</h2>
<p>Imprima uma lista com todas as palavras usadas e vá riscando conforme a noiva abre os presentes. Quando alguém gritar bingo, você confere em segundos. O kit já vem com essa folha.</p>
{cta(s,"end","Bingo + o resto do kit","Além das cartelas únicas, o kit traz quem conhece a noiva, stop, adivinhe o presente, prendas e a capa com os nomes, na paleta do chá.","Ver a prévia grátis")}""",
  faq=[("Quantas cartelas de bingo fazer?","Uma por convidada, mais 2 ou 3 de reserva. O gerador faz de 10 a 40 cartelas, todas diferentes."),
       ("Quantas palavras precisa ter o bingo do chá?","Pelo menos 30 para 16 casas por cartela. Com menos, as cartelas ficam parecidas demais e várias fecham juntas."),
       ("O bingo de chá de panela tem que ter os presentes reais?","Não precisa, mas funciona melhor. Use a lista de presentes da noiva e complete com itens clássicos de cozinha.")]))

# ---------------------------------------------------------------- 3
s = "bingo-cha-de-panela-como-funciona"
CONTENT.append(dict(slug=s, crumb="Como funciona o bingo",
  title="Bingo de Chá de Panela: Como Funciona (Regras e Passo a Passo)",
  desc="Como funciona o bingo do chá de panela: preparo, regras, quem canta os itens, quando vale bingo, desempate e prêmios. Passo a passo pra madrinha.",
  h1="Bingo de chá de panela: como funciona, passo a passo",
  body=f"""<p class="lead">O bingo de chá de panela troca os números por presentes. A noiva abre os pacotes, alguém anuncia o que saiu e as convidadas marcam nas cartelas. Parece simples, mas alguns detalhes fazem a diferença entre um jogo animado e uma confusão.</p>
<h2>Passo a passo</h2>
{ol(["<b>Antes do chá:</b> prepare uma cartela diferente pra cada convidada (4 x 4 é o ideal) e uma folha de controle com todos os itens.","<b>Na chegada:</b> entregue a cartela e uma caneta pra cada uma. Explique a regra em 30 segundos.","<b>Durante a abertura:</b> cada vez que a noiva abrir um presente, a madrinha fala o nome em voz alta e risca na folha de controle.","<b>Marcação:</b> quem tiver o item na cartela marca com um X.","<b>Bingo:</b> quem completar uma linha (horizontal, vertical ou diagonal) grita bingo.","<b>Conferência:</b> a madrinha confere os itens da cartela com a folha de controle.","<b>Segunda rodada (opcional):</b> continue até alguém fechar a cartela cheia, com um prêmio maior."])}
<h2>Regras que evitam briga</h2>
{ul(["<b>Presente parecido vale?</b> Combine antes: 'jogo de copos' vale para 'copos de vidro', mas 'caneca' não vale para 'xícara'. A madrinha decide e pronto.","<b>Presente que não está na lista:</b> ninguém marca. Diga o nome do mesmo jeito, é divertido.","<b>Dois bingos no mesmo presente:</b> ganha quem gritou primeiro; ou as duas ganham um prêmio menor.","<b>Presente repetido:</b> marca só uma vez."])}
<h2>Quantos itens precisa?</h2>
<p>Com cartelas de 16 casas, use de 30 a 50 itens diferentes na lista. Com menos de 30, as cartelas ficam parecidas e muita gente fecha junto. Com mais de 60, o jogo pode acabar sem ganhador se a noiva ganhar poucos presentes.</p>
<p>Regra prática: <b>número de itens ≈ número de presentes esperados + 15</b>.</p>
<h2>E se a noiva ganhar poucos presentes?</h2>
<p>Em chás pequenos (menos de 15 presentes), vale a linha de 3 casas em vez de 4, ou considerar também os itens que aparecem dentro de kits (um kit de utensílios pode 'cantar' concha, espátula e pegador ao mesmo tempo).</p>
<h2>Prêmios baratos que fazem sucesso</h2>
{ul(["Brigadeiro gourmet ou pote de doce","Vela aromática","Suculenta num vasinho","Esmalte","Kit de chá ou café"])}
{cta(s,"top","Cartelas únicas + folha de controle, prontas","O Kit do Chá gera até 40 cartelas diferentes com o nome da noiva e as cores do chá, já com a folha de controle da madrinha.","Montar o bingo do meu chá")}""",
  howto=dict(name="Como fazer o bingo do chá de panela", steps=[
    ("Prepare as cartelas","Faça uma cartela diferente por convidada, com 16 presentes cada, e uma folha de controle com todos os itens."),
    ("Distribua","Entregue cartela e caneta pra cada convidada na chegada."),
    ("Cante os presentes","A cada presente aberto pela noiva, fale o nome em voz alta e risque na folha de controle."),
    ("Marque","Quem tiver o item na cartela marca com X."),
    ("Confira o bingo","Quem fechar uma linha grita bingo; a madrinha confere com a folha de controle e entrega o prêmio.")]),
  faq=[("Quem canta o bingo no chá de panela?","A madrinha ou uma amiga próxima. A noiva fica ocupada abrindo os presentes."),
       ("Vale linha ou cartela cheia?","Primeiro linha (mais rápido). Se ainda houver presentes, faça uma segunda rodada de cartela cheia."),
       ("O bingo substitui o adivinhe o presente?","Não. Os dois rodam juntos: a noiva adivinha antes de abrir, e o presente aberto é cantado no bingo.")]))

# ---------------------------------------------------------------- 4
s = "perguntas-quem-conhece-a-noiva"
Q_NOIVA = ["Qual é a comida preferida da noiva?","Qual é a cor preferida dela?","Em que cidade ela nasceu?","Qual era o apelido de infância?","Qual é o maior medo dela?","Qual é o filme ou série preferida?","Qual é a viagem dos sonhos?","Qual prato ela faz melhor?","Qual é a mania mais engraçada dela?","Qual é o número do sapato?","Qual é a sobremesa preferida?","Qual é a bebida preferida?","Qual é a música que ela mais canta no chuveiro?","Qual foi o primeiro emprego dela?","Qual é o cantor ou banda preferida?","Ela é mais praia ou montanha?","Doce ou salgado?","Qual é a estação do ano preferida?","Qual é a flor preferida?","Qual o nome do primeiro bichinho de estimação?","Qual matéria ela mais odiava na escola?","Quantos irmãos ela tem?","Qual é o signo dela?","Qual é o prato que ela não come de jeito nenhum?","O que ela faz pra relaxar?","Qual é o perfume dela?","Qual o maior mico que ela já pagou?","Que talento escondido ela tem?"]
Q_CASAL = ["Onde a noiva e o noivo se conheceram?","Quem disse 'eu te amo' primeiro?","Onde foi o primeiro encontro?","Onde foi o pedido de casamento?","Qual é a música do casal?","Há quanto tempo estão juntos?","Qual foi a primeira viagem juntos?","Quem é mais ciumento?","Quem demora mais pra se arrumar?","Quem cozinha melhor?","Quem pede desculpas primeiro depois de uma briga?","O que a noiva mais admira no noivo?","Qual é o apelido carinhoso que um usa com o outro?","Qual foi o primeiro presente que ela ganhou dele?","Quem é mais bagunceiro?","Qual série o casal está assistindo agora?","Qual é o restaurante preferido dos dois?","Quem ronca?","Onde vai ser a lua de mel?","Quantos filhos eles querem ter?"]
Q_DIVER = ["Se a noiva fosse um tempero, qual seria?","Qual utensílio de cozinha tem a cara dela?","Se ela ganhasse na loteria, qual a primeira compra?","Que personagem de novela ela seria?","Qual emoji ela mais usa?","Quanto tempo ela leva pra responder mensagem?","Qual desculpa ela mais usa pra não ir à academia?","Se a vida dela fosse um filme, qual seria o título?","O que ela nunca sai de casa sem?","Qual comida ela come escondida de madrugada?","Qual palavra ela fala o tempo todo?","Qual celebridade ela diz que é o 'crush' eterno?"]
CONTENT.append(dict(slug=s, crumb="Quem conhece a noiva",
  title="Perguntas Quem Conhece a Noiva: 60 Perguntas + Gabarito",
  desc="60 perguntas para o jogo quem conhece mais a noiva no chá de panela: sobre a noiva, sobre o casal e engraçadas. Com dicas de gabarito e desempate.",
  h1="Perguntas para o jogo \"quem conhece mais a noiva\"",
  body=f"""<p class="lead">É a brincadeira perfeita para a chegada das convidadas: cada uma responde sozinha, sem ajuda, e no fim a noiva (ou a madrinha) lê o gabarito. Escolha de 10 a 12 perguntas — mais que isso cansa e não cabe numa folha.</p>
{cta(s,"top","Folha pronta com o nome da noiva e gabarito","No Kit do Chá você escolhe as perguntas, digita as respostas e sai a folha das convidadas (2 por A4) + o gabarito da madrinha, nas cores do chá.","Montar o quem conhece do meu chá")}
<h2>Como montar um bom "quem conhece"</h2>
{ul(["<b>Misture fáceis e difíceis.</b> 6 fáceis (comida, cor), 4 médias (apelido, medo) e 2 difíceis (número do sapato, primeiro emprego).","<b>Evite perguntas que só a família sabe.</b> Senão a mãe da noiva sempre ganha.","<b>Pegue o gabarito antes.</b> Pergunte discretamente ao noivo ou à mãe, ou peça pra noiva responder no dia, na frente de todas.","<b>Tenha uma pergunta de desempate numérica</b>, tipo 'quantos presentes a noiva vai ganhar hoje?'. Quem chegar mais perto ganha."])}
<h2>28 perguntas sobre a noiva</h2>
{ol(Q_NOIVA)}
<h2>20 perguntas sobre o casal</h2>
{ol(Q_CASAL)}
<h2>12 perguntas engraçadas</h2>
{ol(Q_DIVER)}
<h2>Variações do jogo</h2>
<h3>Noiva responde, convidadas apostam</h3>
<p>As convidadas respondem primeiro; depois a noiva responde em voz alta. É mais divertido que ler um gabarito, e às vezes ela 'erra' sobre si mesma.</p>
<h3>Versão casal (chá bar)</h3>
<p>No chá bar, use as perguntas do casal e faça o noivo e a noiva responderem ao mesmo tempo, de costas, levantando plaquinhas. Veja mais em {L("brincadeiras-cha-bar","brincadeiras de chá bar")}.</p>
<h3>Versão evangélica</h3>
<p>Troque signo e bebida por 'qual o louvor preferido?' e 'qual o versículo preferido?'. Mais ideias em {L("brincadeiras-cha-de-panela-evangelico","chá de panela evangélico")}.</p>
{cta(s,"end","Tudo pronto em 1 minuto","Perguntas com o nome da noiva, gabarito, bingo com cartelas únicas, stop, adivinhe o presente e prendas.","Ver a prévia grátis")}""",
  faq=[("Quantas perguntas colocar no quem conhece a noiva?","De 10 a 12. Cabe numa meia folha A4 e leva uns 10 minutos pra responder."),
       ("Quem faz o gabarito?","A madrinha, perguntando discretamente ao noivo ou à família. Ou a própria noiva responde em voz alta na hora da correção."),
       ("Como desempatar?","Com uma pergunta numérica: quem chegar mais perto do número de presentes que a noiva vai ganhar, por exemplo.")]))

# ---------------------------------------------------------------- 5
s = "stop-cha-de-panela"
CONTENT.append(dict(slug=s, crumb="Stop do chá",
  title="Stop Chá de Panela: Categorias, Regras e Modelo Grátis",
  desc="Stop do chá de panela: 30 categorias temáticas, regras de pontuação e modelo pronto pra imprimir grátis com o nome da noiva, 2 por folha A4.",
  h1="Stop do chá de panela: categorias, regras e modelo grátis",
  body=f"""<p class="lead">O stop (ou adedonha) ganha outra graça no chá de panela quando as categorias são do tema. É ótimo para o final da festa: rápido, todo mundo joga junto e não precisa de nada além de papel e caneta.</p>
{cta(s,"top","Modelo de Stop grátis, com o nome da noiva","Digite o nome da noiva, escolha as cores e imprima o Stop do Chá de graça (2 por folha A4). Sem cadastro.","Imprimir o Stop grátis")}
<h2>Como jogar</h2>
{ol(["Cada convidada recebe uma folha com as categorias.","Alguém fala 'A' em voz alta e segue o alfabeto de cabeça; outra pessoa grita 'stop' e a letra da vez é a da rodada.","Todas escrevem uma palavra com aquela letra em cada coluna.","A primeira a completar grita 'stop!' e todas param de escrever.","Cada uma lê as respostas e soma os pontos."])}
<h2>Pontuação</h2>
<div class="tbl"><table><tr><th>Situação</th><th>Pontos</th></tr><tr><td>Resposta que só você escreveu</td><td>10</td></tr><tr><td>Resposta repetida por outra pessoa</td><td>5</td></tr><tr><td>Em branco ou inválida</td><td>0</td></tr></table></div>
<p>Jogue de 5 a 6 rodadas. Evite as letras K, W, Y, X e Q (ou valha qualquer palavra que tenha a letra, pra ficar engraçado).</p>
<h2>30 categorias para o stop do chá</h2>
<h3>Clássicas do chá de panela</h3>
{ul(["Utensílio de cozinha","Comida","Fruta","Tempero","Eletrodoméstico","Nome de casal famoso","Lugar pra lua de mel","Qualidade da noiva","Sobremesa","Bebida"],"cols")}
<h3>Românticas</h3>
{ul(["Música romântica","Filme de amor","Apelido carinhoso","Presente de namorados","Motivo de briga de casal","Cidade pra casar"],"cols")}
<h3>Pra casa nova</h3>
{ul(["Objeto da casa","Cômodo ou móvel","Cor de parede","Planta","Produto de limpeza","Coisa que quebra"],"cols")}
<h3>Evangélicas</h3>
{ul(["Personagem bíblico","Livro da Bíblia","Louvor","Fruto do Espírito","Cidade bíblica","Virtude"],"cols")}
<h3>Engraçadas</h3>
{ul(["Desculpa pra não lavar a louça","Coisa que o noivo esquece","Mania da noiva"],"cols")}
<h2>Exemplo de rodada com a letra P</h2>
<div class="tbl"><table><tr><th>Utensílio</th><th>Comida</th><th>Nome de casal</th><th>Lua de mel</th><th>Qualidade da noiva</th></tr><tr><td>Panela</td><td>Pudim</td><td>Pedro e Paula</td><td>Paris</td><td>Paciente</td></tr></table></div>
{cta(s,"end","O Stop é grátis. O kit completo vai além","Bingo com cartelas únicas, quem conhece a noiva com gabarito, adivinhe o presente, 24 prendas e capa com os nomes, tudo na paleta do chá.","Montar o kit do meu chá")}""",
  howto=dict(name="Como jogar stop no chá de panela", steps=[
    ("Distribua as folhas","Cada convidada recebe uma folha de stop com as categorias do chá."),
    ("Sorteie a letra","Uma pessoa recita o alfabeto de cabeça e outra grita stop; a letra da vez vale na rodada."),
    ("Preencha","Todas escrevem uma palavra com a letra em cada categoria."),
    ("Stop!","A primeira a completar grita stop e todas param."),
    ("Some os pontos","Resposta única vale 10, repetida 5, em branco 0.")]),
  faq=[("Quantas rodadas de stop jogar no chá?","De 5 a 6 rodadas, uns 15 minutos. Mais que isso cansa."),
       ("O modelo de stop é grátis mesmo?","Sim. No Kit do Chá você digita o nome da noiva e imprime o Stop do Chá sem pagar nada.")]))

# ---------------------------------------------------------------- 6
s = "prendas-cha-de-panela"
PREND = ["Imitar uma galinha botando ovo por 10 segundos","Cantar o refrão de uma música romântica","Dançar com a vassoura como par","Mandar um áudio de declaração pro noivo","Contar como foi o primeiro encontro","Desfilar com o presente na cabeça","Falar uma qualidade de cada madrinha","Fazer um brinde improvisado aos noivos","Falar um trava-língua 3 vezes rápido","Usar o avental até o fim do chá","Contar a maior mania do noivo","Fazer 10 polichinelos contando alto","Desenhar o noivo de olhos fechados","Pular num pé só por 15 segundos","Imitar o bicho que as convidadas escolherem","Fazer 3 poses de modelo pra foto","Inventar um versinho com a palavra 'panela'","Escolher uma convidada pra dançar juntas","Contar o mico mais recente","Fazer o comercial do presente que acabou de abrir","Ficar 30 segundos sem rir","Prender um prendedor na blusa a cada erro","Imitar a própria mãe dando bronca","Dizer 5 coisas que ama no noivo em 20 segundos","Cantar Parabéns com voz de personagem","Andar com um livro na cabeça até a porta","Falar 5 utensílios de cozinha em 10 segundos","Imitar um cantor escolhido pelas amigas","Contar o pior presente que já ganhou","Virar estátua até a próxima rodada","Adivinhar o nome do meio de uma convidada","Dar uma voltinha desfilando como miss","Usar um laço gigante de fita no cabelo","Tomar um copo d'água sem usar as mãos (com canudo)","Comer uma colher de limão sem careta","Fazer a dança da cadeira sozinha","Ligar pra sogra e dizer que ama ela","Soletrar o nome completo do noivo de trás pra frente","Rebolar com um bambolê (ou fingir que tem um)","Fazer uma serenata pra madrinha","Contar a primeira impressão que teve do noivo","Descrever a lua de mel dos sonhos em 3 palavras","Encenar como o noivo acorda","Falar 'eu vou ser uma ótima esposa' com sotaque","Montar um penteado em uma convidada em 1 minuto","Fazer mímica de um filme pra todas adivinharem","Cantar um jingle de comercial antigo","Responder a próxima pergunta só com gestos","Mostrar a última foto da galeria do celular","Dar um abraço coletivo nas madrinhas"]
CONTENT.append(dict(slug=s, crumb="Prendas",
  title="Prendas de Chá de Panela: 50 Ideias Divertidas (Sem Apelação)",
  desc="50 prendas para chá de panela divertidas e sem apelação, pra jogar até com a avó na sala. Como usar, quando sortear e versão pra imprimir.",
  h1="Prendas de chá de panela: 50 ideias divertidas e sem apelação",
  body=f"""<p class="lead">A prenda é o 'castigo' que a noiva paga quando erra o palpite do presente. É a parte do chá que mais rende foto e vídeo. A regra é uma só: tem que ser engraçada pra quem assiste e tranquila pra quem paga — ninguém quer passar vergonha de verdade na frente da sogra.</p>
{cta(s,"top","24 prendas prontas pra recortar","No Kit do Chá as prendas saem num cartão bonito, na paleta do chá, com o nome dos noivos. Recorte, dobre e coloque no potinho.","Montar as prendas do meu chá")}
<h2>Como usar as prendas</h2>
{ol(["Imprima e recorte os cartões.","Dobre e coloque num pote, cesta ou panela (claro).","Antes de abrir cada presente, a noiva dá um palpite.","Errou? Sorteia uma prenda e paga na hora.","Combine um sinal com a noiva pra ela 'errar' de propósito quando o chá estiver parado."])}
<h2>50 prendas para o chá de panela</h2>
{ol(PREND)}
<h2>Prendas para chá evangélico</h2>
{ul(["Cantar o refrão de um louvor","Recitar um versículo de cor","Contar como Deus uniu o casal","Fazer uma oração curtinha pelo lar dos noivos","Contar um testemunho do namoro"])}
<p>Mais ideias em {L("brincadeiras-cha-de-panela-evangelico","brincadeiras de chá de panela evangélico")}.</p>
<h2>Prendas pro noivo (chá bar)</h2>
{ul(["Imitar a noiva acordando","Fazer uma serenata pra noiva","Vestir o avental até o fim","Contar quem deu o primeiro passo","Dançar 20 segundos sem música"])}
<h2>O que evitar</h2>
{ul(["Prendas com bebida alcoólica obrigatória (nem todo mundo bebe).","Expor segredos do casal ou ex-namorados.","Qualquer coisa que envolva tirar roupa ou constrangimento físico.","Prendas que sujam demais (ovo, farinha) se o chá for dentro de casa."])}
{cta(s,"end","Prendas + bingo + quem conhece a noiva","O kit completo tem 24 prendas, bingo com cartelas únicas, quem conhece a noiva, stop e adivinhe o presente, com a cara do chá.","Ver a prévia grátis")}""",
  faq=[("O que é prenda no chá de panela?","É um desafio divertido que a noiva paga quando erra o palpite sobre o presente antes de abrir."),
       ("Quantas prendas preparar?","De 20 a 30. A noiva costuma errar em metade dos presentes."),
       ("Prenda serve pro noivo também?","No chá bar ou chá de casal, sim. Faça cartões separados pra ele.")]))

# ---------------------------------------------------------------- 7
s = "brincadeiras-cha-de-cozinha"
CONTENT.append(dict(slug=s, crumb="Chá de cozinha",
  title="Brincadeiras de Chá de Cozinha: 10 Ideias com Castigos",
  desc="Brincadeiras de chá de cozinha para imprimir: bingo de utensílios, quem conhece a noiva, stop, adivinhe o tempero e castigos divertidos. Roteiro pronto.",
  h1="Brincadeiras de chá de cozinha (com castigos)",
  body=f"""<p class="lead">Chá de cozinha e chá de panela são praticamente a mesma festa — o nome muda conforme a região. O foco é equipar a cozinha do casal, então as brincadeiras giram em torno de utensílios, temperos e receitas.</p>
{cta(s,"top","Kit de chá de cozinha com o nome da noiva","Escolha 'chá de cozinha', digite o nome da noiva e as cores: sai bingo de utensílios com cartelas únicas, stop com categoria de tempero, quem conhece e prendas.","Montar o kit do chá de cozinha","&amp;tipo=cozinha")}
<h2>10 brincadeiras de chá de cozinha</h2>
<h3>1. Bingo de utensílios</h3><p>Igual ao bingo do chá de panela, com foco em itens de cozinha: concha, escumadeira, ralador, peneira. Cartelas diferentes pra cada convidada. {L("bingo-cha-de-panela-para-imprimir","Lista de 60 palavras aqui")}.</p>
<h3>2. Adivinhe o tempero</h3><p>Coloque 6 temperos em potinhos numerados (orégano, cominho, canela, páprica, noz-moscada, alecrim). A noiva, de olhos vendados, cheira e adivinha. Cada erro, um castigo.</p>
<h3>3. Adivinhe o presente</h3><p>O clássico: a noiva chacoalha, palpita e abre. Errou, paga castigo.</p>
<h3>4. Quem conhece a noiva</h3><p>Inclua perguntas de cozinha: 'qual prato ela faz melhor?', 'qual comida ela não come?'. {L("perguntas-quem-conhece-a-noiva","60 perguntas prontas")}.</p>
<h3>5. Stop da cozinha</h3><p>Categorias: utensílio, comida, tempero, sobremesa, nome de casal, qualidade da noiva. {L("stop-cha-de-panela","Veja o modelo")}.</p>
<h3>6. Receita às cegas</h3><p>Cada convidada escreve num cartão a receita que 'salva qualquer jantar'. A noiva lê e tenta adivinhar quem escreveu.</p>
<h3>7. Livro de receitas da família</h3><p>Peça no convite que cada convidada traga uma receita escrita à mão. Encaderne e entregue no final.</p>
<h3>8. Monte o prato</h3><p>Em duplas, uma de olhos vendados monta um sanduíche guiada só pela voz da outra. Rende muita risada.</p>
<h3>9. Qual é o utensílio?</h3><p>Coloque utensílios esquisitos num saco (descascador de alho, boleador, cortador de ovo). A noiva tateia e diz o que é.</p>
<h3>10. Castigos da cozinha</h3><p>Usar avental e touca até o fim, cantar com a colher de pau como microfone, fazer o comercial de um eletrodoméstico. {L("prendas-cha-de-panela","Mais 50 prendas")}.</p>
<h2>Castigos pro chá de cozinha</h2>
{ul(["Cantar o refrão de uma música usando a concha como microfone","Descrever a receita de miojo como se fosse chef de TV","Usar a panela como chapéu por 2 presentes","Imitar uma panela de pressão apitando","Dançar com o rolo de massa"])}
{cta(s,"end","Tudo impresso e combinando","Capa, guia da madrinha, bingo, quem conhece, stop, adivinhe o presente e prendas na paleta da decoração.","Ver a prévia grátis","&amp;tipo=cozinha")}""",
  faq=[("Chá de cozinha e chá de panela são a mesma coisa?","Sim, na prática. O nome muda por região; as brincadeiras e os presentes são os mesmos."),
       ("Quais castigos usar no chá de cozinha?","Castigos leves e com tema de cozinha: cantar com a colher de pau, usar a panela como chapéu, fazer o comercial de um utensílio.")]))

# ---------------------------------------------------------------- 8
s = "brincadeiras-cha-bar"
CONTENT.append(dict(slug=s, crumb="Chá bar",
  title="Brincadeiras de Chá Bar: 10 Ideias para Casal e Amigos",
  desc="Brincadeiras de chá bar para os noivos e convidados: bingo de bar, perguntas ele ou ela, stop de bebidas, adivinhe o presente e prendas pro casal.",
  h1="Brincadeiras de chá bar para o casal e os amigos",
  body=f"""<p class="lead">O chá bar é o chá de panela misto: homens e mulheres, noivo e noiva juntos, clima de boteco e presentes de bar e churrasco. As brincadeiras precisam funcionar pra todo mundo e colocar o casal no centro.</p>
{cta(s,"top","Kit de chá bar com o nome dos noivos","Escolha 'chá bar': o bingo vem com itens de bar e churrasco, o stop com bebida e petisco, e as prendas incluem o noivo.","Montar o kit do chá bar","&amp;tipo=bar")}
<h2>10 brincadeiras de chá bar</h2>
<h3>1. Ele ou ela (jogo do sapato)</h3><p>Noivos sentados de costas, cada um com um sapato seu e um do outro. A madrinha pergunta 'quem ronca mais?', 'quem cozinha melhor?' e os dois levantam o sapato de quem acham. Quando discordam, o público vai à loucura.</p>
<h3>2. Bingo do bar</h3><p>Cartelas com coqueteleira, balde de gelo, tábua de frios, kit churrasco, petisqueira. Cada cartela diferente. Funciona durante a abertura dos presentes.</p>
<h3>3. Quem conhece mais os noivos</h3><p>Perguntas sobre o casal: onde se conheceram, primeira viagem, quem pediu desculpa primeiro. {L("perguntas-quem-conhece-a-noiva","20 perguntas de casal aqui")}.</p>
<h3>4. Adivinhe o presente — versão duelo</h3><p>Noivo e noiva palpitam juntos. Quem errar paga prenda. Placar no quadro.</p>
<h3>5. Stop do bar</h3><p>Categorias: bebida, petisco, música pra dançar, nome de casal, lugar pra lua de mel, qualidade dos noivos.</p>
<h3>6. Time da noiva × time do noivo</h3><p>Divida os convidados em dois times e faça gincanas rápidas: quem monta o maior castelo de copos plásticos, quem canta mais músicas com a palavra 'amor'.</p>
<h3>7. Mímica de casal</h3><p>O noivo faz mímica de momentos do namoro e a noiva adivinha (e vice-versa).</p>
<h3>8. Batata quente das perguntas</h3><p>Uma garrafa (vazia) passa de mão em mão; quando a música para, quem estiver com ela conta uma história do casal.</p>
<h3>9. Karaokê dos noivos</h3><p>Os convidados escolhem a música, o casal canta. Simples e sempre funciona.</p>
<h3>10. Prendas do casal</h3><p>'O noivo imita a noiva acordando', 'serenata pra noiva', 'avental até o fim da festa'. {L("prendas-cha-de-panela","Mais prendas")}.</p>
<h2>Dica: bebida não precisa ser obrigatória</h2>
<p>Muita gente não bebe (ou está dirigindo). Evite prendas do tipo 'vira um copo' e tenha opções sem álcool. O chá bar funciona muito bem com drinks sem álcool e suco.</p>
{cta(s,"end","Kit completo do chá bar","Bingo do bar, quem conhece os noivos, stop, adivinhe o presente e prendas pro casal, com os nomes e as cores da festa.","Ver a prévia grátis","&amp;tipo=bar")}""",
  faq=[("O que é chá bar?","É um chá de panela misto, com noivo, noiva e amigos, em clima de bar, onde os presentes costumam ser itens de bar, churrasco e cozinha."),
       ("Quais as melhores brincadeiras de chá bar?","Ele ou ela (jogo do sapato), bingo do bar, quem conhece os noivos e adivinhe o presente em duelo."),
       ("Precisa ter bebida alcoólica?","Não. As brincadeiras funcionam igual com drinks sem álcool.")]))

# ---------------------------------------------------------------- 9
s = "brincadeiras-cha-de-casa-nova"
CONTENT.append(dict(slug=s, crumb="Chá de casa nova",
  title="Brincadeiras de Chá de Casa Nova: 10 Ideias para Imprimir",
  desc="Brincadeiras de chá de casa nova para imprimir: bingo da casa, stop, adivinhe o presente, caça ao tesouro nos cômodos e prendas. Pra casal ou solteira.",
  h1="Brincadeiras de chá de casa nova",
  body=f"""<p class="lead">O chá de casa nova (ou open house) serve pra quem está mudando — casal, solteira, amigas dividindo apê. Os presentes vão além da cozinha: cama, banho, ferramentas, organização. E as brincadeiras podem usar a própria casa como cenário.</p>
{cta(s,"top","Kit de chá de casa nova personalizado","Escolha 'chá de casa nova': o bingo vem com itens da casa toda, o stop com 'objeto da casa' e 'cômodo', e tudo sai com o nome de quem faz o chá.","Montar o kit do chá de casa nova","&amp;tipo=casanova")}
<h2>10 brincadeiras de chá de casa nova</h2>
<h3>1. Bingo da casa</h3><p>Cartelas com jogo de cama, toalhas, luminária, kit ferramentas, varal, aspirador. Todas diferentes, uma por convidado.</p>
<h3>2. Caça ao tesouro pelos cômodos</h3><p>Esconda 10 objetos pela casa e dê pistas em rima. Quem achar mais ganha. É também um jeito divertido de apresentar a casa.</p>
<h3>3. Adivinhe o presente</h3><p>O dono da casa chacoalha, palpita e abre. Errou, paga prenda.</p>
<h3>4. Stop da casa</h3><p>Categorias: objeto da casa, comida, cor, cidade, planta, qualidade do anfitrião. {L("stop-cha-de-panela","Mais categorias")}.</p>
<h3>5. Quanto custa?</h3><p>Mostre 5 itens do dia a dia (detergente, lâmpada, rolo de papel toalha) e cada um chuta o preço. Quem chegar mais perto ganha.</p>
<h3>6. Quem conhece o anfitrião</h3><p>Perguntas sobre manias domésticas: 'quem lava a louça?', 'qual cômodo é o preferido?', 'qual a primeira coisa que comprou pra casa?'.</p>
<h3>7. Mural de desejos</h3><p>Cada convidado escreve um desejo pra casa nova num post-it e cola na porta da geladeira.</p>
<h3>8. Adivinhe o cômodo</h3><p>Faça fotos bem de perto de detalhes da casa (maçaneta, azulejo, tomada). Quem acertar mais cômodos ganha.</p>
<h3>9. Planta da casa dos sonhos</h3><p>Em duplas, desenhem em 3 minutos a casa dos sonhos do anfitrião. Ele escolhe a vencedora.</p>
<h3>10. Prendas</h3><p>Varrer a sala com uma dança, imitar um aspirador, fazer o tour da casa como corretor de imóveis. {L("prendas-cha-de-panela","Mais prendas")}.</p>
<h2>Lista de presentes pra casa nova</h2>
{ul(["Jogo de cama","Toalhas de banho","Tapete","Cortina","Almofadas","Luminária","Porta-retrato","Vaso de planta","Kit ferramentas","Varal","Cesto de roupa","Ferro de passar","Aspirador","Organizadores","Espelho","Relógio de parede","Capacho","Travesseiros","Manta de sofá","Kit de limpeza"],"cols")}
<p>Pra cozinha, veja a {L("lista-de-cha-de-panela-completa","lista de chá de panela completa")}.</p>
{cta(s,"end","Tudo pronto, com o nome do chá","Capa, guia, bingo da casa com cartelas únicas, stop, quem conhece, adivinhe o presente e prendas.","Ver a prévia grátis","&amp;tipo=casanova")}""",
  faq=[("Chá de casa nova é só pra casal?","Não. Serve pra qualquer pessoa que está mudando: casal, solteira ou amigas dividindo apartamento."),
       ("Qual a diferença entre chá de casa nova e chá de panela?","O chá de panela é focado na cozinha e costuma acontecer antes do casamento; o de casa nova inclui presentes pra casa toda.")]))

# ---------------------------------------------------------------- 10
s = "brincadeiras-cha-de-panela-evangelico"
CONTENT.append(dict(slug=s, crumb="Chá de panela evangélico",
  title="Chá de Panela Evangélico: 10 Brincadeiras Cristãs",
  desc="Brincadeiras para chá de panela evangélico e cristão: bingo, quem conhece a noiva com perguntas de fé, stop bíblico, prendas família e versículos.",
  h1="Brincadeiras para chá de panela evangélico",
  body=f"""<p class="lead">Um chá de panela cristão pode ser tão divertido quanto qualquer outro — só troca apelação por criatividade. As brincadeiras abaixo funcionam com a avó, o pastor e as crianças na sala, e algumas ainda deixam uma palavra de bênção pro casal.</p>
{cta(s,"top","Kit cristão com o nome da noiva","Escolha o estilo 'cristão / evangélico': a capa traz 1 Coríntios 13:4, o stop tem 'personagem bíblico', as perguntas incluem louvor e versículo preferido e as prendas são 100% família.","Montar o kit cristão","&amp;estilo=cristao")}
<h2>10 brincadeiras para chá evangélico</h2>
<h3>1. Bingo do chá</h3><p>O bingo de presentes não tem nada que precise mudar: cada convidada marca os presentes que a noiva abre. {L("bingo-cha-de-panela-como-funciona","Como funciona")}.</p>
<h3>2. Quem conhece a noiva — versão de fé</h3><p>Inclua 'qual o louvor preferido dela?', 'qual o versículo preferido?', 'em que igreja ela se batizou?', 'qual ministério ela serve?'.</p>
<h3>3. Stop bíblico</h3><p>Categorias: personagem bíblico, livro da Bíblia, cidade bíblica, louvor, fruto do Espírito, qualidade da noiva.</p>
<h3>4. Adivinhe o presente</h3><p>Com prendas família em vez de castigos: cantar um louvor, recitar um versículo.</p>
<h3>5. Casais da Bíblia</h3><p>Leia uma pista ('ela foi buscar água no poço e voltou noiva') e as convidadas adivinham o casal (Rebeca e Isaque). Outros: Rute e Boaz, Abraão e Sara, Jacó e Raquel, Priscila e Áquila.</p>
<h3>6. Versículo embaralhado</h3><p>Escreva um versículo sobre amor em cartões, uma palavra por cartão. Em equipes, quem montar primeiro ganha. Sugestões: 1 Coríntios 13:4-7, Eclesiastes 4:12, Cantares 8:7.</p>
<h3>7. Cordão de três dobras</h3><p>Cada convidada escreve num papel uma oração ou conselho pro casal. Enrole tudo com três fitas trançadas (Eclesiastes 4:12) e entregue à noiva.</p>
<h3>8. Receitas com bênção</h3><p>Cada convidada traz uma receita e um versículo. Encaderne como livro de receitas da nova família.</p>
<h3>9. Mímica de histórias bíblicas</h3><p>Uma convidada faz a mímica e as outras adivinham: Davi e Golias, a arca de Noé, Jonas e o grande peixe.</p>
<h3>10. Oração pelo casal</h3><p>No encerramento, as convidadas fazem uma roda em volta da noiva. É um momento simples que costuma emocionar.</p>
<h2>Prendas para chá de panela evangélico</h2>
{ul(["Cantar o refrão de um louvor","Recitar um versículo de cor","Contar como Deus uniu o casal","Imitar uma galinha botando ovo","Dançar com a vassoura","Desfilar com o presente na cabeça","Falar uma qualidade de cada madrinha","Contar como foi o primeiro encontro"])}
<h2>Versículos para usar na decoração</h2>
{ul(["\"O amor é paciente, o amor é bondoso.\" — 1 Coríntios 13:4","\"O cordão de três dobras não se quebra tão depressa.\" — Eclesiastes 4:12","\"Sobretudo, revistam-se do amor, que é o elo perfeito.\" — Colossenses 3:14"])}
{cta(s,"end","Kit cristão completo","Capa com versículo, guia da madrinha, bingo com cartelas únicas, quem conhece a noiva, stop bíblico, adivinhe o presente e prendas família.","Ver a prévia grátis","&amp;estilo=cristao")}""",
  faq=[("Quais brincadeiras fazer num chá de panela evangélico?","Bingo, quem conhece a noiva com perguntas de fé, stop bíblico, casais da Bíblia e adivinhe o presente com prendas família."),
       ("Que prendas usar num chá cristão?","Cantar um louvor, recitar um versículo, contar como Deus uniu o casal e brincadeiras leves como imitar um bicho ou dançar com a vassoura.")]))

# ---------------------------------------------------------------- 11
s = "lista-de-cha-de-panela-completa"
def bloco(t, itens):
    return f"<h3>{t}</h3>" + ul(itens, "cols")
CONTENT.append(dict(slug=s, crumb="Lista de chá de panela",
  title="Lista de Chá de Panela Completa (120 Itens por Categoria)",
  desc="Lista de chá de panela completa com 120 itens separados por categoria: panelas, eletros, utensílios, mesa posta, organização. Com faixa de preço.",
  h1="Lista de chá de panela completa (por categoria)",
  body=f"""<p class="lead">Uma boa lista de chá de panela tem itens de todos os preços, pra cada convidada achar algo no orçamento dela, e evita os famosos três liquidificadores. Abaixo, 120 itens organizados por categoria — marque o que a noiva ainda não tem e mande pro grupo.</p>
{cta(s,"top","Use a lista no bingo do chá","Cole a lista da noiva no Kit do Chá e as cartelas do bingo saem com os presentes que ela realmente vai ganhar — até 40 cartelas diferentes.","Montar o bingo com a minha lista")}
<h2>Faixas de preço</h2>
<div class="tbl"><table><tr><th>Faixa</th><th>Exemplos</th></tr><tr><td>Até R$50</td><td>Utensílios, panos de prato, porta-temperos, forma de gelo, abridor</td></tr><tr><td>R$50–150</td><td>Jogo de copos, frigideira, tábuas, potes herméticos, faqueiro simples</td></tr><tr><td>R$150–400</td><td>Liquidificador, sanduicheira, jogo de panelas, air fryer básica</td></tr><tr><td>Acima de R$400</td><td>Batedeira planetária, micro-ondas, panela elétrica, jogo de panelas premium</td></tr></table></div>
<h2>A lista completa</h2>
{bloco("Panelas e formas",["Jogo de panelas","Panela de pressão","Frigideira pequena","Frigideira grande","Caçarola","Leiteira","Fervedor","Wok","Cuscuzeira","Panela de arroz","Forma de bolo","Forma de pudim","Assadeira grande","Assadeira pequena","Forma de pizza","Refratário de vidro","Travessa de cerâmica","Forma de muffin"])}
{bloco("Eletroportáteis",["Liquidificador","Batedeira","Air fryer","Sanduicheira","Cafeteira","Chaleira elétrica","Mixer","Processador","Espremedor de frutas","Pipoqueira","Grill","Panela elétrica de arroz","Torradeira","Micro-ondas","Forno elétrico","Balança de cozinha"])}
{bloco("Utensílios",["Concha","Escumadeira","Espátula","Colher de pau","Pegador de massa","Pegador de salada","Fouet","Ralador","Peneira","Descascador","Espremedor de alho","Abridor de latas","Saca-rolhas","Tesoura de cozinha","Rolo de massa","Funil","Medidores","Termômetro culinário","Porta-talheres"])}
{bloco("Facas e tábuas",["Jogo de facas","Faca de pão","Faca de chef","Afiador","Tábua de corte de madeira","Tábua de corte de polipropileno","Suporte de facas"])}
{bloco("Mesa posta",["Jogo de pratos","Pratos de sobremesa","Jogo de copos","Taças de água","Taças de vinho","Faqueiro","Jogo de xícaras","Canecas","Bowls","Jarra de suco","Garrafa térmica","Bule","Açucareiro","Manteigueira","Saleiro","Galheteiro","Travessas de servir","Saladeira","Petisqueira","Jogo americano","Toalha de mesa","Porta-guardanapos","Sousplat"])}
{bloco("Organização",["Potes herméticos","Pote de mantimentos","Porta-temperos","Organizador de geladeira","Fruteira","Porta-pão","Escorredor de louça","Lixeira de pia","Porta-detergente","Suporte de papel toalha","Cesto de pães","Porta-frios"])}
{bloco("Têxteis e acessórios",["Pano de prato","Avental","Luva térmica","Descanso de panela","Pano de copa","Tapete de cozinha","Forma de gelo","Kit churrasco","Espetos","Tábua de churrasco"])}
<h2>Dicas pra lista funcionar</h2>
{ul(["Coloque a cor ou a linha preferida (ex.: 'panelas em inox', 'utensílios de silicone') pra evitar trocas.","Deixe itens baratos em quantidade — nem todo mundo pode dar eletro.","Use uma planilha compartilhada ou um grupo pra marcar quem vai dar o quê.","Guarde a lista: ela vira as palavras do bingo no dia do chá."])}
{cta(s,"end","Da lista pro bingo em 1 minuto","Cole a lista, escolha as cores e receba bingo com cartelas únicas, quem conhece a noiva, stop, adivinhe o presente e prendas.","Ver a prévia grátis")}""",
  faq=[("O que não pode faltar na lista de chá de panela?","Jogo de panelas, frigideira, utensílios básicos (concha, espátula, colher de pau), jogo de facas, tábua, potes, panos de prato e jogo de copos."),
       ("Quantos itens colocar na lista?","Pelo menos 1,5 item por convidada, com várias faixas de preço. Para 20 convidadas, uns 30 a 40 itens."),
       ("Posso usar a lista no bingo?","Pode e deve: no Kit do Chá você cola a lista e as cartelas saem com os presentes reais da noiva.")]))
