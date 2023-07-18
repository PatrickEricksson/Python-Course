import requests


def get_fii_data(ticker):
    url = f"https://statusinvest.com.br/fundos-imobiliarios/{ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro ao obter informações do FII {ticker}.")
        return None


def balance_portfolio(fii_list, monthly_income):
    num_fiis = len(fii_list)
    percentage_per_fii = 100 / num_fiis
    portfolio = {}

    for fii in fii_list:
        data = get_fii_data(fii)
        if data is not None:
            dividend_annual = float(data["dy"])
            dividend_future = float(data["dy_ano"])
            current_quote = float(data["cotacao"])
            cota_quantity = (monthly_income / dividend_annual) / current_quote * 100 / percentage_per_fii
            portfolio[fii] = cota_quantity

    return portfolio


def main():
    num_fiis = int(input("Quantos fundos imobiliários deseja inserir na carteira? "))
    fii_list = []
    for i in range(num_fiis):
        ticker = input(f"Informe o ticker do FII {i + 1}: ")
        fii_list.append(ticker.upper())

    monthly_income = float(input("Qual a renda mensal desejada (em reais)? "))

    portfolio = balance_portfolio(fii_list, monthly_income)

    print("\nCotações e quantidade de cotas recomendadas:")
    for fii, quantity in portfolio.items():
        print(f"{fii}: Quantidade de cotas recomendadas: {quantity:.2f}")


if __name__ == "__main__":
    main()
