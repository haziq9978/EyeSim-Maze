#!/usr/bin/env python3
from eye import *
import random
#define SPEED    360
#define ASPEED    45
#define THRES    175
SPEED=360
ASPEED=45
THRES=175
SAFE = 200
LCDMenu("GO","","","END")
while (KEYRead() !=KEY4):

    while (PSDGet(2)<200):

        if (PSDGet(1)>200): #JJALAN TERUS
            # if(PSDGet(2)<60): #BELAKANG SIKIT
            #         VWTurn(-1, 40)
            #         VWWait()
            #         print("A")
            VWStraight(370,500)
            VWWait()
            print("B")

            # if(PSDGet(1)<60): #BETULKAN POSITION
            #         VWStraight(-60,500)
            #         VWWait()
            #         print("C")
            print(PSDGet(2))
        else:
            if(PSDGet(1)<200 and PSDGet(2)<200): #CHECK KIRI KANAN
                # if(PSDGet(1)<60): #BELAKANG SIKIT
                #     VWStraight(-60,500)
                #     VWWait()
                #     print("D")
                VWTurn(180, 70) #PUSING BELAKANG
                VWWait()
                print("E")
            else:    
                if(PSDGet(2)>PSDGet(3)): #KIRI KOSONG
                    # if(PSDGet(1)<60): #DEPAN TAK KOSONG
                    #     VWStraight(-60,500)
                    #     VWWait()
                    #     print("F")
                    VWTurn(90, 75)
                    VWWait()
                    print("G")
                    if(PSDGet(1)<300): 
                        # if(PSDGet(1)<60):
                        #     VWStraight(-60,500)
                        #     VWWait()
                        #     print("H")
                        VWTurn(90, 75)
                        VWWait()
                        print("I")
                    else:
                        # if(PSDGet(1)<60):
                        #     VWStraight(-60,500)
                        #     VWWait()
                        #     print("J")
                        VWStraight(380,500)
                        VWWait()
                        print("K")
                else:
                    # if(PSDGet(1)<60):
                    #     VWStraight(-60,500)
                    #     VWWait()
                    #     print("L")
                    VWTurn(-90, 75)
                    VWWait()
                    print("M")
                    if(PSDGet(1)<300):
                        # if(PSDGet(1)<60):
                        #     VWStraight(-60,500)
                        #     VWWait()
                        #     print("N")
                        VWTurn(90, 75)
                        VWWait()
                        print("O")
                    else:
                        VWStraight(380,500)
                        VWWait()
                        print("P")
            #if(PSDGet(2)<200):
                #VWStraight(250,500)
               # VWWait()
    #if (PSDGet(1)>200):
       # VWStraight(70,500)  
        # if(PSDGet(1)<60):
        #     VWStraight(-60,500)
        #     VWWait()   
        #     print("Q")       
    VWTurn(90, 50)
    VWWait()
    VWStraight(380,500)
    VWWait()
    print("R")
    # if(PSDGet(1)<60):
    #     VWStraight(-60,500)
    #     VWWait()   
    #     print("S") 


    #if(PSDGet(2)>300):
    #    VWTurn(90, 90)
     #   VWWait()
    #    VWStraight(170,500)
     #   VWWait()
     #   print(PSDGet(2))
    #elif (PSDGet(1)>300):
     #   VWStraight(300,500)
     #   print(PSDGet(2))
    #else:
     #   VWTurn(180, 80)
     #   VWWait()
       