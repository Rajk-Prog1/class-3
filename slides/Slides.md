---
title: Függvények, Lokális és globális állapottér
description: Függvények, Lokális és globális állapottér
author: Bence Kovács
marp: true
math: mathjax
class: lead
paginate: false
footer: Prog1
size: 16:9
theme: uncover
---

# Függvények, Lokális és globális állapottér

---

# Függvény programozás

- A **függvény** egy újrafelhasználható kódrészlet, amely egy adott feladat elvégzésére szolgál.
- A függvények segítenek elkerülni a kód ismétlését és javítják a moduláris felépítést.

**Szintaxis Pythonban**:

```python
def fuggveny_nev(parameterek):
    # Kódrészlet
    return ertek
```

- A függvények fontos szerepet játszanak a programok felépítésében és szervezésében.

---

## Lokális és Globális Állapottér

- Az **állapottér** (state) az a terület, ahol a változók értékei érvényesek és elérhetők a program különböző részein.
- A programozás során fontos megérteni a **lokális** (helyi) és **globális** állapottér fogalmát.

---

## Globális Állapottér

- A globális állapottér a program minden részére kiterjed, és a globálisan definiált változók bárhonnan elérhetők a programban.
- Az ilyen változók neve globális változók.
- A globális változók elérése függvényekből is lehetséges, de módosításukhoz a global kulcsszó szükséges.

---

```python
y = 20  # Globális változó

def globalis_fuggveny():
    global y
    y = y + 5  # A globális y módosítása
    print(f"A globális y új értéke: {y}")

globalis_fuggveny()
print(f"A globális y végső értéke: {y}")
```

- Itt a global kulcsszó használatával a y változó módosítható a globalis_fuggveny függvényből.
- Globális változók azonban gyakran mellékhatásokat okoznak, mert más függvények is módosíthatják őket.

---

## Lokális Állapottér

- A **lokális állapottér** a függvényen belüli terület, ahol a változók csak az adott függvényen belül érvényesek.
- Ezek a változók **lokális változók**.
- A lokális változókat a függvény meghívásakor hozzuk létre, és amikor a függvény befejeződik, a változók megszűnnek.

---

```python
def lokalis_fuggveny():
    x = 10  # Lokális változó
    print(f"A lokális x értéke: {x}")

lokalis_fuggveny()
# A következő sor hibát okoz, mert x lokális változó:
# print(x)
```

Az x változó itt csak a lokalis_fuggveny függvényen belül létezik.

---

### Lokális és Globális Állapottér Használata

-Általában a lokális változók használata előnyös, mert megakadályozza az adatok véletlen módosítását, és a kód könnyebben karbantarthatóvá válik.
-A globális változók használata összetettebb rendszerekben veszélyes lehet, mert a program különböző részei váratlanul megváltoztathatják az értéküket.

---

### Lokális és Globális Állapot Egyszerre

- Egy függvényen belül egyszerre lehet lokális és globális változókat is kezelni, de figyelni kell az elkülönítésükre.

```python
a = 10  # Globális változó

def vegyes_fuggveny():
    a = 5  # Lokális változó, nem érinti a globális a-t
    print(f"A lokális a értéke: {a}")

vegyes_fuggveny()
print(f"A globális a értéke: {a}")
```

- A függvényen belül létezik egy a nevű lokális változó, amely nem módosítja a globális a értékét.

---

## Főhatás és mellékhatás

- A programozás során gyakran találkozunk olyan fogalmakkal, mint a **főhatás** és a **mellékhatás**, különösen a függvényekkel kapcsolatban.
- Ezeknek a fogalmaknak a megértése elengedhetetlen a tiszta és karbantartható kód írásához.

---

## Főhatás

- A függvény főhatása (főhatás) az az elsődleges eredmény, amelyet a függvény produkál.
- Programozásban ez általában az, amit a függvény visszaad
- Ha egy függvény csak a főhatásra összpontosít, akkor kiszámíthatóbb és könnyebben érthető.

```python
def osszead(a, b):
    return a + b  # Főhatás: az összeadás eredményének visszaadása
```

---

## Mellékhatás

- A mellékhatás akkor következik be, ha egy függvény valami mást csinál a visszatérési értéken kívül.
- Gyakori mellékhatások közé tartozik a globális változók módosítása, nyomtatás a konzolra, vagy fájlba írás.

---

```python
x = 10

def osszead_mellekhatas(a, b):
    global x
    x = x + (a + b)  # Mellékhatás: globális változó módosítása
    print(f"Az x új értéke: {x}")  # Mellékhatás: nyomtatás
    return a + b

osszead_mellekhatas(3, 4)
```

- Globális állapotváltozás: A függvény módosítja a globális x változót.
- Kimenet: Nyomtat a konzolra, ami nem a főhatás része.
- A mellékhatások nehezebbé teszik a függvény kiszámíthatóságát, mert külső állapotokat változtatnak meg.

---

## Tiszta Függvények Pythonban

- A tiszta függvény nem rendelkezik mellékhatásokkal. Egyetlen hatása a főhatás, azaz az érték visszaadása a bemenetek alapján.
- Ugyanazon bemenetek esetén egy tiszta függvény mindig ugyanazt az eredményt adja.

---

## A Tiszta Függvények Előnyei

- Kiszámíthatóság: Egy tiszta függvény mindig ugyanúgy viselkedik azonos bemenetekkel.
- Könnyű Tesztelhetőség: A tiszta függvények tesztelése egyszerűbb, mivel nincs mellékhatásuk, így elkülöníthetők a környezettől.
- Újrafelhasználhatóság: A tiszta függvények újra felhasználhatóak a program különböző részein anélkül, hogy nem várt következményekkel járnának.

---

## Miért Kerüljük a Mellékhatásokat?

- A mellékhatásokkal rendelkező függvények tesztelése és hibakeresése nehezebb, mert függenek a külső állapotoktól, vagy módosítják azokat.
- A tiszta függvények (mellékhatások nélkül) kiszámíthatóak és könnyebben kezelhetőek, mert csak a bemeneti paramétereken alapulnak.
- A tiszta függvények a funkcionális programozás alapkövei.

---

## Hogyan nézek a gépre - paradigma

- **imperatív**: utasításonként változtatom a program állapotát, amíg el nem érek a kívánt állapotba
  - **procedurális**: meghívható utasítássorozatok, procedúrák (függvények)
  - **struktúrált**: blokkok, elágazások, for/while struktúrák (iterációk)
  - **objektumorientált**: függvényeket, adatot, speciális típusokat egységesen objektumként tároljuk az állapotban

---

## Paradigma

| Objektum Orientált Programozás                                                       | Imperatív programozási paradigma            |
| ------------------------------------------------------------------------------------ | ------------------------------------------- |
| Nem tevékenység vagy logika, hanem objektumok, illetve adat köré építjük a programot | Lépésenként adunk választ a hogyan kérdésre |

| Imperatív OOP                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lépésenként adunk utasításokat a programnak arra, hogy egyes objektumokat hogyan manipuláljon/kezeljen. Programnak ebben a megközelítésben bármely pillanatban van állapota, amiben világos a program számára elérhető objektumok tulajdonságai és értékei. Legtöbb népszerű nyelv így közelíti meg a programokat. Pl: C++, Java, C#, PHP, Python... |
