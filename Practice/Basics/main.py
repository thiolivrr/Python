from hashlib import sha256
import rsa
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode

chave_acesso = ('HywxGnZppbZWOY9ZXF4RMGpmU6Znl6ThlZEkjxGzL6g=')
senha_armazenar = sha256(chave_acesso.encode()).digest()

senha_log = input('insira a chave de acesso: ')
hash_senha_login = sha256(senha_log.encode()).digest()

if hash_senha_login == senha_armazenar:
    print('Login bem sucedido')
else:
    print('Senha incorreta')

while True:
    print('Menu:')
    print('-'*35)
    print('1) Criptografar a mensagem')
    print('2) Descriptografar a mensagem')
    print('3) encerrar o programa')
    print('-'*35)

    escolha = int(input('Insira uma das opções acima: '))

    if escolha == 1:
        chavePub, chavePri = rsa.newkeys(2048)
        chaveSim = Fernet.generate_key()
        f = Fernet(chaveSim)


        password = input('insira a mensagem a ser criptografada: ')

        print("\nMensagem original: ", password)

        senhaEnc = f.encrypt(password.encode('utf-8'))


        b64SenhaEnc = b64encode(senhaEnc).decode('utf-8')


        chaveSimEnc = rsa.encrypt(chaveSim, chavePub)


        b64_chaveSimEnc = b64encode(chaveSimEnc).decode('utf-8')


        payload = { 'chave':b64_chaveSimEnc, 'password': b64SenhaEnc }

        print("\nPayload: ", payload)

    elif escolha == 2:
        user = input("Digite a chave para descriptografar: ",)


        if payload['chave'] == user:
            chaveSimEnc = b64decode(payload['chave'])

            senhaEnc = b64decode(payload['password'])


            chaveSim = rsa.decrypt(chaveSimEnc, chavePri)


            f = Fernet(chaveSim)
            password = f.decrypt(senhaEnc).decode('utf-8')

            print("\nSenha descriptografada: ",password)
        else:
            print("Chave incorreta")
    elif escolha == 3:
        break
    else:
        print('Escolha uma opção válida: ')
 