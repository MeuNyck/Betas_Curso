# Como Mogar um Beta! 
# Atualizado: 27/06/2026

socos = []
farmada = 0
viu = 0

print("== Tutorial de Como Mogar um Beta! ==\n")

dectdador = input("Você se considera um Beta? \n(sim/não)\n")

if dectdador == "sim":
    print("\nSEU BETA! VOCÊ É QUEM PRECISA SER MOGADO! SAIA DAQUI!\n")
    exit()
elif dectdador == "não":
    print("\nParabéns! Você é um Alpha!")
else:
    print("\nQue? favor, responder com sim ou não, seu beta...\n")
    exit()
print("Primeiro passo feito! Vamos começar o treino de verdade!\n")

print("== PASSOS DE MOGAR UM BETA! ==\n")

print("Vamos ver se você passa no teste de inteligência de um verdadeiro Alpha.\n")

beta = input("Já mogou um Beta hoje?\n")
aura = input("Já farmou aura hoje?\n")
if aura == "sim":
    farmada = int(input("Quanto de aura você farmou hoje?\n"))
sixseven = input("Você viu alguem fazendo 67 hoje?\n")
if sixseven == "sim":
    viu = int(input("Quantos betas você viu fazendo 67?\n"))
    for i in range(viu):
        muito = int(input("Quantos socos você deu nos " +str(i + 1)+ "?\n"))
        socos.append(muito)
print("\n== ULTIMA PERGUNTA! ==\n")
cb = input("Você é cuiudo, ou é macio?\n")

print("\n== RESULTADOS ==\n")

print(f"Beta: {beta}")
print(f"Aura: {aura}")
if farmada >= 10:
    print(f"Farmada: {farmada}")
else:
    print("Farmada: Não farmou")
print(f"Sixseven: {sixseven}")
if sixseven == "sim":
    print(f"Viu: {viu}")
    print(f"Socos: {socos}")
print(f"CB: {cb}")

if beta == "sim" and aura == "sim" and farmada >= 1000 and cb == "cuiudo":
    print("\nVOCÊ PASSOU, obrigado por cursar este curso.\n É sempre bom ter alphas no curso.")
if beta == "sim" and aura == "sim" and farmada >= 1000 and cb == "macio":
    print("\nVocê estava indo bem... mas você é MACIO!? QUE MERDA! VOCÊ É UM BETA! SAIA DAQUI!\n")
if beta == "sim" and aura == "sim" and farmada < 1000:
    print("\nVocê estava indo bem... mas você não farmou o suficiente! VOCÊ É UM BETA! SAIA DAQUI!\n")
if beta == "sim" and aura == "não":
    print("\nVocê estava indo bem... mas você não farmou aura hoje! Oque ocorreu?\n")
if beta == "não":
    print("\nNão mogou um beta hoje? Que estranho...\n")
if beta == "não" and aura == "sim":
    print("\nQue estranho... você farmou aura mas não mogou um beta, eu vejo traidores de longe. SAIA DAQUI!\n")
if beta == "sim" and aura == "sim" and farmada <= 1000 and cb == "macio":
    print("\nOque? Você não farmou o suficiente e é macio? Você é um BETA! SAIA DAQUI!\n")