import telebot, requests, re, json

PRIVADO = [1858837102]
#
#
GRUPO = []
#
#
EXCEPT = []
#
#
ANONY = [] # OFF

bot = telebot.TeleBot("1951201458:AAGw09kA2tOAe2KXmHBgsWiGh8ujZA2zk_I")

@bot.message_handler(commands=['cnpj'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>ð¼ððð¼ðð¿ð, ððððð ð½ððð¾ð¼ðð¿ð...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'ð <b>CONSULTA DE CNPJ</b> ð\n\n<b>â¢ CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>â¢ MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>â¢ ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>â¢ NOME</b>: <code>{req["nome"]}</code>\n\n<b>â¢ NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>â¢ PORTE</b>: <code>{req["porte"]}</code>\n\n<b>â¢ ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>â¢ ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>â¢ CÃDIGO NATUREZA JUDICIÃRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>â¢ QUADRO DE SÃCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>â¢ LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>â¢ NÃMERO</b>: <code>{req["numero"]}</code>\n<b>â¢ COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>â¢ CEP</b>: <code>{req["cep"]}</code>\n<b>â¢ BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>â¢ MUNICÃPIO</b>: <code>{req["municipio"]}</code>\n<b>â¢ ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>â¢ TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>â¢ EMAIL</b>: <code>{req["email"]}</code>\n\n<b>â¢ By</b>: @Machineleguasbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''ð¾ððððð ðð¼ ð ððð ð¼ð¾ðððð ð¼ð ððððð ð½ðð

ð ðð¼ðð¼ ððððð¼ð ððð½ðð ð
âââââââââââââââââ
ð ð½ðð ððð:

â ð¾ððððððð¼ ð¿ð ð¾ðð
â ð¾ððððððð¼ ð¿ð ð¾ððð
â ð¾ððððððð¼ ð¿ð ðððððð
â ð¾ððððððð¼ ð¿ð ðððð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ððð¼ðð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ðð¼ðððððð
â ð¾ððððððð¼ ð¿ð ððð¼ð¾ð¼
â ð¾ððððððð¼ ð¿ð ð½ðð

âââââââââââââââââ
â ï¸ ððððððð¼ ððð¿ðð ðð ð¿ð¼ð¿ðð â ï¸

ð¨ ððð ððððððð¼ð¿ð PV ð¿ð ð½ðð ð¨
âââââââââââââââââ
ðð¼ððððð:
â¢ 1 ðððð¼ðð¼ = R$10
â¢ 2 ðððð¼ðð¼ð = R$20
â¢ 1 MÃS = R$30

ðð¼ðð¼ ððð ððððð:
â¢ 15 ð¿ðð¼ð = R$30
â¢ 31 ð¿ðð¼ð = R$40

âââââââââââââââââ
ð² ððððð¼ð ð¿ð ðð¼ðð¼ðððððð ð²

â ððð­
â ð½ð¤ð¡ðð©ð¤
â ðð¤ð©ðð§ððð
â ððð

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
âââââââââââââââââ''', parse_mode='html')
                		  		
@bot.message_handler(commands=['menu', 'help', 'start'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + 'â  ERRADO BURRO â ' + '</b>')
    else:
        try:
        	menu = f'olÃ¡, <pre>{men.from_user.first_name}</pre>\n<b>VEJA MEUS COMANDOS</b>\n\n<b>ðMENU DO BOTð</b>\n\n<b>ð¸ TELEFONE</b>: <code>/telefone 19996101067</code>\n<b>ð¸ NOME:</b>: <code>/nome CARINA ALVES MAIESKY</code>\n<b>ð¸ CPF</b>: <code>/cpf 34592913892</code>\n<b>ð¸ CNPJ</b>: <code>/cnpj 27865757000102</code>\n<b>ð¸ BIN</b>: <code>/bin 545323</code>\n<b>ð¸ VIZINHOS</b>: <code>/vizinhos 27867260854</code>\n<b>ð¸ PLACA</b>: <code>/placa ATJ8617</code>\n\n<b>â¢ By</b>: @Machineleguasbot'
        	bot.reply_to(men, menu, parse_mode='HTML')
        except:
                    bot.reply_to(men, 'ERRADO BURRO',)
                    
@bot.message_handler(commands=['vizinhos'])
def byti(men):
            chtid = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001369485386]
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtÃ©m os nomes dos vizinhos do portador do nÃºmero de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            bot.reply_to(men, '<code>ð¼ððð¼ðð¿ð, ððððð ð½ððð¾ð¼ðð¿ð...</code>', parse_mode='html')

                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' 'ðCONSULTA DE VIZINHOS ð' '</b>' + '\n\n' + '<b>' 'â¢ VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' 'â¢ By: @Machineleguasbot' '</b>' , parse_mode='html')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' 'ðCONSULTA DE VIZINHOS ð' '</b>' + '\n\n' + '<b>' 'â¢ VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' 'â¢ By: @Machineleguasbot' '</b>',
                                             parse_mode='html')
                            except:
                                bot.reply_to(men, '<b>â ï¸VIZINHOS NÃO ENCONTRADO!â ï¸</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>â ï¸VIZINHOS NÃO ENCONTRADO!â ï¸</b>ï¸', parse_mode='html')

            else:
                bot.reply_to(men, '''ð¾ððððð ðð¼ ð ððð ð¼ð¾ðððð ð¼ð ððððð ð½ðð

ð ðð¼ðð¼ ððððð¼ð ððð½ðð ð
âââââââââââââââââ
ð ð½ðð ððð:

â ð¾ððððððð¼ ð¿ð ð¾ðð
â ð¾ððððððð¼ ð¿ð ð¾ððð
â ð¾ððððððð¼ ð¿ð ðððððð
â ð¾ððððððð¼ ð¿ð ðððð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ððð¼ðð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ðð¼ðððððð
â ð¾ððððððð¼ ð¿ð ððð¼ð¾ð¼
â ð¾ððððððð¼ ð¿ð ð½ðð

âââââââââââââââââ
â ï¸ ððððððð¼ ððð¿ðð ðð ð¿ð¼ð¿ðð â ï¸

ð¨ ððð ððððððð¼ð¿ð PV ð¿ð ð½ðð ð¨
âââââââââââââââââ
ðð¼ððððð:
â¢ 1 ðððð¼ðð¼ = R$10
â¢ 2 ðððð¼ðð¼ð = R$20
â¢ 1 MÃS = R$30

ðð¼ðð¼ ððð ððððð:
â¢ 15 ð¿ðð¼ð = R$30
â¢ 31 ð¿ðð¼ð = R$40

âââââââââââââââââ
ð² ððððð¼ð ð¿ð ðð¼ðð¼ðððððð ð²

â ððð­
â ð½ð¤ð¡ðð©ð¤
â ðð¤ð©ðð§ððð
â ððð

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
âââââââââââââââââ''', parse_mode='html')


@bot.message_handler(commands=['cep'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>ð¼ððð¼ðð¿ð, ððððð ð½ððð¾ð¼ðð¿ð...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cep')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://viacep.com.br/ws/"+ ip +"/json", verify=False)
                    req = url.json()
                    response = f'ð <b>CONSULTA DE CEP</b> ð\n\n<b>â¢ CEP</b>: <code>{req["cep"]}</code>\n<b>â¢ LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n\n<b>â¢ COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>â¢ BAIRRO</b>: <code>{req["bairro"]}</code>\n\n<b>â¢ LOCALIDADE</b>: <code>{req["localidade"]}</code>\n<b>â¢ UF</b>: <code>{req["uf"]}</code>\n\n<b>â¢ IBGE</b>: <code>{req["ibge"]}</code>\n\n<b>â¢ DDD</b>: <code>{req["ddd"]}</code>\n\n<b>â¢ SIAFI</b>: <code>{req["siafi"]}</code>\n\n<b>â¢ By</b>: @Machineleguasbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CEP NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''ð¾ððððð ðð¼ ð ððð ð¼ð¾ðððð ð¼ð ððððð ð½ðð

ð ðð¼ðð¼ ððððð¼ð ððð½ðð ð
âââââââââââââââââ
ð ð½ðð ððð:

â ð¾ððððððð¼ ð¿ð ð¾ðð
â ð¾ððððððð¼ ð¿ð ð¾ððð
â ð¾ððððððð¼ ð¿ð ðððððð
â ð¾ððððððð¼ ð¿ð ðððð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ððð¼ðð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ðð¼ðððððð
â ð¾ððððððð¼ ð¿ð ððð¼ð¾ð¼
â ð¾ððððððð¼ ð¿ð ð½ðð

âââââââââââââââââ
â ï¸ ððððððð¼ ððð¿ðð ðð ð¿ð¼ð¿ðð â ï¸

ð¨ ððð ððððððð¼ð¿ð PV ð¿ð ð½ðð ð¨
âââââââââââââââââ
ðð¼ððððð:
â¢ 1 ðððð¼ðð¼ = R$10
â¢ 2 ðððð¼ðð¼ð = R$20
â¢ 1 MÃS = R$30

ðð¼ðð¼ ððð ððððð:
â¢ 15 ð¿ðð¼ð = R$30
â¢ 31 ð¿ðð¼ð = R$40

âââââââââââââââââ
ð² ððððð¼ð ð¿ð ðð¼ðð¼ðððððð ð²

â ððð­
â ð½ð¤ð¡ðð©ð¤
â ðð¤ð©ðð§ððð
â ððð

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
âââââââââââââââââ''', parse_mode='html')






@bot.message_handler(commands=['telefone'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>ð¼ððð¼ðð¿ð, ððððð ð½ððð¾ð¼ðð¿ð...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/telefone')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.dualitybuscas.org/api_nova/telefoneastra.php?consulta=' + ip)
                    req = url.json()
                    response = f'ð <b>CONSULTA DE TELEFONE</b> ð\n\n<b>â¢ TELEFONE</b>: <code>{req["TELEFONE"]}</code>\n\n<b>â¢ By</b>: @Machineleguasbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>TELEFONE NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '<b>VOCÃ NÃO TEM AUTORIZAÃÃO</b>', parse_mode='HTML')
































































                
@bot.message_handler(commands=['placa'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>ð¼ððð¼ðð¿ð, ððððð ð½ððð¾ð¼ðð¿ð...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json", verify=False)
                    req = url.json()
                    response = f'ð<b>PLACA ENCONTRADA</b>ð\n\n<b>â¢ PLACA</b>: <code>{req["placa"]}</code>\n<b>â¢ ANO</b>: <code>{req["ano"]}</code>\n<b>â¢ CHASSI</b>: <code>{req["chassi"]}</code>\n<b>â¢ COR</b>: <code>{req["cor"]}</code>\n<b>â¢ DATA</b>: <code>{req["data"]}</code>\n<b>â¢ ALERME</b>: <code>{req["dataAtualizacaoAlarme"]}</code>\n<b>â¢ VEICULO</b>: <code>{req["dataAtualizacaoCaracteristicasVeiculo"]}</code>\n<b>â¢ ROUBO/FURTO</b>: <code>{req["dataAtualizacaoRouboFurto"]}</code>\n<b>â¢ MARCA</b>: <code>{req["marca"]}</code>\n<b>â¢ MODELO</b>: <code>{req["modelo"]}</code>\n<b>â¢ MUNICÃPIO</b>: <code>{req["municipio"]}</code>\n<b>â¢ UF</b>: <code>{req["uf"]}</code>\n<b>â¢ SITUAÃÃO</b>: <code>{req["situacao"]}</code>\n\n<b>â¢ By</b>: @Machineleguasbot'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                	bot.reply_to(nome, '<b>PLACA NÃO FOI ENCONTRADA</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''ð¾ððððð ðð¼ ð ððð ð¼ð¾ðððð ð¼ð ððððð ð½ðð

ð ðð¼ðð¼ ððððð¼ð ððð½ðð ð
âââââââââââââââââ
ð ð½ðð ððð:

â ð¾ððððððð¼ ð¿ð ð¾ðð
â ð¾ððððððð¼ ð¿ð ð¾ððð
â ð¾ððððððð¼ ð¿ð ðððððð
â ð¾ððððððð¼ ð¿ð ðððð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ððð¼ðð
â ð¾ððððððð¼ ð¿ð ðððððððð
â ð¾ððððððð¼ ð¿ð ðð¼ðððððð
â ð¾ððððððð¼ ð¿ð ððð¼ð¾ð¼
â ð¾ððððððð¼ ð¿ð ð½ðð

âââââââââââââââââ
â ï¸ ððððððð¼ ððð¿ðð ðð ð¿ð¼ð¿ðð â ï¸

ð¨ ððð ððððððð¼ð¿ð PV ð¿ð ð½ðð ð¨
âââââââââââââââââ
ðð¼ððððð:
â¢ 1 ðððð¼ðð¼ = R$10
â¢ 2 ðððð¼ðð¼ð = R$20
â¢ 1 MÃS = R$30

ðð¼ðð¼ ððð ððððð:
â¢ 15 ð¿ðð¼ð = R$30
â¢ 31 ð¿ðð¼ð = R$40

âââââââââââââââââ
ð² ððððð¼ð ð¿ð ðð¼ðð¼ðððððð ð²

â ððð­
â ð½ð¤ð¡ðð©ð¤
â ðð¤ð©ðð§ððð
â ððð

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
âââââââââââââââââ''', parse_mode='html')   		
bot.polling()
