## 4. Hoe en wat in te dienen?

Nu je alle queries ingevuld (en hopelijk getest), ben je klaar om je taak in te dienen. De deadline wordt gecommuniceerd via Toledo.

1. **Maak een leeg bestand** aan, en geef het de bestandsnaam met formaat: `achternaam_voornaam_studentennummer.py`.
    - `achternaam` verwijst naar je achternaam, bijvoorbeeld `Janssens`
    - `voornaam`  verwijst naar je achternaam, bijvoorbeeld `Patrick`
    - `studentennummer` is je studentennummer zoals vermeld op je studentenkaart, bijvoorbeeld r0123456
    -  Een goede bestandsnaam is dus bijvoorbeeld: `janssens_patrick_r0123456.py`

2. Kopieer **ALLE INGEVULDE FUNCTIES EN NIETS ANDERS** naar dit bestand. Het bevat dus _enkel en alleen_ de functies:
    - query_01(connection, column_names)
    - query_02(connection, column_names, datum_x='1980-01-16')
    - etc, etc

3. **TIP**: voor de eerste 3 queries kan je je oplossing zelfs testen via de `verification.ipynb` notebook!
    - Eerst worden je functies ingelezen vanuit het zonet aangemaakte bestand
    - Die functies worden automatisch gerund, met verschillende parameters
    - De resultaten worden opgeslagen als `.csv` files (in de `out` folder)
    - Die `.csv` files worden vergeleken met de `.csv` files van de oplossing (te vinden in de `solution` folder).
    - Elke query krijgt een score toegekend. Cf. https://en.wikipedia.org/wiki/F1_score.  
    - Al dan niet sorteren is verantwoordelijk voor 10% van je score.
    - Een kort rapport wordt weergegeven die je hints kan geven over wat er mis is met je query. 
        - TP: True Positives
        - TN: True Negatives
        - FP: False Positives
    - Dit kan je helpen om je oplossing van de eerste 3 queries te debuggen, _en_ om zeker te zijn dat je `achternaam_voornaam_studentennummer.py` bestand correct werkt.
    - Voor de overige 7 queries houden we de oplossingen geheim tot na de deadline. Daar moet je dus zelf de resultaten inspecteren om jezelf ervan te overtuigen dat deze inderdaad correct zijn.
        
4. Als je oplossing definitief is, submit je je `achternaam_voornaam_studentennummer.py` bestand via Toledo. De deadline wordt gecommuniceerd via Toledo.   

5. Nogmaals, als finale submissie verwachten we dus enkel een python bestand (e.g., `achternaam_voornaam_studentennummer.py`) dat jullie ingevulde functies bevat en niks anders. Zoals zonet uitgelegd laat de `verification.ipynb` notebook je toe om zelf te checken dat je bestand aan deze standaard voldoet. **Bijgevolg: eender welke afwijking van deze standaard is absoluut onacceptabel en zal als dusdanig behandeld worden.**  