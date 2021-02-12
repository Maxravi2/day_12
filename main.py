if __name__ == '__main__' :
    fichier = open('input_2.txt' , 'r')
    content = fichier.read()

    x=0

    monTableau = [i for i in content.split('\n')]
    for i in monTableau:
        s = i.split(' ')

        min = int(s[0].split('-')[0])
        print(min)
        max = int(s[0].split('-')[1])
        mdp = s[2]
        lettre = s[1].split(':')[0]

        nb = mdp.count(lettre)
        if min <= nb <= max:
            x = x + 1

        if int mdp [min, -1] == 'x' and int mdp [max, -1] != 'x':


            print(min)
            print(max)
            print(mdp,mdp[1])
            print(lettre)
            print(x)








