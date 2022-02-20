import MainClass
from tokens import Tokens
import SecretsHolder;
from broker.Order import OrderClass

secret=SecretsHolder.SecretsHolderClass('encrypted key');

main=MainClass.MainClass();
main.run([Tokens.usdtrls],secretkey=secret);

