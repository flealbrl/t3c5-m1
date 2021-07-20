import os                  #IMPORT PARA USAR CÓDIGO DE LIMPAR TERMINAL
import logojogo            #IMPORT PARA PEGAR LOGO DO JOGO EM OUTRO ARQUIVO
import playsound           #IMPORT PARA PODER RODAR SONS NO JOGO
import time                #IMPORT PARA UTILIZAR TEMPO COMO ESPAÇAMENTO DE AÇOES
playsound.playsound('n01.mp3')

print()
print(f"\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n  🚀  Bem-vindo A Última Centelha do Universo.  🚀  \n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

##################### CLASSE COM SUAS FUNÇOES ↓
class Personagem():
    def __init__(self,nome, idade, genero, panico, carisma):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.carisma = carisma
        self.panico = panico

    def mostrarPergonagem(self):
        print(f"Seu nome é {self.nome} tens {self.idade} anos e seu gênero é {self.genero}.\n")
    
#### DEF'S DO CARISMA. ↓

    def aumentarCarisma(self):
        if self.carisma == 100:
            print(f"Você chegou ao nível maximo de Carisma.\nCarisma atual é {self.carisma}% ▮▮▮▮▮▮▮▮▮▮ de 100%.\n")
        elif self.carisma == 99.5:
            self.carisma += 0.5
            print(f"Você chegou ao nível maximo de Carisma.\nCarisma atual é {self.carisma}% ▮▮▮▮▮▮▮▮▮▮ de 100%.\n")
        else:         
            self.carisma += 15

    def diminuirCarisma(self):
        self.carisma -= 15
        if self.carisma <= 15 or self.carisma < 30 :
            print(f"Cuidado, você está com nível de carisma muito baixo!!!.\nCarisma atual é {self.carisma}% ▮▯▯▯▯▯▯▯▯▯ de 100%.\n")
        elif self.carisma == 0 :
            print("Atenção, você chegou a um nível CRITICO de carisma.")
                   
    def mostrarCarisma(self):
        if self.carisma >= 0  and self.carisma <= 19 :
            print(f"\nCarisma atual é {self.carisma}% ▮▯▯▯▯▯▯▯▯▯ de 100%.\n")
            if self.carisma < 3:
                print("Cuidado, você está com nível de carisma muito baixo.\n")
        elif self.carisma >= 20 and self.carisma < 29 :
            print(f"Carisma atual é {self.carisma}% ▮▮▯▯▯▯▯▯▯▯ de 100%.\n")
        elif self.carisma >= 30 and self.carisma < 39 :
            print(f"Carisma atual é {self.carisma}% ▮▮▮▯▯▯▯▯▯▯ de 100%.\n")
        elif self.carisma >= 40 and self.carisma < 49 :
            print(f"Carisma atual é {self.carisma}% ▮▮▮▮▯▯▯▯▯▯ de 100%.\n")
        elif self.carisma >= 50 and self.carisma < 59 :
            print(f"Carisma atual é {self.carisma}% ▮▮▮▮▮▯▯▯▯▯ de 100%.\n")        
        elif self.carisma >= 60 and self.carisma < 69 :
            print(f"Carisma atual é {self.carisma}% ▮▮▮▮▮▮▯▯▯▯ de 100%.\n") 
        elif self.carisma >= 70 and self.carisma < 79 :
            print(f"Carisma atual é {self.carisma}% ▮▮▮▮▮▮▮▯▯▯ de 100%.\n")
        elif self.carisma >= 80 and self.carisma < 89 :
            print(f"Carisma atual é {self.carisma}% ▮▮▮▮▮▮▮▮▯▯ de 100%.\n")
        elif self.carisma >= 90 and self.carisma <= 99 :
            print(f"Carisma atual é {self.carisma}% ▮▮▮▮▮▮▮▮▯ de 100%.\n") 
        else:
            print(f"Carisma atual é {self.carisma}% ▮▮▮▮▮▮▮▮▮▮ de 100%.\n") 

#### DEF'S DO CARISMA. ↑	

#### DEF'S DO PANICO. ↓

    def aumentarPanico(self):
        if self.panico == 100:
            print("Atenção, você chegou a um nível CRITICO de PÂNICO.")
            print(f"Você chegou ao nível maximo de pânico, você está louco e tendo alucinações...\nPânico atual é {self.panico}% ▮▮▮▮▮▮▮▮▮▮ de 100%.\n")
        elif self.panico == 99.5:
            self.panico += 5
            print("Atenção, você chegou a um nível CRITICO de PÂNICO.")
            print(f"Você chegou ao nível maximo de pânico, você está louco e tendo alucinações...\nPânico atual é {self.panico}% ▮▮▮▮▮▮▮▮▮▮ de 100%.\n")
        else:         
            self.panico += 15

    def diminuiPanico(self):
        self.panico -= 15
        if self.panico <= 15 or self.panico < 3 :
            print(f"Cuidado, você está com nível de pânico baixo, tente ficar sempre alerta!\nCarisma atual é {self.carisma}% ▮▯▯▯▯▯▯▯▯▯ de 100%.\n")
        elif self.panico == 0 :
            print("Atenção, você chegou a um nível CRITICO de pânico, redobre sua atenção.")
               
    def mostrarPanico(self):
        if self.panico >= 0  and self.panico <= 19 :
            print(f"\nPânico atual é {self.panico}% ▮▯▯▯▯▯▯▯▯▯ de 100%.")
            if self.panico < 3:
                print("Cuidado, você está com nível de pânico muito baixo.\n")
        elif self.panico >= 20 and self.panico < 29 :
            print(f"Pânico atual é {self.panico}% ▮▮▯▯▯▯▯▯▯▯ de 100%.\n")
        elif self.panico >= 30 and self.panico < 39 :
            print(f"Pânico atual é {self.panico}% ▮▮▮▯▯▯▯▯▯▯ de 100%.\n")
        elif self.panico >= 40 and self.panico < 49 :
            print(f"Pânico atual é {self.panico}% ▮▮▮▮▯▯▯▯▯▯ de 100%.\n")
        elif self.panico >= 50 and self.panico < 59 :
            print(f"Pânico atual é {self.panico}% ▮▮▮▮▮▯▯▯▯▯ de 100%.\n") 
            print("Cuidado, você está com nível de pânico muito alto.\n")       
        elif self.panico >= 60 and self.panico < 69 :
            print(f"Pânico atual é {self.panico}% ▮▮▮▮▮▮▯▯▯▯ de 100%.\n") 
            print("Cuidado, você está com nível de pânico muito alto e esta ouvindo vozes.\n") 
        elif self.panico >= 70 and self.panico < 79 :
            print(f"Pânico atual é {self.panico}% ▮▮▮▮▮▮▮▯▯▯ de 100%.\n")
            print("Cuidado, você está com nível de pânico muito alto e esta ouvindo vozes.\n")  
        elif self.panico >= 80 and self.panico < 89 :
            print(f"Pânico atual é {self.panico}% ▮▮▮▮▮▮▮▮▯▯ de 100%.\n")
            print("Cuidado, você está com nível de pânico muito alto e esta ouvindo vozes.\n") 
        elif self.panico >= 90 and self.panico <= 99 :
            print(f"Pânico atual é {self.panico}% ▮▮▮▮▮▮▮▮▯ de 100%.\n") 
            print("Cuidado, você está com nível de pânico muito alto e esta ouvindo vozes e tendo alucinações.\n")
        else:
            print(f"Pânico atual é {self.panico}% ▮▮▮▮▮▮▮▮▮▮ de 100%.\n") 
            print("Cuidado, você está com nível de pânico muito alto e esta ouvindo vozes e tendo alucinações.\n")

### DEF'S DO PANICO. ↑	

##################### CLASSE COM SUAS FUNÇOES ↑	
##################### ITENS E INVENTÁRIO ↓

class Item():
    def __init__(self, nomeItem, descricao, buff, debuff):
        self.nomeItem = nomeItem
        self.descricao = descricao
        self.buff = buff 
        self.debuff = debuff 

    def Adquirido(self):
        print(f'Você adquiriu {self.nomeItem}!')
        print(self.descricao)
        print(self.buff)
        print(self.debuff)
        item = {'Nome': self.nomeItem, 'Descrição': self.descricao, 'Buff': self.buff, 'Debuff': self.debuff}
        return item
    

class Mochila():
    def __init__(self, espaco, inventario = []):
        self.espaco = espaco
        self.inventario = inventario
    
    def getItem(self, item):
        if len(self.inventario) < self.espaco:
            self.inventario.append(item)
            print('O item foi adicionado à sua mochila.')
        elif len(self.inventario) == self.espaco:
            print('O inventário está cheio! O item anterior foi removido.')
        
    def abrirMochila(self):
        if len(self.inventario) == 0:
            print('O inventário está vazio.') 
        else:
            print(self.inventario)

bag = Mochila(5)

######### INPUT PRA PEGAR NOME, IDADE, GENERO DO PERSONAGEM QUE VAI INTERAGIR COM O GAME. ↓
nome = str(input("Digite o nome do personagem: ").strip().capitalize())
sobrenome = str(input("Digite o sobrenome do personagem(apenas um): ").strip().capitalize())
idade = int(input("Informe a idade do personagem: ").strip())
while idade < 15 or idade > 80:
    idade = int(input('Idade inválida.\nInforme a idade do personagem: ').strip())

genero = str(input("Informe o gênero: [ Masculino / Feminino ] ").strip().capitalize())
while genero != 'Masculino' and genero != 'Feminino':
            genero = str(input('Gênero inválido. Tente novamente:\nUse MASCULINO ou Use FEMININO. ').strip().capitalize())
objeto = input('Escolha seu objeto favorito:\n\n[1] - Relógio\n[2] - Abajur\n[3] - Máquina de Lavar\n\nDigite o número: ')

if objeto == '1':
    abajur = False
    relógio = True
    maquina = False
    chaos = False
    Cha = False
    oos = False
    vish = False
if objeto == '2':
    abajur = True
    relógio = False
    maquina = False
    chaos = False
    Cha = False
    oos = False
    vish = False
if objeto == '3':
    abajur = False
    relógio = False
    maquina = True
    chaos = False
    Cha = False
    oos = False
    vish = False
else:
    print('\nModo Chaos ativado')
    abajur = False
    relógio = False
    maquina = False
    chaos = True
    Cha = True
    oos = True
    vish = True
########### LISTA DE ITENS PRESENTES NO JOGO:

############### DESCIÇÃO ITENS ###############
chaveRe = Item('Ponteiro de Relógio de Pulso', f"Um ponteiro simples, para um relógio simples. Compatível com dispositivos da {sobrenome}'s Corp.", 'Sem buffs', 'Sem debuffs')
chaveAba = Item('Lâmpada de Abajur', f"Uma lâmpada especial que só funciona em abajures da {sobrenome}'s Corp!", 'Sem buffs', 'Sem debuffs')
chaveMa = Item('Amaciante Temporal', f"Para viagens mais fresquinhas. Produzido pela {sobrenome}'s Corp.", 'Carisma+', 'Sem debuffs')
revista = Item('Revista sobre Ficção Científica', 'Assuntos: Buracos Negros, Viagens Interdimensionais, Viagens Temporais, etc.', 'Você recebe um adicional de Conhecimento!', None)
caos = Item('Loop do Caos', 'Eu avisei que era uma escolha do objeto era importante, engraçadinho/a...', 'Sem buffs', 'Debuff: Loop Temporal')
relog = Item('Relógio de Pulso sem Ponteiro', f"Produto da {sobrenome}'s Corp.", 'Buff: Viajar no Tempo(requer ponteiro)', 'Sem debuffs')
abaj = Item('Abajur sem Lâmpada', f"Propriedade exclusiva da {sobrenome}'s Corp.", 'Buff: Viajar no Tempo(requer lâmpada)', 'Sem debuffs')
maqlavar = Item('Máquina de Lavar Especial', f"Faz qualquer coisa dentro dela viajar no tempo. Propriedade da {sobrenome}'s Corp.", 'Buff: Viajar no Tempo', 'Debuff: Morte Certa(requer "Amaciante Temporal" para sobreviver dentro dela.')
documento = Item('Documento de Identificação', f"Kate {sobrenome} da Silva, Gerente da {sobrenome}'s Corp.", 'Sem buffs', 'Sem debuffs')
ps5000 = Item('Playstation 5000', 'Console Cósmico', 'Sem buffs', 'Sem debuffs')
estranho = Item('Parafuso da Sorte', 'Um parafuso simples', 'Buff: Sorte(se você acreditar)', 'Sem debuffs')
############### DESCIÇÃO ITENS ###############

print("\nPersonagem gerado, dados salvos...")
time.sleep(1.7)

pessoa = Personagem(nome, idade, genero, 30, 30)

time.sleep(0.7)
os.system('cls' if os.name == 'nt' else 'clear') 

######### INPUT PRA PEGAR NOME, IDADE, GENERO DO PERSONAGEM QUE VAI INTERAGIR COM O GAME. ↑

######### INICIO DA HISTÓRIA. ↓
print(f"\nBoas vindas, {nome}.")
print()
print('A história se passa no ano de 4570. A humanidade já se desenvolveu ao ponto de deixar a Terra e\npovoar outros planetas, porém, por uma causa desconhecida, o universo, assim como toda forma de vida está morrendo.\nSeu objetivo é sair de seu planeta o mais breve possível e descobrir as razões por trás do fim do universo.')
def StatusUniverso(dias_a_menos):
    diasRestantes = (7 - dias_a_menos)
    return diasRestantes

dias_a_menos = 0
statusatual = 0
tapa = 0
salvou = 0
jogo = True
chave = False
cenoura = False
input("\nClique ENTER pra prosseguir...")

statusatual = StatusUniverso(dias_a_menos)
print()
print(f'Restam {statusatual} dias para que a última centelha do universo se extinga.\n')

time.sleep(2.0)

print('- O dia começou, você se encontra no planeta X-khara, um pouco distante do planeta Terra, \na sua cidade está um caos. A galáxia já começou a gerar uma gravidade acima do comum...')
time.sleep(3.0)

print()
print('- De repente, um meteorito médio voa em direção ao seu planeta, tendo um impacto\nmoderado, porém suficiente para assustar qualquer civil...\n')
time.sleep(3.0)

print('O que você fará nessa situação?\n')
time.sleep(1.0)

##### PERGUNTAS / PERGUNTA 1.
p1 = input('[1] - Me acalmaria, e tentaria chegar até a minha nave. Eu estou confuso/a e preciso de respostas.\n[2] - Eu correria, junto com a galera da cidade. Tá achando que vou ficar aqui?\n[3] - Essa é a oportunidade perfeita pra conseguir meu Playstation 5000, afinal, ninguém tá olhando...\n\nDigite o número que representa a sua escolha: ')
while jogo == True:
    ##### PERGUNTA 1 ABAIXO
    if p1 == '1':
        print('\nVocê fica por ali, enquanto os outros fogem.')
        time.sleep(0.2)
        print('Indo até a sua nave, um ancião se aproxima de você. Vocês haviam sido os únicos que não\nse afastaram assim que o pequeno meteoro atingiu a cidade.\n')

        print('- Ancião: Você tem muita coragem, jovem. Mas o que pensa em fazer? O universo, assim como toda a vida, está morrendo.\n')
        segundaescolhaP1 = input('[1] - "Não é da sua conta, velhote."\n[2] - "Eu aprendi que não se deve aceitar qualquer informação sem antes pesquisar e entender."\n[3] - Você fica em silêncio.\n[4] - Você agride o idoso.\n\nDigite o número que representa a sua escolha: ')
        if segundaescolhaP1 == '1':
            time.sleep(0.3)
            pessoa.diminuirCarisma()
           
            while Cha == True:
                print('O velho lhe desce a bifa na cara.')
                tapa += 1
                time.sleep(0.9)
                if tapa >= 5:
                    caos1 = input('Responda: "2+2" para sair do loop temporal')
                    if caos1 == '2+2':
                        Cha = False
                    else:
                        tapa = 0
            print('O ancião vai embora dali.')
            pessoa.diminuirCarisma()         
        elif segundaescolhaP1 == '2':
            time.sleep(0.3)
            print('\nO ancião dá um sorriso.\n- Ancião: Então você está em busca da história, não é?\n- Ancião: Nesse caso, pegue isso.\n')
            if abajur == True:
                item1 = chaveAba.Adquirido()
                bag.getItem(item1)
                chave = True
                playsound.playsound('up.mp3')
            elif relógio == True:
                item1 = chaveRe.Adquirido()
                bag.getItem(item1)
                chave = True
                playsound.playsound('up.mp3')
            elif maquina == True:
                item1 = chaveMa.Adquirido()
                bag.getItem(item1)
                chave = True
                playsound.playsound('up.mp3')
            elif chaos == True:
                print('No momento em que ele te daria um item, o mesmo acaba caindo no chão e o vento leva, incapacitando você de pegar.')
            print('\nO ancião foi embora.')
        elif segundaescolhaP1 == "3":
            time.sleep(0.3)
            print('O ancião lhe observa, um pouco distante.\nAncião: Pelo visto você não quer muito papo. Tudo bem, eu vou embora.\n')
            time.sleep(0.3)
            print('O ancião deixa um item perto de você e vai embora.○\n')
            playsound.playsound('drop.mp3')
            print('Você se aproxima, e pega o item do chão.')
            item2 = revista.Adquirido()
            bag.getItem(item2)
            playsound.playsound('up.mp3')
        elif segundaescolhaP1 == "4":
            time.sleep(0.3)
            print('\nAo tentar agredir o ancião, ele puxa uma arma a laser e te pulveriza. 🔫')
            playsound.playsound('laser.mp3')
            import gameover
            playsound.playsound('gm.mp3')
            break
                
        print('Chegando na sua nave, você percebe que há pertences estranhos, como se alguém tivesse entrado ali em outro momento.\nEsse fato te deixa angustiado.')
        print()
        time.sleep(0.4)
        print('Você dá partida nela, desesperado/a por respostas. O mundo vai acabar, então você não liga pra muita coisa.\nDo nada, você ouve ruídos em algum lugar de dentro da nave.')
        time.sleep(0.9)
        variavel = input('O que você fará?\n\n[1] - "Vou verificar o que é, naturalmente."\n[2] - "Usarei uma arma que está em cima do painel para me defender... Peraí, tem armas aqui???\n[3] - Não foi nada, deve ter sido o vento...\n\n Digite número da escolha: ')
    
        if variavel == '1':
                    print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.\n')
                    print('Salvar ela?')
                    salvar = input('[1] - Sim\n[2] - Não\n')
                    if salvar == '1':
                        print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.\n')
                        batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade\n')
                        if batata == '1': 
                            print('Sua tentativa desesperada de se defender foi fracassada e você foi assasinado.\n')
                            import gameover
                            playsound.playsound('gm.mp3')
                            break
                        elif batata == '2':
                            print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                            what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                            if what == '1':
                                pessoa.diminuirCarisma()
                                print('Você tem coragem para alguém que está sob ameaça.')
                                time.sleep(0.8)
                            elif what == '2':
                                pessoa.aumentarCarisma()
                                print('Moça: Você não parece estar mentindo.')
                                time.sleep(0.3)
                            if what == '1' or what == '2':
                                input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                                print('Ela te dá um item.')
                                print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                                time.sleep(1)
                        if relógio == True:
                            new = relog.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif abajur == True:
                            new = abaj.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif maquina == True:
                            new = maqlavar.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif chaos == True:
                            print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                            print('Ela se sente ofendida com a sua lerdeza.')
                        print('A moça sai da sala principal da nave.')
                        if chave == True and cenoura == True:
                            print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                            conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                            if conclusão == '1':
                                input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                                input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                                input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                                input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                                print('Será que a sua história acaba aqui?')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                            elif conclusão == '2':
                                print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                        else:
                            input('A versão 1.0 fica por aqui. Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break  
                    elif salvar == '2':
                        print('Você a deixou amarrada.\n')
                        time.sleep(0.4)
                        print()
                        input('Depois de horas, a nave começa a balançar. \nNaves de Políciais Espaciais te cercam por suspeitar de você em crimes de roubos.\nAPERTE ENTER PARA CONTINUAR')
                        print('Eles invadem a nave e ao encontrar uma refém em sua nave, você é detido.')   
                        import gameover
                        playsound.playsound('gm.mp3')
                        break
        elif variavel == '2': 
            print('Você pega uma arma e vai olhar o que é.')
            print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.')
            print('Salvar ela?')
            salvar = input('[1] - Sim\n[2] - Não')
            
            if salvar == '1':
                print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.')
                batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade')
                if batata == '1': 
                    print('Por ter uma arma com você, você consegue ameaçar a mesma, igualando o jogo.')
                    time.sleep(0.7)
                    print('Moça: Você tem coragem. Depois de tudo que causou...')
                elif batata == '2':
                    print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                if what == '1':
                    pessoa.diminuirCarisma()
                    print('Você tem coragem para alguém que está sob ameaça.')
                    time.sleep(0.8)
                elif what == '2':
                    pessoa.aumentarCarisma()
                    print('Moça: Você não parece estar mentindo.')
                    time.sleep(0.3)
                if what == '1' or what == '2':
                    input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                    print('Ela te dá um item.')
                    print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                    time.sleep(1)
                    if relógio == True:
                        new = relog.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif abajur == True:
                        new = abaj.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif maquina == True:
                        new = maqlavar.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif chaos == True:
                        print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                        print('Ela se sente ofendida com a sua lerdeza.')
                    print('A moça sai da sala principal da nave.')
                    if chave == True and cenoura == True:
                        print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                        conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                        if conclusão == '1':
                            input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                            input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                            input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                            input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                            print('Será que a sua história acaba aqui?')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break
                        elif conclusão == '2':
                            print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break 
                        ######

    elif p1 == '2':
        print('Correndo com os civis, você percebe que parte daquelas pessoas estão aproveitando o caos para destruir\ne saquear algumas lojas e pessoas.')
        print('O que você fará? Digite abaixo o número que representa a sua escolha.\n')
        time.sleep(0.2)
        segundaescolhaP2 = input('[1] - Começo a correr mais ainda, em pânico. Talvez eu consiga me esconder.\n[2] - Vou me unir à patifaria e roubar algumas coisas que podem ser úteis.\n[3] - Vou ajudar as pessoas saqueadas.\n[4] - Vou dar um jeito de roubar alguma nave.\n')
        if segundaescolhaP2 == '1':
            pessoa.aumentarPanico()
            print('Você está com muito medo e se afasta da multidão. Ao se afastar, você chega numa área cheia de sucatas e restos de máquinas, como um ferro-velho futurista.')
            time.sleep(0.4)
            print('O lugar infelizmente é perigoso demais, e você acaba encontrando bandidos que simplesmente atiram em você.')
            playsound.playsound('gun.mp3')
            input('Antes de morrer, você ouve os bandidos dizendo: "A culpa é toda sua!"APERTE ENTER PARA CONTINUAR')
            import gameover
            playsound.playsound('gm.mp3')
            break

        elif segundaescolhaP2 == '2':
            pessoa.diminuirCarisma()
            print('Você começa a se camuflar no meio da bagunça pra saquear os itens que deseja, mas enquanto você chega, os demais ladrões se afastam.')
            print('Nessa situação, você:')
            conf = input('[1] - Se afasta junto, para não chamar à atenção.\n\n[2] - Continua roubando, afinal, tem muitas coisas valiosas ali.')
            if conf == '1':
                print('Antes de sair, você pega um item estranho que estava no caminho.')
                sorte = estranho.Adquirido()
                bag.getItem(sorte)    
            elif conf == '2':
                print('Ao ficar, você chama a atenção de guardas que foram acionados. Eles encontram somente você no local e lhe culpam por todos os saques.')
                time.sleep(0.2)
                pessoa.diminuirCarisma()
                print('Como pena de morte, você é levado para uma nave e será lançado no vácuo do espaço.')
                import gameover
                break
        elif segundaescolhaP2 == '3':
            print('Com um lapso de coragem, você ajuda algumas pessoas que seriam saqueadas por ladrões.')
            pessoa.aumentarCarisma()
            pessoa.aumentarCarisma()
            pessoa.diminuiPanico()
            time.sleep(0.3)
            print('Entre as pessoas que você ajudou, duas delas tiveram um comportamento um tanto incomum. A primeira, era uma mulher que estava de terno, como se tivesse saído do trabalho. Ela dizia te conhecer, e parecia um tanto desnorteada. A segunda pessoa era um Cosmocientista, um termo meio futurístico para "vidente". Ele o olhava com desprezo e revolta, além de se recusar a aceitar a sua ajuda.')
            print('Faça sua escolha:')
            opa = input('[1] - Vou tentar conversar com essa moça. De onde ela me conhece?\n[2] - Quem esse Cosmocientista é? Preciso perguntar a ele.\n[3] - Vou ignorá-los e dar meu jeito de sair desse lugar.')
            time.sleep(0.2)
            print()
            print()
            input('Soldados passam por ali, levando um homem aparentemente louco para uma nave, com o intuito de jogá-lo no vácuo. Enquanto eles passavam, o homem que se debatia, exclamava: "O Universo está sendo destruído!"\nOutras pessoas não perceberam tanto, mas pra você, aquilo lhe choca um pouco.\nAté onde se sabia, o universo estava sumindo por causas naturais, mas agora, \na sua mente se abre para uma nova possibilidade.\nAperte Enter para prosseguir')
            if opa == '1':
                print('Você se aproxima da moça. Ao fazer isso, ela evita te olhar e ignora boa parte das suas perguntas, dizendo apenas estar assustada demais.')
                quest = input('Escolha:\n\n[1] - Você sai dali, buscando outro meio de sair do planeta.\n[2] - Você insiste.')
                if quest == '1':
                    print('Você saiu, procurando meios de sair dali.')
                if quest == '2':
                    print('Depois de insistir, ela simplesmente lhe diz que prometeu não lhe contar nada, se afastando.\n\n Ela sai dali correndo, deixando cair um dos documentos de identificação dela.')
                    rocambole = documento.Adquirido()
                    bag.getItem(rocambole)
                    print('Você saiu, procurando meios de sair dali.')
            if opa == '2':
                print('Ao se aproximar do homem místico, ele saca uma arma e aponta pra sua cabeça. Todos em volta se desesperam.')
                pessoa.aumentarPanico()
                pessoa.aumentarPanico()
                print('Cosmocientista: Venha comigo. Agora.')
                reagir = input('Você percebe que ele não é mais àgil do que você.\nReagir?\n\n[1]- Sim\n[2] - Não')
                if reagir == '1':
                    print('Ao tentar reagir, você falha. Ele pode ser menos ágil, mas tem uma arma. Não se deve reagir a situações assim.')
                    print('Ele atira em você, com uma arma mais convencional, nada futurista. Antes de morrer, você ouve uma frase dele um tanto quanto intrigante: "Se você vai morrer agora... É bom que aja da maneira certa na próxima vez..."')
                    playsound.playsound('gun.mp3')
                    import gameover
                    playsound.playsound('gm.mp3')
                    break
                elif reagir == '2':    
                    print('Sem que você reaja, ele consegue te levar até uma nave, e chegando lá, tira a arma da sua cabeça.')
                    print()
                    print('Cosmocientista: Eu não sou obrigado a lhe dar dicas, mas acho que deveria ficar com isso.')
                    if abajur == True:
                        item1 = chaveAba.Adquirido()
                        bag.getItem(item1)
                        chave = True
                        playsound.playsound('up.mp3')
                    elif relógio == True:
                        item1 = chaveRe.Adquirido()
                        bag.getItem(item1)
                        chave = True
                        playsound.playsound('up.mp3')
                    elif maquina == True:
                        item1 = chaveMa.Adquirido()
                        bag.getItem(item1)
                        chave = True
                        playsound.playsound('up.mp3')
                    elif chaos == True:
                        print('No momento em que ele te daria um item, o mesmo acaba caindo no chão e o vento leva, incapacitando você de pegar.')
                    ue = input('[1] - "Hã... Obrigado?"\n\n[2] - "Porque você está me ajudando do nada?"\n\n[3] - "Vai me matar aqui dentro?"')
                    time.sleep(0.2)
                    if ue == '1':
                        print('O homem sai da nave sem falar nada.')
                    elif ue == '2':
                        print('Cosmocientista: Existem algumas coisas que ninguém é capaz de deter;\nCosmocientista: Entre elas, está: A busca constante do ser humano pelo conhecimento.')
                        time.sleep(0.3)
                        print('Cosmocientista: Parece uma frase de apoio, mas não é bom ter algo que não pode ser detido, nem pela natureza.\nEssa é a resposta que você precisa obter agora.')
                        time.sleep(0.3)
                        print('O homem sai da nave.')
                    
            if opa == '3' or opa == '1':
                print('Você sai para fazer uma busca no local, e acaba encontrando um recorte de papel que lhe pode ser útil.')
                print(f"Esse papel mostra um logotipo de uma empresa conhecida, chamada {sobrenome}'s Corp.\n")
                print('O nome dessa empresa te surpreende um pouco, já que tem o seu mesmo sobrenome.\nVocê pensa em investigar sobre ela.')
                playsound.playsound('up.mp3')     
            time.sleep(0.4)
            print('Você dá partida na nave, desesperado/a por respostas. O mundo vai acabar, então você não liga pra muita coisa.\n\nDo nada, você ouve ruídos em algum lugar de dentro da nave.')
            time.sleep(0.9)
            variavel = input('O que você fará?\n\n[1] - "Vou verificar o que é, naturalmente."\n[2] - "Usarei uma arma que está em cima do painel para me defender.., Peraí, tem armas aqui???\n[3] - Não foi nada, deve ter sido o vento...\n\n Digite sua escolha: ')
            
            if variavel == '1':
                    print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.\n')
                    print('Salvar ela?')
                    salvar = input('[1] - Sim\n[2] - Não\n')
                    if salvar == '1':
                        print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.\n')
                        batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade\n')
                        if batata == '1': 
                            print('Sua tentativa desesperada de se defender foi fracassada e você foi assasinado.\n')
                            import gameover
                            playsound.playsound('gm.mp3')
                            break
                        elif batata == '2':
                            print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                            what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                            if what == '1':
                                pessoa.diminuirCarisma()
                                print('Você tem coragem para alguém que está sob ameaça.')
                                time.sleep(0.8)
                            elif what == '2':
                                pessoa.aumentarCarisma()
                                print('Moça: Você não parece estar mentindo.')
                                time.sleep(0.3)
                            if what == '1' or what == '2':
                                input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                                print('Ela te dá um item.')
                                print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                                time.sleep(1)
                        if relógio == True:
                            new = relog.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif abajur == True:
                            new = abaj.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif maquina == True:
                            new = maqlavar.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif chaos == True:
                            print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                            print('Ela se sente ofendida com a sua lerdeza.')
                        print('A moça sai da sala principal da nave.')
                        if chave == True and cenoura == True:
                            print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                            conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                            if conclusão == '1':
                                input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                                input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                                input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                                input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                                print('Será que a sua história acaba aqui?')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                            elif conclusão == '2':
                                print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                    elif salvar == '2':
                        print('Você a deixou amarrada.\n')
                        time.sleep(0.4)
                        print()
                        input('Depois de horas, a nave começa a balançar. \nNaves de Políciais Espaciais te cercam por suspeitar de você em crimes de roubos.\nAPERTE ENTER PARA CONTINUAR')
                        print('Eles invadem a nave e ao encontrar uma refém em sua nave, você é detido.')   
                        import gameover
                        playsound.playsound('gm.mp3')
                        break
        elif variavel == '2': 
            print('Você pega uma arma e vai olhar o que é.')
            print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.')
            print('Salvar ela?')
            salvar = input('[1] - Sim\n[2] - Não')
            
            if salvar == '1':
                print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.')
                batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade')
                if batata == '1': 
                    print('Por ter uma arma com você, você consegue ameaçar a mesma, igualando o jogo.')
                    time.sleep(0.7)
                    print('Moça: Você tem coragem. Depois de tudo que causou...')
                elif batata == '2':
                    print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                if what == '1':
                    pessoa.diminuirCarisma()
                    print('Você tem coragem para alguém que está sob ameaça.')
                    time.sleep(0.8)
                elif what == '2':
                    pessoa.aumentarCarisma()
                    print('Moça: Você não parece estar mentindo.')
                    time.sleep(0.3)
                if what == '1' or what == '2':
                    input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                    print('Ela te dá um item.')
                    print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                    time.sleep(1)
                    if relógio == True:
                        new = relog.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif abajur == True:
                        new = abaj.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif maquina == True:
                        new = maqlavar.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif chaos == True:
                        print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                        print('Ela se sente ofendida com a sua lerdeza.')
                    print('A moça sai da sala principal da nave.')
                    if chave == True and cenoura == True:
                        print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                        conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                        if conclusão == '1':
                            input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                            input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                            input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                            input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                            print('Será que a sua história acaba aqui?')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break
                        elif conclusão == '2':
                            print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break 
                        ######
        

        elif segundaescolhaP2 == '4':
            print('Você começa a se esgueirar pelo local, procurando por naves. \nVocê acaba encontrando um homem de porte baixo com uma chave de nave na mão, "dando mole". \n\nVocê vai roubar a chave dele?')
            time.sleep(1)
            resposta = input('[1] - Sim, eu vou.\n[2] - Não, eu não vou.')
            if resposta == '1':
                pessoa.diminuirCarisma()
                pessoa.diminuirCarisma()
                time.sleep(0.3)
                print('Você o rouba na frente de todos, fazendo com que alguns te olhem estranho, e outros tentem chamar a polícia.\n\nVocê entra na nave roubada, mas não à tempo, e então vocé é detido.')
                import gameover
                playsound.playsound('gm.mp3')
            elif resposta == '2':
                print('Você resolveu não roubar aquele homem.')
                pessoa.aumentarCarisma
                print()
                print('Você dá a incrível sorte de achar uma chave no chão!! O que ela irá abrir?')
                if abajur == True:
                    item1 = chaveAba.Adquirido()
                    bag.getItem(item1)
                    chave = True
                    playsound.playsound('up.mp3')
                elif relógio == True:
                    item1 = chaveRe.Adquirido()
                    bag.getItem(item1)
                    chave = True
                    playsound.playsound('up.mp3')
                elif maquina == True:
                    item1 = chaveMa.Adquirido()
                    bag.getItem(item1)
                    chave = True
                    playsound.playsound('up.mp3')
                elif chaos == True:
                    print('No momento em que você pegaria o item, ele simplesmente entra no chão e some. Você está alucinando?!')
                
                print()
                time.sleep(0.1)
                print('Chegando na nave, você percebe que há pertences seus ali dentro, como se a nave fosse sua.\n Isso te deixa desconfortável.')
                print()
                time.sleep(0.4)
                print('Você dá partida nela, desesperado por respostas. O mundo vai acabar, então você não liga pra muita coisa.\n\nDo nada, você ouve ruídos em algum lugar de dentro da nave.')
                time.sleep(1.2)
                variavel = input('O que você fará?\n\n[1] - "Vou verificar o que é, naturalmente." [2] - "Usarei uma arma que está em cima do painel para me defender... Peraí, tem armas aqui???\n\n[3] - Não foi nada, deve ter sido o vento...\n')
                
                if variavel == '1':
                    print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.\n')
                    print('Salvar ela?')
                    salvar = input('[1] - Sim\n[2] - Não\n')
                    if salvar == '1':
                        print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.\n')
                        batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade\n')
                        if batata == '1': 
                            print('Sua tentativa desesperada de se defender foi fracassada e você foi assasinado.\n')
                            import gameover
                            playsound.playsound('gm.mp3')
                            break
                        elif batata == '2':
                            print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                            what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                            if what == '1':
                                pessoa.diminuirCarisma()
                                print('Você tem coragem para alguém que está sob ameaça.')
                                time.sleep(0.8)
                            elif what == '2':
                                pessoa.aumentarCarisma()
                                print('Moça: Você não parece estar mentindo.')
                                time.sleep(0.3)
                            if what == '1' or what == '2':
                                input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                                print('Ela te dá um item.')
                                print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                                time.sleep(1)
                        if relógio == True:
                            new = relog.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif abajur == True:
                            new = abaj.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif maquina == True:
                            new = maqlavar.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif chaos == True:
                            print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                            print('Ela se sente ofendida com a sua lerdeza.')
                        print('A moça sai da sala principal da nave.')
                        if chave == True and cenoura == True:
                            print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                            conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                            if conclusão == '1':
                                input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                                input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                                input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                                input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                                print('Será que a sua história acaba aqui?')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                            elif conclusão == '2':
                                print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                    elif salvar == '2':
                        print('Você a deixou amarrada.\n')
                        time.sleep(0.4)
                        print()
                        input('Depois de horas, a nave começa a balançar. \nNaves de Políciais Espaciais te cercam por suspeitar de você em crimes de roubos.\nAPERTE ENTER PARA CONTINUAR')
                        print('Eles invadem a nave e ao encontrar uma refém em sua nave, você é detido.')   
                        import gameover
                        playsound.playsound('gm.mp3')
                        break
        elif variavel == '2': 
            print('Você pega uma arma e vai olhar o que é.')
            print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.')
            print('Salvar ela?')
            salvar = input('[1] - Sim\n[2] - Não')
            
            if salvar == '1':
                print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.')
                batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade')
                if batata == '1': 
                    print('Por ter uma arma com você, você consegue ameaçar a mesma, igualando o jogo.')
                    time.sleep(0.7)
                    print('Moça: Você tem coragem. Depois de tudo que causou...')
                elif batata == '2':
                    print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                if what == '1':
                    pessoa.diminuirCarisma()
                    print('Você tem coragem para alguém que está sob ameaça.')
                    time.sleep(0.8)
                elif what == '2':
                    pessoa.aumentarCarisma()
                    print('Moça: Você não parece estar mentindo.')
                    time.sleep(0.3)
                if what == '1' or what == '2':
                    input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                    print('Ela te dá um item.')
                    print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                    time.sleep(1)
                    if relógio == True:
                        new = relog.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif abajur == True:
                        new = abaj.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif maquina == True:
                        new = maqlavar.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif chaos == True:
                        print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                        print('Ela se sente ofendida com a sua lerdeza.')
                    print('A moça sai da sala principal da nave.')
                    if chave == True and cenoura == True:
                        print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                        conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                        if conclusão == '1':
                            input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                            input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                            input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                            input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                            print('Será que a sua história acaba aqui?')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break
                        elif conclusão == '2':
                            print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break 
                        ######  

    elif p1 == '3':
        print(f"Você corre e começa a pegar o seu Play5000. Ao  olhar na embalagem, a empresa que está distribuindo o console chama-se {sobrenome}'s Corp.")
        yudi = ps5000.Adquirido()
        bag.getItem(yudi)
        pessoa.diminuirCarisma()
        print('Depois de pegar seu console enquanto poucos viam, o que você fará:?')
        escolha = input('\n[1] - Vou para o lugar que a maioria das pessoas fugiu.\n[2] - Vou pra casa.\n\nDigite sua esolha: ')
        if escolha == '1':
            print('Correndo na direção dos civis, você percebe que parte daquelas pessoas estão aproveitando o caos para destruir\ne saquear algumas lojas e pessoas.')
            print('O que você fará? Digite abaixo o número que representa a sua escolha.\n')
            time.sleep(0.2)
            segundaescolhaP2 = input('[1] - Começo a correr mais ainda, em pânico. Talvez eu consiga me esconder.\n[2] - Vou me unir à patifaria e roubar algumas coisas que podem ser úteis.\n[3] - Vou ajudar as pessoas saqueadas.\n[4] - Vou dar um jeito de roubar alguma nave.\n')
            if segundaescolhaP2 == '1':
                pessoa.aumentarPanico()
                print('Você está com muito medo e se afasta da multidão. Ao se afastar, você chega numa área cheia de sucatas e restos de máquinas, como um ferro-velho futurista.')
                time.sleep(0.4)
                print('O lugar infelizmente é perigoso demais, e você acaba encontrando bandidos que simplesmente atiram em você.')
                playsound.playsound('gun.mp3')
                input('Antes de morrer, você ouve os bandidos dizendo: "A culpa é toda sua!"APERTE ENTER PARA CONTINUAR')
                import gameover
                playsound.playsound('gm.mp3')
                break

            elif segundaescolhaP2 == '2':
                pessoa.diminuirCarisma()
                print('Você começa a se camuflar no meio da bagunça pra saquear os itens que deseja, mas enquanto você chega, os demais ladrões se afastam.')
                print('Nessa situação, você:')
                conf = input('[1] - Se afasta junto, para não chamar à atenção.\n\n[2] - Continua roubando, afinal, tem muitas coisas valiosas ali.')
                if conf == '1':
                    print('Antes de sair, você pega um item estranho que estava no caminho.')
                    sorte = estranho.Adquirido()
                    bag.getItem(sorte)    
                elif conf == '2':
                    print('Ao ficar, você chama a atenção de guardas que foram acionados. Eles encontram somente você no local e lhe culpam por todos os saques.')
                    time.sleep(0.2)
                    pessoa.diminuirCarisma()
                    print('Como pena de morte, você é levado para uma nave e será lançado no vácuo do espaço.')
                    import gameover
                    break
            elif segundaescolhaP2 == '3':
                print('Com um lapso de coragem, você ajuda algumas pessoas que seriam saqueadas por ladrões.')
                pessoa.aumentarCarisma()
                pessoa.aumentarCarisma()
                pessoa.diminuiPanico()
                time.sleep(0.3)
                print('Entre as pessoas que você ajudou, duas delas tiveram um comportamento um tanto incomum. A primeira, era uma mulher que estava de terno, como se tivesse saído do trabalho. Ela dizia te conhecer, e parecia um tanto desnorteada. A segunda pessoa era um Cosmocientista, um termo meio futurístico para "vidente". Ele o olhava com desprezo e revolta, além de se recusar a aceitar a sua ajuda.')
                print('Faça sua escolha:')
                opa = input('[1] - Vou tentar conversar com essa moça. De onde ela me conhece?\n[2] - Quem esse Cosmocientista é? Preciso perguntar a ele.\n[3] - Vou ignorá-los e dar meu jeito de sair desse lugar.')
                time.sleep(0.2)
                print()
                print()
                input('Soldados passam por ali, levando um homem aparentemente louco para uma nave, com o intuito de jogá-lo no vácuo. Enquanto eles passavam, o homem que se debatia, exclamava: "O Universo está sendo destruído!"\nOutras pessoas não perceberam tanto, mas pra você, aquilo lhe choca um pouco.\nAté onde se sabia, o universo estava sumindo por causas naturais, mas agora, \na sua mente se abre para uma nova possibilidade.\nAperte Enter para prosseguir')
                if opa == '1':
                    print('Você se aproxima da moça. Ao fazer isso, ela evita te olhar e ignora boa parte das suas perguntas, dizendo apenas estar assustada demais.')
                    quest = input('Escolha:\n\n[1] - Você sai dali, buscando outro meio de sair do planeta.\n[2] - Você insiste.')
                    if quest == '1':
                        print('Você saiu, procurando meios de sair dali.')
                    if quest == '2':
                        print('Depois de insistir, ela simplesmente lhe diz que prometeu não lhe contar nada, se afastando.\n\n Ela sai dali correndo, deixando cair um dos documentos de identificação dela.')
                        rocambole = documento.Adquirido()
                        bag.getItem(rocambole)
                        print('Você saiu, procurando meios de sair dali.')
                if opa == '2':
                    print('Ao se aproximar do homem místico, ele saca uma arma e aponta pra sua cabeça. Todos em volta se desesperam.')
                    pessoa.aumentarPanico()
                    pessoa.aumentarPanico()
                    print('Cosmocientista: Venha comigo. Agora.')
                    reagir = input('Você percebe que ele não é mais àgil do que você.\nReagir?\n\n[1]- Sim\n[2] - Não')
                    if reagir == '1':
                        print('Ao tentar reagir, você falha. Ele pode ser menos ágil, mas tem uma arma. Não se deve reagir a situações assim.')
                        print('Ele atira em você, com uma arma mais convencional, nada futurista. Antes de morrer, você ouve uma frase dele um tanto quanto intrigante: "Se você vai morrer agora... É bom que aja da maneira certa na próxima vez..."')
                        playsound.playsound('gun.mp3')
                        import gameover
                        playsound.playsound('gm.mp3')
                        break
                    elif reagir == '2':    
                        print('Sem que você reaja, ele consegue te levar até uma nave, e chegando lá, tira a arma da sua cabeça.')
                        print()
                        print('Cosmocientista: Eu não sou obrigado a lhe dar dicas, mas acho que deveria ficar com isso.')
                        if abajur == True:
                            item1 = chaveAba.Adquirido()
                            bag.getItem(item1)
                            chave = True
                            playsound.playsound('up.mp3')
                        elif relógio == True:
                            item1 = chaveRe.Adquirido()
                            bag.getItem(item1)
                            chave = True
                            playsound.playsound('up.mp3')
                        elif maquina == True:
                            item1 = chaveMa.Adquirido()
                            bag.getItem(item1)
                            chave = True
                            playsound.playsound('up.mp3')
                        elif chaos == True:
                            print('No momento em que ele te daria um item, o mesmo acaba caindo no chão e o vento leva, incapacitando você de pegar.')
                        ue = input('[1] - "Hã... Obrigado?"\n\n[2] - "Porque você está me ajudando do nada?"\n\n[3] - "Vai me matar aqui dentro?"')
                        time.sleep(0.2)
                        if ue == '1':
                            print('O homem sai da nave sem falar nada.')
                        elif ue == '2':
                            print('Cosmocientista: Existem algumas coisas que ninguém é capaz de deter;\nCosmocientista: Entre elas, está: A busca constante do ser humano pelo conhecimento.')
                            time.sleep(0.3)
                            print('Cosmocientista: Parece uma frase de apoio, mas não é bom ter algo que não pode ser detido, nem pela natureza.\nEssa é a resposta que você precisa obter agora.')
                            time.sleep(0.3)
                            print('O homem sai da nave.')
                        
                if opa == '3' or opa == '1':
                    print('Você sai para fazer uma busca no local, e acaba encontrando um recorte de papel que lhe pode ser útil.')
                    print(f"Esse papel mostra um logotipo de uma empresa conhecida, chamada {sobrenome}'s Corp.\n")
                    print('O nome dessa empresa te surpreende um pouco, já que tem o seu mesmo sobrenome.\nVocê pensa em investigar sobre ela.')
                    playsound.playsound('up.mp3')     
                time.sleep(0.4)
                print('Você dá partida na nave, desesperado/a por respostas. O mundo vai acabar, então você não liga pra muita coisa.\n\nDo nada, você ouve ruídos em algum lugar de dentro da nave.')
                time.sleep(0.9)
                variavel = input('O que você fará?\n\n[1] - "Vou verificar o que é, naturalmente." [2] - "Usarei uma arma que está em cima do painel para me defender... Peraí, tem armas aqui???\n\n[3] - Não foi nada, deve ter sido o vento...\n')
                
                if variavel == '1':
                    print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.\n')
                    print('Salvar ela?')
                    salvar = input('[1] - Sim\n[2] - Não\n')
                    if salvar == '1':
                        print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.\n')
                        batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade\n')
                        if batata == '1': 
                            print('Sua tentativa desesperada de se defender foi fracassada e você foi assasinado.\n')
                            import gameover
                            playsound.playsound('gm.mp3')
                            break
                        elif batata == '2':
                            print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                            what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                            if what == '1':
                                pessoa.diminuirCarisma()
                                print('Você tem coragem para alguém que está sob ameaça.')
                                time.sleep(0.8)
                            elif what == '2':
                                pessoa.aumentarCarisma()
                                print('Moça: Você não parece estar mentindo.')
                                time.sleep(0.3)
                            if what == '1' or what == '2':
                                input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                                print('Ela te dá um item.')
                                print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                                time.sleep(1)
                        if relógio == True:
                            new = relog.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif abajur == True:
                            new = abaj.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif maquina == True:
                            new = maqlavar.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif chaos == True:
                            print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                            print('Ela se sente ofendida com a sua lerdeza.')
                        print('A moça sai da sala principal da nave.')
                        if chave == True and cenoura == True:
                            print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                            conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                            if conclusão == '1':
                                input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                                input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                                input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                                input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                                print('Será que a sua história acaba aqui?')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                            elif conclusão == '2':
                                print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                    elif salvar == '2':
                        print('Você a deixou amarrada.\n')
                        time.sleep(0.4)
                        print()
                        input('Depois de horas, a nave começa a balançar. \nNaves de Políciais Espaciais te cercam por suspeitar de você em crimes de roubos.\nAPERTE ENTER PARA CONTINUAR')
                        print('Eles invadem a nave e ao encontrar uma refém em sua nave, você é detido.')   
                        import gameover
                        playsound.playsound('gm.mp3')
                        break
                elif variavel == '2': 
                    print('Você pega uma arma e vai olhar o que é.')
                    print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.')
                    print('Salvar ela?')
                    salvar = input('[1] - Sim\n[2] - Não')
                    
            if salvar == '1':
                print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.')
                batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade')
                if batata == '1': 
                    print('Por ter uma arma com você, você consegue ameaçar a mesma, igualando o jogo.')
                    time.sleep(0.7)
                    print('Moça: Você tem coragem. Depois de tudo que causou...')
                elif batata == '2':
                    print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                if what == '1':
                    pessoa.diminuirCarisma()
                    print('Você tem coragem para alguém que está sob ameaça.')
                    time.sleep(0.8)
                elif what == '2':
                    pessoa.aumentarCarisma()
                    print('Moça: Você não parece estar mentindo.')
                    time.sleep(0.3)
                if what == '1' or what == '2':
                    input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                    print('Ela te dá um item.')
                    print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                    time.sleep(1)
                    if relógio == True:
                        new = relog.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif abajur == True:
                        new = abaj.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif maquina == True:
                        new = maqlavar.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif chaos == True:
                        print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                        print('Ela se sente ofendida com a sua lerdeza.')
                    print('A moça sai da sala principal da nave.')
                    if chave == True and cenoura == True:
                        print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                        conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                        if conclusão == '1':
                            input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                            input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                            input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                            input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                            print('Será que a sua história acaba aqui?')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break
                        elif conclusão == '2':
                            print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break 
                        ###### 
                                        
            elif segundaescolhaP2 == '4':
                print('Você começa a se esgueirar pelo local, procurando por naves. \nVocê acaba encontrando um homem de porte baixo com uma chave de nave na mão, "dando mole". \n\nVocê vai roubar a chave dele?')
                time.sleep(1)
                resposta = input('[1] - Sim, eu vou.\n[2] - Não, eu não vou.')
                if resposta == '1':
                    pessoa.diminuirCarisma()
                    pessoa.diminuirCarisma()
                    time.sleep(0.3)
                    print('Você o rouba na frente de todos, fazendo com que alguns te olhem estranho, e outros tentem chamar a polícia.\n\nVocê entra na nave roubada, mas não à tempo, e então vocé é detido.')
                    import gameover
                    playsound.playsound('gm.mp3')
                elif resposta == '2':
                    print('Você resolveu não roubar aquele homem.')
                    pessoa.aumentarCarisma
                    print()
                    print('Você dá a incrível sorte de achar uma chave no chão!! O que ela irá abrir?')
                    if abajur == True:
                        item1 = chaveAba.Adquirido()
                        bag.getItem(item1)
                        chave = True
                        playsound.playsound('up.mp3')
                    elif relógio == True:
                        item1 = chaveRe.Adquirido()
                        bag.getItem(item1)
                        chave = True
                        playsound.playsound('up.mp3')
                    elif maquina == True:
                        item1 = chaveMa.Adquirido()
                        bag.getItem(item1)
                        chave = True
                        playsound.playsound('up.mp3')
                    elif chaos == True:
                        print('No momento em que você pegaria o item, ele simplesmente entra no chão e some. Você está alucinando?!')
                    
                    print()
                    time.sleep(0.1)
                    print('Chegando na nave, você percebe que há pertences seus ali dentro, como se a nave fosse sua.\n Isso te deixa desconfortável.')
                    print()
                    time.sleep(0.4)
                    print('Você dá partida nela, desesperado por respostas. O mundo vai acabar, então você não liga pra muita coisa.\n\nDo nada, você ouve ruídos em algum lugar de dentro da nave.')
                    time.sleep(1.2)
                    variavel = input('O que você fará?\n\n[1] - "Vou verificar o que é, naturalmente." [2] - "Usarei uma arma que está em cima do painel para me defender... Peraí, tem armas aqui???\n\n[3] - Não foi nada, deve ter sido o vento...\n')
                    
                if variavel == '1':
                    print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.\n')
                    print('Salvar ela?')
                    salvar = input('[1] - Sim\n[2] - Não\n')
                    if salvar == '1':
                        print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.\n')
                        batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade\n')
                        if batata == '1': 
                            print('Sua tentativa desesperada de se defender foi fracassada e você foi assasinado.\n')
                            import gameover
                            playsound.playsound('gm.mp3')
                            break
                        elif batata == '2':
                            print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                            what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                            if what == '1':
                                pessoa.diminuirCarisma()
                                print('Você tem coragem para alguém que está sob ameaça.')
                                time.sleep(0.8)
                            elif what == '2':
                                pessoa.aumentarCarisma()
                                print('Moça: Você não parece estar mentindo.')
                                time.sleep(0.3)
                            if what == '1' or what == '2':
                                input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                                print('Ela te dá um item.')
                                print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                                time.sleep(1)
                        if relógio == True:
                            new = relog.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif abajur == True:
                            new = abaj.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif maquina == True:
                            new = maqlavar.Adquirido()
                            bag.getItem(new)
                            cenoura = True
                        elif chaos == True:
                            print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                            print('Ela se sente ofendida com a sua lerdeza.')
                        print('A moça sai da sala principal da nave.')
                        if chave == True and cenoura == True:
                            print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                            conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                            if conclusão == '1':
                                input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                                input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                                input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                                input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                                print('Será que a sua história acaba aqui?')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                            elif conclusão == '2':
                                print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                                time.sleep(0.5)
                                input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                                bag.abrirMochila()
                                input('Continua...')
                                break
                    elif salvar == '2':
                        print('Você a deixou amarrada.\n')
                        time.sleep(0.4)
                        print()
                        input('Depois de horas, a nave começa a balançar. \nNaves de Políciais Espaciais te cercam por suspeitar de você em crimes de roubos.\nAPERTE ENTER PARA CONTINUAR')
                        print('Eles invadem a nave e ao encontrar uma refém em sua nave, você é detido.')   
                        import gameover
                        playsound.playsound('gm.mp3')
                        break
                elif variavel == '2': 
                    print('Você pega uma arma e vai olhar o que é.')
                    print('Ao chegar lá, você encontra uma mulher amarrada que parece estar em pânico. Ao olhar o seu rosto, ao invés de\nse sentir segura, ela se debate ainda mais.')
                    print('Salvar ela?')
                    salvar = input('[1] - Sim\n[2] - Não')
            
            if salvar == '1':
                print('Ao ser salva, a mulher lhe golpeia, colocando uma arma na sua cabeça e estando prestes a atirar.')
                batata = input('[1] - Procurar algo próximo pra se defender\n[2] - Pedir piedade')
                if batata == '1': 
                    print('Por ter uma arma com você, você consegue ameaçar a mesma, igualando o jogo.')
                    time.sleep(0.7)
                    print('Moça: Você tem coragem. Depois de tudo que causou...')
                elif batata == '2':
                    print('Moça: Você não tem autoridade pra me pedir piedade depois do que causou, com tanta gente!')
                what = input('[1] - "Mas o que diabos eu fiz afinal??"\n[2] - "Me desculpa, mas... eu realmente não faço ideia do que está falando."\n[3] - Sei do que está falando, mas prometo fazer diferente dessa vez.')
                if what == '1':
                    pessoa.diminuirCarisma()
                    print('Você tem coragem para alguém que está sob ameaça.')
                    time.sleep(0.8)
                elif what == '2':
                    pessoa.aumentarCarisma()
                    print('Moça: Você não parece estar mentindo.')
                    time.sleep(0.3)
                if what == '1' or what == '2':
                    input(f" Moça: Bem, você se lembra pelo menos da {sobrenome}'s Corp?\nEla tira a arma da sua cabeça.\nMoça: Os seus capangas me prenderam, e olha que eu te ajudei muito. Mas pelo que tô vendo, você conseguiu voltar.\nPRESS ENTER PARA PROSSEGUIR.")
                    print('Ela te dá um item.')
                    print('Moça: Fique com isso. Podemos dizer que é um atalho.')
                    time.sleep(1)
                    if relógio == True:
                        new = relog.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif abajur == True:
                        new = abaj.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif maquina == True:
                        new = maqlavar.Adquirido()
                        bag.getItem(new)
                        cenoura = True
                    elif chaos == True:
                        print('Ela te dá um item, mas ele cai no chão e quebra, espalhando cacos.')
                        print('Ela se sente ofendida com a sua lerdeza.')
                    print('A moça sai da sala principal da nave.')
                    if chave == True and cenoura == True:
                        print('Você tem os dois componentes necessários para viajar no tempo. Meus parabéns!')
                        conclusão = input('\nViajar para o passado? [1] - Sim\n[2] - Não')
                        if conclusão == '1':
                            input("Você viaja para o passado, afim de descobrir o motivo na qual o universo está sucumbindo.\nAPERTE ENTER PARA CONTINUAR")
                            input(f"\nAo chegar lá, você descobre ser herdeiro da empresa {sobrenome}'s Corp, e usa a tecnologia deles para fazer experimentos\nno Universo, em pleno espaço sideral.\nAPERTE ENTER PARA CONTINUAR")
                            input('\nPorém, tamanha radiação cósmica causada por sua pesquisa acaba sendo A PRINCIPAL CAUSA na mudança de estrutura cósmica\ndo Universo, o fazendo se destruir aos poucos.\nAPERTE ENTER PARA CONTINUAR')
                            input('\nVocê ficou até o último dia que o universo teria, voltando no tempo após, para impedir isso, porém você perdeu suas memórias ao voltar.APERTE ENTER PARA CONTINUAR')
                            print('Será que a sua história acaba aqui?')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break
                        elif conclusão == '2':
                            print('Te espero da próxima vez! Desafios o aguardam na versão 2.0!')
                            time.sleep(0.5)
                            input('Veja como ficou seu inventário no final: APERTE ENTER PARA CONTINUAR')
                            bag.abrirMochila()
                            input('Continua...')
                            break 
        elif escolha == '2':
            print('Correndo para casa, você vê 2 homens e uma moto, eles passam por você e dão a volta...')
            time.sleep(1.8)
            print('você já não sabe o que fazer e começa a correr, mas a motocosmica é mais rápida...')
            time.sleep(1.8)
            print('Eles param do seu lado, e te roubam o PLAYSTATIO 5000, você reage e leva um tiro laser.')
            playsound.playsound('laser.mp3')
            import gameover
            break