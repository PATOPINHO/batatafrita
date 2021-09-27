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
                    bot.reply_to(nome, '<code>𝘼𝙂𝙐𝘼𝙍𝘿𝙀, 𝙀𝙎𝙏𝙊𝙐 𝘽𝙐𝙎𝘾𝘼𝙉𝘿𝙊...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUADRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>• By</b>: @Machineleguasbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

🔍 𝙋𝘼𝙋𝘼 𝙇𝙀𝙂𝙐𝘼𝙎 𝙍𝙊𝘽𝙊𝙏 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$20
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$30
• 31 𝘿𝙄𝘼𝙎 = R$40

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲

✅ 𝙋𝙞𝙭
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙇𝙤𝙩𝙚𝙧𝙞𝙘𝙖
✅ 𝙏𝙚𝙙

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')
                		  		
@bot.message_handler(commands=['menu', 'help', 'start'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠ ERRADO BURRO ⚠' + '</b>')
    else:
        try:
        	menu = f'olá, <pre>{men.from_user.first_name}</pre>\n<b>VEJA MEUS COMANDOS</b>\n\n<b>🔍MENU DO BOT🔍</b>\n\n<b>🔸 TELEFONE</b>: <code>/telefone 19996101067</code>\n<b>🔸 NOME:</b>: <code>/nome CARINA ALVES MAIESKY</code>\n<b>🔸 CPF</b>: <code>/cpf 34592913892</code>\n<b>🔸 CNPJ</b>: <code>/cnpj 27865757000102</code>\n<b>🔸 BIN</b>: <code>/bin 545323</code>\n<b>🔸 VIZINHOS</b>: <code>/vizinhos 27867260854</code>\n<b>🔸 PLACA</b>: <code>/placa ATJ8617</code>\n\n<b>• By</b>: @Machineleguasbot'
        	bot.reply_to(men, menu, parse_mode='HTML')
        except:
                    bot.reply_to(men, 'ERRADO BURRO',)
                    
@bot.message_handler(commands=['vizinhos'])
def byti(men):
            chtid = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001369485386]
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtém os nomes dos vizinhos do portador do número de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

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
                            bot.reply_to(men, '<code>𝘼𝙂𝙐𝘼𝙍𝘿𝙀, 𝙀𝙎𝙏𝙊𝙐 𝘽𝙐𝙎𝘾𝘼𝙉𝘿𝙊...</code>', parse_mode='html')

                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Machineleguasbot' '</b>' , parse_mode='html')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Machineleguasbot' '</b>',
                                             parse_mode='html')
                            except:
                                bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>️', parse_mode='html')

            else:
                bot.reply_to(men, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

🔍 𝙋𝘼𝙋𝘼 𝙇𝙀𝙂𝙐𝘼𝙎 𝙍𝙊𝘽𝙊𝙏 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$20
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$30
• 31 𝘿𝙄𝘼𝙎 = R$40

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲

✅ 𝙋𝙞𝙭
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙇𝙤𝙩𝙚𝙧𝙞𝙘𝙖
✅ 𝙏𝙚𝙙

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')


@bot.message_handler(commands=['cep'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>𝘼𝙂𝙐𝘼𝙍𝘿𝙀, 𝙀𝙎𝙏𝙊𝙐 𝘽𝙐𝙎𝘾𝘼𝙉𝘿𝙊...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cep')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://viacep.com.br/ws/"+ ip +"/json", verify=False)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CEP</b> 🔍\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n\n<b>• LOCALIDADE</b>: <code>{req["localidade"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n\n<b>• IBGE</b>: <code>{req["ibge"]}</code>\n\n<b>• DDD</b>: <code>{req["ddd"]}</code>\n\n<b>• SIAFI</b>: <code>{req["siafi"]}</code>\n\n<b>• By</b>: @Machineleguasbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CEP NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

🔍 𝙋𝘼𝙋𝘼 𝙇𝙀𝙂𝙐𝘼𝙎 𝙍𝙊𝘽𝙊𝙏 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$20
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$30
• 31 𝘿𝙄𝘼𝙎 = R$40

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲

✅ 𝙋𝙞𝙭
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙇𝙤𝙩𝙚𝙧𝙞𝙘𝙖
✅ 𝙏𝙚𝙙

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')






@bot.message_handler(commands=['telefone'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>𝘼𝙂𝙐𝘼𝙍𝘿𝙀, 𝙀𝙎𝙏𝙊𝙐 𝘽𝙐𝙎𝘾𝘼𝙉𝘿𝙊...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/telefone')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.dualitybuscas.org/api_nova/telefoneastra.php?consulta=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE TELEFONE</b> 🔍\n\n<b>• TELEFONE</b>: <code>{req["TELEFONE"]}</code>\n\n<b>• By</b>: @Machineleguasbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>TELEFONE NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '<b>VOCÊ NÃO TEM AUTORIZAÇÃO</b>', parse_mode='HTML')
































































                
@bot.message_handler(commands=['placa'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>𝘼𝙂𝙐𝘼𝙍𝘿𝙀, 𝙀𝙎𝙏𝙊𝙐 𝘽𝙐𝙎𝘾𝘼𝙉𝘿𝙊...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json", verify=False)
                    req = url.json()
                    response = f'🔍<b>PLACA ENCONTRADA</b>🔍\n\n<b>• PLACA</b>: <code>{req["placa"]}</code>\n<b>• ANO</b>: <code>{req["ano"]}</code>\n<b>• CHASSI</b>: <code>{req["chassi"]}</code>\n<b>• COR</b>: <code>{req["cor"]}</code>\n<b>• DATA</b>: <code>{req["data"]}</code>\n<b>• ALERME</b>: <code>{req["dataAtualizacaoAlarme"]}</code>\n<b>• VEICULO</b>: <code>{req["dataAtualizacaoCaracteristicasVeiculo"]}</code>\n<b>• ROUBO/FURTO</b>: <code>{req["dataAtualizacaoRouboFurto"]}</code>\n<b>• MARCA</b>: <code>{req["marca"]}</code>\n<b>• MODELO</b>: <code>{req["modelo"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n<b>• SITUAÇÃO</b>: <code>{req["situacao"]}</code>\n\n<b>• By</b>: @Machineleguasbot'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                	bot.reply_to(nome, '<b>PLACA NÃO FOI ENCONTRADA</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

🔍 𝙋𝘼𝙋𝘼 𝙇𝙀𝙂𝙐𝘼𝙎 𝙍𝙊𝘽𝙊𝙏 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$20
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$30
• 31 𝘿𝙄𝘼𝙎 = R$40

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲

✅ 𝙋𝙞𝙭
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙇𝙤𝙩𝙚𝙧𝙞𝙘𝙖
✅ 𝙏𝙚𝙙

<a href='http://t.me/D4RK4NGEL'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')   		
bot.polling()
