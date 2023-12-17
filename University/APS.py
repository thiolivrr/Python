import rsa
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode

# Gerar chave pública e privada
chavePub, chavePri = rsa.newkeys(2048)

# Gerar chave simétrica
chaveSim = Fernet.generate_key()
f = Fernet(chaveSim)

# Senha a ser encriptada
password = input('insira a mensagem a ser criptografada: ')

print("\nMensagem original: ", password)

# Encriptando a senha com a chave simétrica
senhaEnc = f.encrypt(password.encode('utf-8'))

# Convertendo para base64
b64SenhaEnc = b64encode(senhaEnc).decode('utf-8')

#Encriptando a chave simétrica com a chave pública
chaveSimEnc = rsa.encrypt(chaveSim, chavePub)

#Convertendo para base64
b64_chaveSimEnc = b64encode(chaveSimEnc).decode('utf-8')

# Criando payload
payload = { 'chave':b64_chaveSimEnc, 'password': b64SenhaEnc }

print("\nPayload: ", payload)

user = input("Digite a chave para descriptografar: ",)

# Descriptografando chave da base64
if payload['chave'] == user:
    chaveSimEnc = b64decode(payload['chave'])
    # Descriptografando senha da base64
    senhaEnc = b64decode(payload['password'])

    # Descriptografando a chave simétrica com a chave privada
    chaveSim = rsa.decrypt(chaveSimEnc, chavePri)

    # Descriptografando a senha 
    f = Fernet(chaveSim)
    password = f.decrypt(senhaEnc).decode('utf-8')

    print("\nSenha descriptografada: ",password)
else:
    print("Chave incorreta")


