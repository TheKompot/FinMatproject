# Financna matematika projekt

# I. Pripravna faza

## Hodnotenie portfolia FMFI

Obdobie za ktore vyhodnocujeme data: 1.1.2021 az 1.11.2021
pocet pracovnych dni v roku aproximujeme na: 252

Mame prekonat portfolio fmfi
po analyze sme ziskali hodnoty
**Rocny vynos: 5.85%** 
**Rocna volatilita: 18.91%**

## Vyberanie aktiv

Rozhodli sme sa vyberat z akcii na indexe S&P 100
pouzili sme zoznam z  22. marca 2021
nebolo mozne stiahnut data z akcii BRK.B, HD

Zoznam akcii ktore chceme pouzit: 'GOOG', 'SPG', 'GOOGL', 'MSFT', 'GD', 'ACN', 'COP', 'F', 'BAC', 'GS',
       'NVDA', 'AIG', 'MS', 'WFC', 'ORCL', 'XOM', 'TGT', 'LOW', 'EXC', 'COST',
       'AXP', 'BK', 'JPM', 'COF', 'CSCO', 'DHR', 'UNH', 'CVS', 'LLY', 'CVX',
       'MET', 'AMT', 'CRM', 'BLK', 'RTX', 'MCD', 'TMO', 'LIN', 'ADBE', 'EMR',
       'USB', 'UPS', 'TSLA', 'PFE', 'PM'

Rozdelenie vybratych aktiv podla sektorov:
![alt text](plots/stocks_per_sector.png "rozdelenie aktiv")

Kedze ziadny sektor nieje priliz dominantny tak sme boli spokojny s vyberom aktiv

## Rozdelenie aktiv: Markowitz

Na tvorbu prveho portfolia sme pouzili markowitzov problem avsak formulovany ako minimalizacia Sharpe ratio
* kapital nam rozdelilo iba do 17 akcii
* preto sme zmenili ohranicenia vah na interval od 0.01 do 1
* **Rocny vynos: 55.37%**
* **Rocna volatilila: 12.49%** 

Vyskusali sme pridat ohranicenie ze do 17 akcii ktore si najprv "vybral" model moze ist max 80% kapitalu, avsak pocet pouzitych akcii sa znizil 

## Rozdelenie aktiv: Geneticky algoritmus:

Na tvorbu drueho portfolia chceme pouzit umelu intelgenciu. Konkretne geneticky algoritmus.

* Jedinec: vektor vah pre nejake portfolio
* Populacia: 100
* Pocitanie fitness: 
    * **sharpe ratio**
    * druha mocnina vzdialenosti od predom urcenenej cielenej volatility a vynosu
* k v k-point-crossover: 10
    * ak bolo k > 5 tak bolo celkom jedno ake zvolime
* sanca pre mutaciu: 0.01
  * mala mutacia bola dobra nie avsak nulova

Kedze musi platit ze &sum;w<sub>i</sub> = 1 tak po kazdej iteracii musime celu populaciu **normalizovat** .

## Benchmark

Moznych kanditatov na benchmark sme vybrali S&P100, S&P500 a NASDAQ100. S&P pretoze z neho sme vyberali aktiva do jednotlivych portfolii.

|    corr    | S&P100    | S&P500  |  NASDAQ100 |
| :---       |    :----: |  :---:  | ---:       |
| Markowitz  | 0.8429    | 0.8864  | 0.6435     |
| GenAlg     | 0.8465    | 0.8839  | 0.6335     |

Na zaklade korelacii sme vybrali ako benchmark **S&P500**


**TODO**
* vypocitat Sharpe ratio pomocou benchmarku
* prejst do obchodovacej fazy

# II. Obchodovacia faza
