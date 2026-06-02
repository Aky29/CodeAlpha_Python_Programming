import csv 

stock_prices = {"GO":180,'INK':250,"TES":98}
amount = 0 

data = []

while True: 

    stock = input("Name of the stock(or quit): ").upper()
    if stock == "QUIT":break
    if stock in stock_prices.keys():

        number_of_stocks = int(input("how many stocks : "))
        investment = stock_prices[stock] * number_of_stocks

        data.append({"Name of stock":stock,"Number of stocks":number_of_stocks,'Investment amount':investment})

        with open("Investment.csv","w") as file:
            writer = csv.DictWriter(file,fieldnames=['Name of stock','Number of stocks','Investment amount'])
            writer.writeheader()
            writer.writerows(data)
            file.close()

    else :print("not a valid stock")

with open("Investment.csv",'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
