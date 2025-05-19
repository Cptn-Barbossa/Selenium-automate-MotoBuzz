# 🏍️ MotoBuzz Automātiskā Rezerves Daļu Meklēšana

Šis projekts automatizē rezerves daļu meklēšanu trīs dažādos interneta veikalos, izmantojot **Selenium WebDriver**:

- [PartsEurope.eu](https://partseurope.eu/)
- [Mike Matthies](https://mike.matthies.de/)
- [MotonetLV.lv](https://motonetlv.lv/)

---

## 🔧 Lietošana

1. Klonē repozitoriju:

git clone https://github.com/Cptn-Barbossa/Selenium-automate-MotoBuzz.git

cd Selenium-automate-MotoBuzz

2. Izveido .env failu šajā direktorijā un ievadi piekļuves datus:

MOTOBUZZ_PARTS_USERNAME=...

MOTOBUZZ_PARTS_PASSWORD=...

MOTOBUZZ_MATTHIES_USERNAME=...

MOTOBUZZ_MATTHIES_PASSWORD=...

MOTOBUZZ_MOTONET_USERNAME=...

MOTOBUZZ_MOTONET_PASSWORD=...

3. Instalē nepieciešamās Python bibliotēkas (ieteicams izmantot virtuālo vidi):
pip install -r requirements.txt

4. Palaid programmu:
python main.py

---

✅ Funkcionalitāte:

-Automātiska pieslēgšanās katram piegādātājam

-Preces koda ievade no lietotāja

-Meklēšanas rezultātu attēlošana pārlūkā

-Atbalsts vairākām pārlūka cilnēm


---

📁 Fails .gitignore:
Projekts neiekļauj sensitīvus failus (.env) un sistēmas failus. Aizsardzība tiek nodrošināta ar .gitignore.

---

⚠️ Piezīmes:
-Nepieciešams Microsoft Edge WebDriver (msedgedriver.exe)
-Nepieciešama stabila interneta pieslēguma darbība
-Nav testēts uz citiem pārlūkiem

---
