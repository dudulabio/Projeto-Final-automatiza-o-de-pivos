import time
from pivo import Pivo

pivo1 = Pivo(
    tipo="Pivo Central",
    
    th="Th 1", 
    
    cultura="Soja", 
    
    velocidade_pivo=float(input("Insira a velocidade do pivo em M/h: ")), 
    
    linha_pivo=float(input("Insira o alcance em linha do pivo em metros: "))

)

comprimento_circunferencia = 2 * 3.14 * pivo1.linha_pivo
tempo_volta = comprimento_circunferencia / pivo1.velocidade_pivo


print('________________________')
pivo1.imprimir()

print(f"O pivo levará {tempo_volta} horas para dar uma volta completa.")
print('________________________')



while True:
    opcao = input("Deseja ligar o pivô? (s/n): ").strip().lower()
    print('________________________')
    if opcao == 's':
        print(f"O pivô está ligado e funcionará por {tempo_volta} horas.")
        pivo1.ligar()

        
        start_time = time.time()
        while time.time() - start_time < tempo_volta * 3600:
            print("O pivô está ligado.")
            time.sleep(0.5) 

        print(f"O pivô completou o ciclo de {tempo_volta} e agora está desligado.")
        break
    elif opcao == 'n':
        print("O pivô não será ligado.")
        break
    else:
        print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")