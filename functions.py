from time import sleep
import yfinance as yf
import os


def textreader(file_name:str):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the file
    file_path = os.path.join(script_dir, file_name)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            symbols = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return symbols

def chuck(tick:str,price):
    lt=len(tick)
    lp=len(str(price))
    t=f"{tick}:{lp*' '} "
    b=f"{lt*' '} {price} "
    return (t,b)


def tape(yticks,assets:list):
    
    top=""
    bot=""

    prices={}

    for t in assets:
        try:
            prices[t]=round(yticks.tickers[t].fast_info["lastPrice"],2)
        except KeyError as kr:
            print(f"Key error: {kr}\nAsset {t} no available see if the symbol exist")
            pass


    for tik in assets:
        to,bo=chuck(tik,prices[tik])        
        top+=to
        bot+=bo
    return (top,bot)


def main():

    assets= textreader('portfolio.txt')
    ticks= yf.Tickers(assets)
    try:
        while True:
            top, bot=tape(ticks,assets)
            for l in range(0,len(top)):
                ul=top[l:] + top[:l]
                dl=bot[l:] + bot[:l]
                os.system('cls' if os.name == 'nt' else 'clear')
                print(ul,flush=True)
                print(dl,end="",flush=True)
                sleep(0.15)
    except KeyboardInterrupt:
        print("GOODBYE!!")


