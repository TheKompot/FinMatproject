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

Na tvorbu prveho portfolia sme pouzili markowitzov problem avsak formulovany ako maximalizacia Sharpe ratio
* kapital nam rozdelilo iba do 17 akcii
* preto sme zmenili ohranicenia vah na interval od 0.01 do 1
* **Rocny vynos: 55.37%**
* **Rocna volatilila: 12.49%** 

Vyskusali sme pridat ohranicenie ze do 17 akcii ktore si najprv "vybral" model moze ist max 80% kapitalu, avsak pocet pouzitych akcii sa znizil 

## Rozdelenie aktiv: Geneticky algoritmus

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

## Sharpe ratio

* Markowitz : 0.553768036184104 - 0.273886 / 0.12499518714208688 = **2.23914250287054**
* GenAlg    : 0.5221685528589605- 0.273886 / 0.12175833412469572 = **2.039142163399576**  

# II. Obchodovacia faza

nakupili sme akcie 1.12.2021

12.12. - rebalansovanie GenAlg portfolia
* Na zaciatku sme do jednotlivych sektorov investovali niekolko % fin. prostriedkov. Teraz sme porovnali ako sa tieto % zmenili a rozhodli sme sa predat a nakupit akcie tak, aby sa zachovali percenta jednotlivych sektorov ako na zaciatku.
* Pozorovanie sektorov, ktore mali narast/pokles viac ako 0.5%:
  * Technology: +0.757 %
  * Healtcare: -0.796 %
  * Real Estate: -0.123 %
* V sektore Technology, prudko vzrastli akcie ORCL -> predaj 8 ks akcii (zisk 11.89 za akciu)
* V sektore Healthcare, poklesli ceny LLY a PFE -> nakup 2 ks a 4 ks akcii
* V sektore Real Estate, poklesli ceny SPG -> nakup 1 ks akcie
* Tabulky v subore rebalansovanie.

20.12. - rebalansovanie GenAlg portfolia
* postup rebalansovania rovnaky ako pri predchadzajucom rebalansovani
* Pozorovanie sektorov, ktore mali narast/pokles viac ako 0.5%:
  * Technology: -1.165 %
  * Healtcare: +1.654 %
* V sektore Technology, poklesli ceny MSFT, CRM, NVDA, ADBE -> nakup 1 ks akcii z kazdej
* V sektore Healthcare, vzrastli ceny LLY a PFE -> nakup 4 ks a 10 ks akcii
* Tabulky v subore rebalansovanie.

# III. Hodnotiaca faza
Portfolio Markowitz:
* portfólio vo viacerých úsekoch rástlo rýchlejšie ako akciový index S&P 500 (konkrétne 18 dní z pozorovaných 32 dní. V období 20.12.2021 – 30.12.2021 rástlo portfólio takmer rovnako rýchlo ako akciový index S&P 500).
* Portfólio bolo po celé obdobie v relatívnom zisku s výnimkou dňa 20.12.2021 kedy bolo v relatívnej strate 0.06%.

Portfolio GenAlg:
* portfólio s výnimkou prvých troch dní a dňa 3.1.2021 vždy rástlo rýchlejšie ako akciový index S&P 500 (konkrétne 28 dní z pozorovaných 32 dní). 
* Portfólio bolo po celé obdobie v relatívnom zisku.

|                       | Markowitz           | GenALg                  |
| :---                  |    :----:           |  :---:                  |
| Výnos po 32 dňoch     | 3.47% (3069.96 $)   |    2.92 % (2156.86)     |
| Výnos p.a.            | 54.65 %             | 45.99 %                 | 
| Ex-ante Sharpe Ratio  | 2.24                | 2.04                    | 
| Ex-post Sharpe Ratio  | 2.18                | 1.53                    | 