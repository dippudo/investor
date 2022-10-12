import os
import time
import random
from sys import platform



########## DEFINING FUNCTIONS ##########

# CLEAR USER TERMINAL AFTER CHECKING THEIR OPERATING SYSTEM
def clear_terminal():

    print(platform)

    if platform == "linux" or platform == "linux2": # LINUX
        os.system("clear")

    elif platform == "darwin": # APPLE / MAC
        os.system("clear")

    elif platform == "win32": # WINDOWS
        os.system("cls")

    else:
        os.system("cls")


# PRINT A NEW LINE
def empty_line():
    print("\n")


# NEW WINDOW: CLEAR TERMINAL + ADD NEW LINE
def start_new_window():
    clear_terminal()
    empty_line()


# DISPLAY THE RULES OF THE GAME
def display_rules():
    print("+-------------------------------------------------------------------------  ABOUT THE GAME  --------------------------------------------------------------------------+")
    print("|                                                                                                                                                                     |")
    print("|    This game is an investing simulation that enables players to learn the risks and rewards involved in the decision-making and risk-taking of financial markets.   |")
    print("|                                                                                                                                                                     |")
    print("|    You will start off with a balance of $100,000 to invest and grow your money through your chosen asset(s).                                                        |")
    print("|    Your goal is to win the challenge by growing your money into $1,000,000.                                                                                         |")
    print("|                                                                                                                                                                     |")
    print("|    A fully randomised set of economic events will be presented to you, and you will be given the option to buy, hold, or sell.                                      |")
    print("|    In order to win the game, you must search for clues in the news, read between the lines, and play some hunches.                                                  |")
    print("|                                                                                                                                                                     |")
    print("|    The game will end once you have beat the challenge, or run out of money. You may type QUIT at any time to leave the game.                                        |")
    print("|                                                                                                                                                                     |")
    print("+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+")


# PRESS ANY KEY TO CONTINUE OR TYPE "QUIT" TO QUIT
def continue_or_quit():
    CorQ = input("Press any key to continue, or type 'QUIT' to quit the game.")
    CorQ_lower = CorQ.lower()

    if CorQ_lower == "quit":
        print("Come back next time when you are ready, see you soon.")
        quit()
    
    time.sleep(1)


# STOCKS DICTIONARY
stocks_dict = {
    "Apple, Inc. (AAPL)" : "168.49",
    "Microsoft Corp. (MSFT)" : "287.02",
    "Alphabet, Inc. (GOOGL)" : "118.84",
    "Amazon.com, Inc. (AMZ)" : "140.64",
    "Tesla, Inc. (TSLA)" : "859.89",
    "Berkshire Hathaway (BKR-B)" : "296.47",
    "Meta Platforms, Inc. (META)" : "177.49",
    "Netflix, Inc. (NFLX)" : "242.70"
}


# DISPLAY INVESTMENT OPTIONS
def display_stocks():
    print("+-------------------------  INVESTMENT OPTIONS  ------------------------+")
    print("|                                                                       |")
    print("+--- Ticker ----- Company ---------------------------------- Price -----+")
    print("|    AAPL         Apple, Inc.                                $168.49    |")
    print("|    MSFT         Microsoft Corp.                            $287.02    |")
    print("|    GOOGL        Alphabet, Inc. (Google)                    $118.84    |")
    print("|    AMZ          Amazon.com, Inc.                           $140.64    |")
    print("|    TSLA         Tesla, Inc.                                $859.89    |")
    print("|    BKR-B        Berkshire Hathaway, Inc.                   $296.47    |")
    print("|    META         Meta Platforms, Inc. (FKA Facebook)        $177.49    |")
    print("|    NFLX         Netflix, Inc.                              $242.70    |")
    print("|                                                                       |")
    print("+-----------------------------------------------------------------------+")


# STOCK KEYWORDS (CHECK IF INPUT IS IN THIS LIST)
stocks_keywords_list = ["aapl", "apple, inc.", "apple", "msft", "microsoft corp.", "microsoft", "googl", "alphabet", "alphabet, inc.", "google", "amz", "amazon.com", "amazon.com, inc.", "amazon", "tsla", "tesla, inc.", "tesla", "bkr-b", "berkshire hathaway, inc.", "berkshire hathaway", "berkshire", "meta", "meta platforms, inc.", "meta platforms", "meta", "nflx", "netflix, inc.", "netflix"]


# STOCK CHOICE INPUT CONVERTER
def player_investment_choice_converter(investment_choice):

    investment_choice_lower = investment_choice.lower() 

    if investment_choice_lower == "aapl" or investment_choice_lower == "apple, inc." or investment_choice_lower == "apple":
        investment_choice = "Apple, Inc. (AAPL)"
        return investment_choice
    
    elif investment_choice_lower == "msft" or investment_choice_lower == "microsoft corp." or investment_choice_lower == "microsoft":
        investment_choice = "Microsoft Corp. (MSFT)"
        return investment_choice
    
    elif investment_choice_lower == "googl" or investment_choice_lower == "alphabet" or investment_choice_lower == "alphabet, inc." or investment_choice_lower == "google":
        investment_choice = "Alphabet, Inc. (GOOGL)"
        return investment_choice
    
    elif investment_choice_lower == "amz" or investment_choice_lower == "amazon.com" or investment_choice_lower == "amazon.com, inc." or investment_choice_lower == "amazon":
        investment_choice = "Amazon.com, Inc. (AMZ)"
        return investment_choice

    elif investment_choice_lower == "tsla" or investment_choice_lower == "tesla, inc." or investment_choice_lower == "tesla":
        investment_choice = "Tesla, Inc. (TSLA)"
        return investment_choice

    elif investment_choice_lower == "bkr-b" or investment_choice_lower == "berkshire hathaway, inc." or investment_choice_lower == "berkshire" or investment_choice_lower == "berkshire hathaway":
        investment_choice = "Berkshire Hathaway (BKR-B)"
        return investment_choice

    elif investment_choice_lower == "meta" or investment_choice_lower == "meta platforms, inc." or investment_choice_lower == "meta platforms" or investment_choice_lower == "meta":
        investment_choice = "Meta Platforms, Inc. (META)"
        return investment_choice

    elif investment_choice_lower == "nflx" or investment_choice_lower == "netflix, inc." or investment_choice_lower == "netflix":
        investment_choice = "Netflix, Inc. (NFLX)"
        return investment_choice


# PLAYER INVESTMENT OPTION - ASSIGNING TO ASSET CLASS
def assign_player_investment_profile(investment_choice):
    
    if investment_choice == "Apple, Inc. (AAPL)":
        investment_choice_profile = "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services."
        return investment_choice_profile

    elif investment_choice == "Microsoft Corp. (MSFT)":
        investment_choice_profile = "Microsoft Corp. engages in the development and support of software, services, devices, and solutions."
        return investment_choice_profile

    elif investment_choice == "Alphabet, Inc. (GOOGL)":
        investment_choice_profile = "Alphabet, Inc. is a holding company, which engages in the business of acquisition and operation of different companies, such as its main internet products: ads, Android, Chrome, hardware, Google Cloud, Google Maps, Google Play, Search, and YouTube."
        return investment_choice_profile
    
    elif investment_choice == "Amazon.com, Inc. (AMZ)":
        investment_choice_profile = "Amazon.com, Inc. is a multinational technology company, which engages in the provision of online retail shopping services."
        return investment_choice_profile

    elif investment_choice == "Tesla, Inc. (TSLA)":
        investment_choice_profile = "Tesla, Inc. engages in the design, development, manufacture, and sale of fully electric vehicles and energy generation and storage systems."
        return investment_choice_profile

    elif investment_choice == "Berkshire Hathaway (BKR-B)":
        investment_choice_profile = "Berkshire Hathaway, Inc. engages in the provision of property and casualty insurance and reinsurance, utilities and energy, freight rail transportation, finance, manufacturing, and retailing services."
        return investment_choice_profile

    elif investment_choice == "Meta Platforms, Inc. (META)":
        investment_choice_profile = "Meta Platforms, Inc. engages in the development of social media applications. It builds technology that helps people connect, find communities, and grow businesses."
        return investment_choice_profile

    elif investment_choice == "Netflix, Inc. (NFLX)":
        investment_choice_profile = "Netflix, Inc. operates as a streaming entertainment service company. The firm provides subscription service streaming movies and television episodes over the internet."
        return investment_choice_profile


# INITIALISE PORTFOLIO DASHBOARD VARIABLES

# positions
pf_positions_open = 0
pf_positions_asset = "N/A"
pf_postions_shares = 0

# prices and values
pf_price_current = 0
pf_price_current_total_value = 0
pf_price_when_bought = 0
pf_price_total_acquisition_cost = 0

# balances
pf_balance_cash = 100000 #starting cash
pf_balance_investments = 0 #starting value of investments
pf_balance_investments_pnl = 0 #starting + or - of investments


# DISPLAY PLAYER PORTFOLIO
def display_player_portfolio():
    print(f"______________________________  PORTFOLIO  ______________________________\n")
    print(f"   Open positions                             {int(pf_positions_open)}\n")

    print(f"   Invested asset                             {pf_positions_asset}")
    print(f"   Number of shares                           {int(pf_postions_shares)}\n")
    
    print(f"   ($) Current price                          {format(pf_price_current, '.2f')}")
    print(f"   ($) Current total value                    {format(pf_price_current_total_value, '.2f')}")
    print(f"   ($) Price when bought                      {format(pf_price_when_bought, '.2f')}")
    print(f"   ($) Total acquisition cost                 {format(pf_price_total_acquisition_cost, '.2f')}\n")

    print(f"   ($) Current cash on hand                   {format(pf_balance_cash, '.2f')}")
    print(f"   ($) Current value of investments           {format(pf_balance_investments, '.2f')}")
    print(f"   ($) Profit / Loss                          {format(pf_balance_investments_pnl, '.2f')} \n")
    print("__________________________________________________________________________")


# PLAYER USERNAME EASTER EGG
player_username_easter_egg_dict = {
    "steve jobs": "Apple",
    "bill gates": "Microsoft",
    "larry Page": "Google",
    "sergey brin": "Google",
    "jeff bezos": "Amazon",
    "elon musk": "Tesla",
    "warren buffett": "Berkshire Hathaway",
    "charlie munger": "Berkshire Hathaway",
    "mark zuckerberg": "Facebook",
    "reed hastings": "Netflix",
    "marc randolph":"Netflix",
    "lebron james" : "the Lakers",
    "stephen curry": "the Warriors",
    "michael jordan": "the Bulls",
    "shaquille o'neal": "the Lakers",
    "ryan sean adams": "Bankless",
    "david hoffman": "Bankless",
    "vitalik buterin": "making Ethereum",
    "satoshi nakamoto": "making Bitcoin",
    "marc cuban": "investing"
    }

player_username_easter_egg_list = list(player_username_easter_egg_dict.keys())

########## INTRO ##########


clear_terminal()

username = input("Hello there! Please enter your desired username: ")

if username.lower() in player_username_easter_egg_list:

    player_username_easter_egg_company = player_username_easter_egg_dict.get(username.lower())
    print(f"\nOh hi there {username}! I did not expect to see you today...")
    print(f"Have fun playing this game, hopefully you'll find success here just like you did at {player_username_easter_egg_company}!")



print(f"""
Hello, {username}, and welcome to:

/$$                                           /$$
|__/                                          | $$
/$$ /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$
| $$| $$__  $$|  $$  /$$//$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
| $$| $$  \ $$ \  $$/$$/| $$$$$$$$|  $$$$$$   | $$    | $$  \ $$| $$  \__/
| $$| $$  | $$  \  $$$/ | $$_____/ \____  $$  | $$ /$$| $$  | $$| $$
| $$| $$  | $$   \  $/  |  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$/| $$
|__/|__/  |__/    \_/    \_______/|_______/    \___/   \______/ |__/

""")

ready_for_rules = input("Are you ready to review the rules? (yes/no): ")
ready_for_rules_lower = ready_for_rules.lower()

time.sleep(0.5)

if ready_for_rules_lower != "yes":
    empty_line()
    print("You are inexperienced and will get rekt.")
    print("Come back next time when you are ready, see you soon.")
    empty_line()
    quit()

print("> Let's begin")

print("\nFor the best experience, please make sure that you are playing this game in fullscreen.")
print("This game was coded in Python 3.10, running this game in prior Python versions may result in glitches or bugs that disrupt the gaming experience.")

empty_line()
continue_or_quit()



########## DISPLAY RULES ##########

start_new_window()

display_rules()

empty_line()
continue_or_quit()



########## DISPLLAY INVESTMENT OPTIONS ##########

start_new_window()

display_stocks()

# DISPLAY PLAYER PORTFOLIO
empty_line()

display_player_portfolio()

# INPUT INVESTMENT
empty_line()
player_investment = input("Please input the your desired stock to invest in: ")


if player_investment.lower() in stocks_keywords_list:
    player_investment_converted = player_investment_choice_converter(player_investment)

else:
    if player_investment.lower() != "quit":

        while player_investment.lower() != "quit":
            player_investment = input("Please input a valid stock ticker/name: ")

            if player_investment.lower() in stocks_keywords_list:
                player_investment_converted = player_investment_choice_converter(player_investment)
                break

            elif player_investment.lower() == "quit":
                print("Come back next time when you are ready, see you soon.")
    
    elif player_investment.lower() == "quit":
        print("Come back next time when you are ready, see you soon.")

# PRINT ONCE INVESTMENT INPUT IS VALID
print("> Processing transaction...")
time.sleep(1)
print("> Success!")
time.sleep(1)

# RETRIEVE STOCK PRICE
assigned_buyPrice = float(stocks_dict.get(player_investment_converted))

# CALCULATE SHARES BOUGHT
bought_shares = float(pf_balance_cash) / float(assigned_buyPrice)

# RETRIEVE STOCK DESCRIPTION
assigned_desc = assign_player_investment_profile(player_investment_converted)

empty_line()

print(f"You have bought {int(bought_shares)} shares of {player_investment_converted} at ${format(assigned_buyPrice, '.2f')}.")
print(assigned_desc)

time.sleep(1)



########## UPDATES PLAYER VALUES ##########

# positions
pf_positions_open = 1
pf_positions_asset = player_investment_converted
pf_postions_shares = bought_shares

# prices and values
pf_price_current = assigned_buyPrice
pf_price_current_total_value = assigned_buyPrice * pf_postions_shares
pf_price_when_bought = assigned_buyPrice
pf_price_total_acquisition_cost = pf_price_when_bought * pf_postions_shares

# balances
pf_balance_cash = 100000 - pf_price_total_acquisition_cost #starting cash
pf_balance_investments = pf_price_current_total_value # value of investments
pf_balance_investments_pnl = pf_price_total_acquisition_cost -  pf_price_current_total_value # + or - of investments

empty_line()
display_player_portfolio()


time.sleep(100)
