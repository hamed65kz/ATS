import math
#https://nobitex.ir/pricing/
fee_ratio=0.35*0.01



def sell(p_sell,amount_sell,Balance_IR,amount_btc,fee_ratio):#btc to ir
    received = round(amount_sell*p_sell*(1-fee_ratio))
    fee=math.floor(amount_sell*p_sell*(fee_ratio))
    Balance_IR+=received
    amount_btc-=amount_sell
    return Balance_IR,amount_btc
def buy(p_buy,amount_buy,Balance_IR,amount_btc,fee_ratio):#ir to btc
    payment= round(amount_buy*p_buy)
    fee=round((fee_ratio)*amount_buy,6)
    Balance_IR-=payment
    amount_btc+=(amount_buy-fee)
    return Balance_IR,amount_btc
def sell_buy(p0_sell,amount_sell,Balance_IR,amount_btc,fee_ratio):
    #sell
    received = round(amount_sell*p0_sell*(1-fee_ratio),6)
    #buy
    alpha =1/(1-fee_ratio) 
    amountBuy= round(amount_sell*alpha,6) #at least
    p1_buy_th= math.floor(received/amountBuy)
    return p1_buy_th,amountBuy

def buy_sell(p0_buy,amount_buy,Balance_IR,amount_btc,fee_ratio):
    #buy
    payment = round(amount_buy*p0_buy,6)
    fee=round((fee_ratio)*amount_buy,6)
    #sell
    alpha =(1-fee_ratio) 
    amount_sell=round(amount_buy*(1-fee_ratio),6)
    p1_sell_th=round(payment/(alpha*amount_sell))
    return p1_sell_th,amount_sell

Balance_IR=0
amount_btc=0.05
#status
p0_sell=1136200000


#strategy sell and buy (decreasing)
print("0:",Balance_IR,"\t",amount_btc)
print("initial sell price:",p0_sell)
#t0 (sell)
amount_sell=amount_btc
(p1_buy,amount_buy)=sell_buy(p0_sell,amount_sell,Balance_IR,amount_btc,fee_ratio)
print("thereshold buy:",p1_buy)

(Balance_IR,amount_btc) =sell(p0_sell,amount_sell,Balance_IR,amount_btc,fee_ratio)
print("t0:",Balance_IR,"\t",amount_btc)
#t1 (buy)
(Balance_IR,amount_btc) =buy(p1_buy,amount_buy,Balance_IR,amount_btc,fee_ratio)
print("t1:",Balance_IR,"\t",amount_btc)
x= (p0_sell-p1_buy)/26000
x0= (p0_sell-p1_buy)/p1_buy
print(x,"$")

print("*"*72)

##################################################
Balance_IR=11362000
amount_btc=0.05
#status
p0_buy=1136200000

#strategy buy and sell (increasing)
print("0:",Balance_IR,"\t",amount_btc)
#t0 (buy)
amount_buy=amount_btc
(p1_sell,amount_sell)=buy_sell(p0_buy,amount_buy,Balance_IR,amount_btc,fee_ratio)
print("thereshold buy:",p0_buy)#

(Balance_IR,amount_btc) =buy(p0_buy,amount_buy,Balance_IR,amount_btc,fee_ratio)
print("t0:",Balance_IR,"\t",amount_btc)

#t1 (sell)
(Balance_IR,amount_btc) =sell(p1_sell,amount_sell,Balance_IR,amount_btc,fee_ratio)
print("t1:",Balance_IR,"\t",amount_btc)

x= (p1_sell-p0_buy)/26000
x0= (p1_sell-p0_buy)/p1_buy

print(x,"$")

