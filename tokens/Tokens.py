from tokens.Token import TokenClass
from tokens.TokenPair import TokenPairClass

btc=TokenClass('btc', 'Bitcoin');
rls=TokenClass('rls','Iran Rial');
irt=TokenClass('IRT','Iran Toman');
tether=TokenClass('usdt','Tether');

btcrls=TokenPairClass(btc,rls,'BTCRLS');
usdtrls=TokenPairClass(tether,rls,'USDTRLS');
usdtirt=TokenPairClass(tether,irt,'USDTIRT');
btcusdt=TokenPairClass(btc,tether,'BTCUSDT');