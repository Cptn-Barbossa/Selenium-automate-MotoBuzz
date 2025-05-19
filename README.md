# Automatizācija ar Selenium priekš Parts Europe, Mike Matthies un MotonetLV

Šis projekts automatizē preču meklēšanu Parts Europe, Mike Matthies un MotonetLV mājaslapās, izmantojot Selenium.

## Prasības

- Python 3.8 vai jaunāka versija
- Instalētas bibliotēkas no `requirements.txt`:
selenium
python-dotenv

- Edge pārlūks un atbilstošs WebDriver (msedgedriver.exe) pieejamā ceļā

## Uzstādīšana

1. Izveido failu `.env` projekta saknē un ievieto tajā savus lietotājvārdus un paroles šādā formātā:

MOTOBUZZ_PARTS_USERNAME=tu_epasts@example.com

MOTOBUZZ_PARTS_PASSWORD=parole

MOTOBUZZ_MATTHIES_USERNAME=lietotajvards

MOTOBUZZ_MATTHIES_PASSWORD=parole

MOTOBUZZ_MOTONETLV_USERNAME=lietotajvards

MOTOBUZZ_MOTONETLV_PASSWORD=parole


2. Instalē nepieciešamās atkarības:
pip install -r requirements.txt

3. Lejupielādē un uzstādi Edge WebDriver, kas atbilst tavai pārlūkprogrammas versijai, un novieto msedgedriver.exe projekta mapē vai norādi ceļu main.py failā.

Lietošana
python main.py
Ievadi preces kodu, kad programma to prasīs.

