
# Foosball Table Restoration Project

## Overview
This repository documents the restoration of a vintage foosball table, originally from a parish in Mnichovo Hradiště, transformed into a modernized, electronically enhanced version now located near Classroom 225 at the Mnichovo Hradiště Gymnasium. Initiated by the school’s principal, who sought to preserve the damaged table, the project was part of the 2024/2025 school year’s project week for the current seventh-year students (septima). Under the guidance of Mr. Rydval, the project evolved into a collaborative effort involving structural repairs, 3D printing, and electronic upgrades, including LED lighting and sound effects. The project gained local recognition, with an article published in the regional newspaper highlighting the students’ innovative work.

## Project Background
The restoration began as an initiative by the school principal to repurpose a damaged foosball table rather than discard it. Originally planned as a simple project for the gymnasium’s project week, Mr. Rydval expanded its scope and entrusted it to the seventh-year students of the 2024/2025 school year. The work was conducted during free periods, with some teachers excusing students from regular classes to support the effort.

## Development Process
The restoration was divided into three main phases, followed by a two-stage assembly process.

### Phase 1: Structural Restoration
- **Objective**: Disassemble, repair, and reinforce the table’s core structure.
- **Process**: 
  - The team dismantled the table, removing damaged wooden side panels.
  - The upper section required complete replacement due to extensive damage. Jan Studničný designed and crafted a new upper part at home in his spare time.
  - The lower section was repaired and strengthened.
- **Challenges**: The initial plan to simply repaint and reassemble was abandoned due to the table’s poor condition, necessitating a more complex rebuild.

### Phase 2: Component Refurbishment
- **Objective**: Restore or replace the table’s playing components.
- **Process**:
  - Player figurines and rods were disassembled, sanded, and treated.
  - Figurines were painted with tempera paints, which later proved unsuitable as the paint began to peel.
  - Rods were cleaned of rust, and handles were spray-painted black.
  - Old plastic components were discarded and replaced with 3D-printed alternatives.
- **Challenges**: The choice of tempera paint led to durability issues, requiring future repainting.

### Phase 3: Electronic Enhancements
- **Objective**: Add modern features to enhance gameplay.
- **Process**:
  - An ESP32 microcontroller was programmed to control LED underlighting and sound effects.
  - Two ultrasonic sensors detect ball movement, triggering sound effects through a DAC pin to speakers. Special thanks to David Pluhař for providing voice recordings for the effects.
  - The electronics were developed by Eduard Wojnar and Jan Studničný.
- **Challenges**: The initial 2A power supply was insufficient, requiring a 5V 1A micro-USB for the ESP32 and a 5V 2A source for other components.

### Assembly
- **Stage 1 (Pre-Christmas School Sleepover)**:
  - The new upper part was integrated, and the table was assembled.
  - An error occurred with rods installed 180° incorrectly, requiring correction in the next stage.
- **Stage 2**:
  - Rods were realigned and lubricated with WD-40.
  - The lower section was painted black.
  - New side bumpers were installed, LED lighting was recalibrated, and an additional sound effect was added.

## Final Result
The restored foosball table is now fully functional and located near Classroom 225 at the Mnichovo Hradiště Gymnasium. Enhanced with LED underlighting and sound effects, it provides an engaging experience for students. The project successfully gave new life to an item that would have been discarded, ensuring it serves the school community for years to come.

![Final Foosball Table](https://github.com/user-attachments/assets/a582bf9a-bcae-48f2-96ae-9f7d5a8268c4)

## Repository Contents
- Source code for the ESP32 microcontroller, including sound effect and LED control logic.
- Electrical schematic (note: upgraded from 2A to 3A power requirements):  
  ![Schematic](https://github.com/user-attachments/assets/ffdab394-dde5-4fc5-9838-746097248584)
- Images of the process:  
  - Upper part construction at Jan’s home:  
    ![Upper Part](https://github.com/user-attachments/assets/676f01e9-f48f-4127-b663-1b1811d4ab36)
  - Pre-final assembly with unpainted base and misaligned rods:  
    ![Pre-Final 1](https://github.com/user-attachments/assets/18321c85-11e2-4967-a8c5-30ecb99e5834)  
    ![Pre-Final 2](https://github.com/user-attachments/assets/d8b95602-f166-4aca-8741-7538ea89bc55)

## Media Coverage
The project was featured in a local newspaper, celebrating the students’ creativity and dedication in transforming a discarded foosball table into a modernized, interactive piece for the school.

---

# Projekt renovace fotbálku

## Přehled
Tento repozitář dokumentuje renovaci starého fotbálku pocházejícího z fary v Mnichově Hradišti, který byl přeměněn na modernizovanou verzi s elektronickými vylepšeními. Nyní je umístěn vedle učebny 225 na Gymnáziu v Mnichově Hradišti. Projekt iniciovala paní ředitelka, která nechtěla starý, poškozený fotbálek vyhodit. Původně byl plánován jako součást projektového týdne, ale pod vedením pana Rydvala se ho ujali studenti současné septimy (ročník 2024/2025). Práce probíhaly během volných hodin za podpory některých vyučujících, kteří studenty uvolňovali z výuky. O projektu vyšel článek v místních novinách, který vyzdvihl inovativní přístup studentů.

## Pozadí projektu
Renovace začala díky iniciativě paní ředitelky, která chtěla zachránit poškozený fotbálek. Původně měl být projekt součástí projektového týdne gymnázia, ale pan Rydval rozšířil jeho záběr a předal ho studentům septimy ročníku 2024/2025. Práce probíhaly ve volném čase a během uvolněných hodin.

## Proces renovace
Renovace byla rozdělena do tří hlavních fází, následovaných dvoufázovou kompletací.

### Fáze 1: Oprava konstrukce
- **Cíl**: Rozebrat, opravit a zpevnit základní konstrukci.
- **Proces**:
  - Tým rozebral fotbálek a odstranil poškozené dřevěné bočnice.
  - Horní díl musel být kompletně nahrazen kvůli rozsáhlému poškození. Jan Studničný navrhl a vyrobil nový díl doma ve svém volném čase.
  - Spodní část byla opravena a zpevněna.
- **Výzvy**: Původní plán pouze přetřít a složit byl kvůli špatnému stavu opuštěn, což vedlo k náročnější rekonstrukci.

### Fáze 2: Obnova součástek
- **Cíl**: Obnovit nebo nahradit herní komponenty.
- **Proces**:
  - Hráčské figurky a tyče byly rozebrány, obroušeny a ošetřeny.
  - Figurky byly natřeny temperovými barvami, které se později ukázaly jako nevhodné, protože se barva odlupuje.
  - Tyče byly očištěny od rzi a rukojetě nastříkány černou barvou.
  - Staré plastové díly byly vyhozeny a nahrazeny 3D tištěnými náhradami.
- **Výzvy**: Nevhodná volba temperových barev způsobila problémy s trvanlivostí nátěru.

### Fáze 3: Elektronická vylepšení
- **Cíl**: Přidat moderní prvky pro vylepšení herního zážitku.
- **Proces**:
  - Mikročip ESP32 byl naprogramován pro ovládání LED podsvícení a zvukových efektů.
  - Dvě ultrazvuková čidla detekují pohyb míčku a spouštějí zvukové efekty přes DAC pin do reproduktorů. Poděkování Davidu Pluhařovi za poskytnutí hlasových nahrávek pro efekty.
  - Elektroniku vyvíjeli Eduard Wojnar a Jan Studničný.
- **Výzvy**: Původní 2A zdroj nestačil, bylo nutné použít 5V 1A micro-USB pro ESP32 a 5V 2A zdroj pro ostatní komponenty.

### Kompletace
- **Etapa 1 (Předvánoční nocování ve škole)**:
  - Nový horní díl byl přidán a stůl sestaven.
  - Došlo k chybě, kdy byly tyče osazeny otočené o 180°, což bylo opraveno v další etapě.
- **Etapa 2**:
  - Tyče byly správně nasazeny a promazány WD-40.
  - Spodní část byla natřena černou barvou.
  - Byly osazeny nové boční odražeče, přenastaveno LED podsvícení a přidán nový zvukový efekt.

## Výsledek
Renovovaný fotbálek je nyní plně funkční a stojí vedle učebny 225 na Gymnáziu v Mnichově Hradišti. Díky LED podsvícení a zvukovým efektům nabízí studentům poutavý zážitek. Projekt úspěšně vdechl nový život předmětu, který by jinak skončil vyhozený, a bude sloužit školní komunitě ještě dlouhá léta.

![Finální fotbálek](https://github.com/user-attachments/assets/a582bf9a-bcae-48f2-96ae-9f7d5a8268c4)

## Obsah repozitáře
- Zdrojový kód pro mikročip ESP32, včetně logiky pro zvukové efekty a LED podsvícení.
- Elektrické schéma (poznámka: upgradováno z 2A na 3A):  
  ![Schéma](https://github.com/user-attachments/assets/ffdab394-dde5-4fc5-9838-746097248584)
- Fotografie z procesu:  
  - Výroba horního dílu u Honzy doma:  
    ![Horní díl](https://github.com/user-attachments/assets/676f01e9-f48f-4127-b663-1b1811d4ab36)
  - Předfinální verze bez černého spodku a s otočenými tyčemi:  
    ![Předfinální 1](https://github.com/user-attachments/assets/18321c85-11e2-4967-a8c5-30ecb99e5834)  
    ![Předfinální 2](https://github.com/user-attachments/assets/d8b95602-f166-4aca-8741-7538ea89bc55)

## Mediální pokrytí
O projektu vyšel článek v místních novinách, který oslavil kreativitu a odhodlání studentů při přeměně starého fotbálku na moderní interaktivní zařízení pro školu.

## Poděkování
Děkujeme:
- **Paní ředitelce** za iniciativu a finanční podporu.
- **Panu Rydvalovi** za vedení a koordinaci.
- **Všem vyučujícím** za flexibilitu s rozvrhem.
- **Panu školníkovi** za poskytnutí prostor a nářadí.
- **Davidu Pluhařovi** za hlasové nahrávky pro zvukové efekty.

## Přispěvatelé
Na projektu se podíleli:
- Jan Studničný
- Eduard Wojnar
- Matěj Zeman
- Vítek Salaba
- Oskar Kruman
- Michal Havlík
- Michal Kňourek
- Matyáš Koutník
- Daniel Matějů
- Vojtěch Pažout
- David Pluhař
