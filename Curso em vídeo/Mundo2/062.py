# Desafio 61 melhorado
# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa deve encerrar quando o usuário informar que quer mostrar 0 termos

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contador = 1
termo = primeiro
total = 0
mais = 10  

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo}", end=' ')
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos a mais você quer mostrar? "))

print(f"Progressão finalizada com {total} termos mostrados.")
