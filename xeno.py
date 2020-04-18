l=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10]#山札

print("名前を入力してください(プレーヤー1)：")
A=input()#プレーヤー1

print("名前を入力してください(プレーヤー2)：")
B=input()#プレーヤー2

print(A,"vs",B)
input()

#A="賢太"
#B="百香"

la=[]#Aの手持ち
lb=[]#Bの手持ち
bochia=[0]#Aの使用済み
bochib=[0]#Bの使用済み

import random
a=random.choice(l)#Aの引いたカード
l.remove(a)
la.append(a)
b=random.choice(l)#Bの引いたカード
l.remove(b)
lb.append(b)
tensei=random.choice(l)#転生札
l.remove(tensei)

#print(tensei)

import sys

def end():
    if la[0]>lb[0]:
        print(A,"の勝ち！")
    elif la[0]<lb[0]:
        print(B,"の勝ち！")
    else:
        print("引き分け")
    print(A,la[0],B,lb[0],"転生札：",tensei)
    sys.exit()

def ten(o,lo,bochio):
    lo.remove(o)
    bochio.append(o)
    lo.append(tensei)
    tensei=0

def turn(o,card,bochio,bochip):

    if card == 1:
        if 1 in bochip or 1 in bochio:
            pd=random.choice(l)
            l.remove(pd)
            o.append(pd)
            print("捨てさせる札を選んでください：",o)
            pw=int(input())
            if pw==10:
                ten(o[0],o,bochio)
            else:
                o.remove(pw)
                bochio.insert(0,pw)

    if card == 2:
        print("相手のカードを予想してください：")
        guess=int(input())
        if guess==o[0]:
            if o[0]==10:
                ten(o[0],o,bochio)
            else:
                print("あなたの勝ちです",o)
                sys.exit()
        else:
            print("はずれ")
            input()

    if card == 3:
        print("相手のカードは",o)
        input()

    if card == 5:
        pd=random.choice(l)
        l.remove(pd)
        o.append(pd)
        #print(p)
        print("捨てさせる札を選んでください(l/r)")
        pw=input()
        if pw=="l":
            if o[0]==10:
                ten(o[0],o,bochio)
            else:
                bochio.insert(0,o[0])
                o.remove(o[0])
        else:
            if o[0]==10:
                ten(o[0],o,bochio)
            else:
                bochio.insert(0,o[1])
                o.remove(o[1])

    if card == 6:
        print(A,la,B,lb)
        end()

    if card == 8:
        la[0],lb[0]=lb[0],la[0]
        print(A,la,B,lb)

    if card == 9:
        pd=random.choice(l)
        l.remove(pd)
        o.append(pd)
        print("捨てさせる札を選んでください：",o)
        pw=int(input())
        if pw==10:
            print("あなたの勝ちです")
        else:
            o.remove(pw)
            bochio.insert(0,pw)

def menu(P,lp,lo,bochip,bochio):
    for _ in range(20):
        print()
    print(P,"のターン")
    if bochip[-1]==7:
        print(lp)
        if len(l)>=3:
            d1,d2,d3=random.sample(l,3)#引いたカード
            print("欲しいカードを選んでください")
            print(d1,d2,d3)
        elif len(l)==2:
            d1,d2=random.sample(l,2)#引いたカード
            print("欲しいカードを選んでください")
            print(d1,d2)
        else:
            d1=random.sample(l,1)
            print("欲しいカードを選んでください")
            print(d1)
        d0=int(input())
        l.remove(d0)#山札から引く
        lp.append(d0)#手持ちに加える
    else:
        d=random.choice(l)#引いたカード
        l.remove(d)#山札から引く
        lp.append(d)#手持ちに加える
    print(A,"墓地",bochia,B,"墓地",bochib)
    print(P,lp)
    w=int(input())#使うカード
    lp.remove(w)#手札から出す
    if bochio[-1]!=4:
        turn(lo,w,bochio,bochip)
    bochip.append(w)
    for _ in range(20):
        print()
    #print(l)
    print("相手の番です")
    input()

while len(l)>0:
    menu(A,la,lb,bochia,bochib)
    if len(l)==0:
        break
    menu(B,lb,la,bochib,bochia)
    if len(l)==0:
        break

end()

#例外の処理
