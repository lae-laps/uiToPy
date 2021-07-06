import amino

chat_lobby_erajurasica = '69688ab3-20cc-4b24-948d-532806c805cc'
chat_isla_tartaros = '64ce2b86-e4a1-42c8-bc7e-95a1e976199e'

chats = ['64ce2b86-e4a1-42c8-bc7e-95a1e976199e', '69688ab3-20cc-4b24-948d-532806c805cc']

print()
print('=========')
print('THOTH-BOT')
print('=========')


creds = {
    'email':"cifehij223@geekale.com",
    'password':"thothbotG36"
}

client = amino.Client()
client.login(**creds)

print()
print("Logged in as", client.profile.nickname)
print()

comid = '260391359'

subclient = amino.SubClient(comId=comid, profile=client.profile)

print()
print('Loged into comunity')

def enviar_mensaje(mensaje, chat):
    subclient.send_message(message=mensaje, messageType=109, chatId=chat)

mensaje = input("Mensaje: ")
veces = int(input("Número de veces: "))

num_chats = len(chats)
for x in range(veces):
    for y in range(num_chats):
        enviar_mensaje(mensaje, chats[y])
