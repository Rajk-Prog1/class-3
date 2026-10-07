---
title: Függvények és hatókör
description: Függvényhívás, paraméterek, visszatérés, hatókör és mellékhatások
author: Bence Kovács
marp: true
math: mathjax
paginate: true
footer: Prog1 – Függvények és hatókör
size: 16:9
theme: uncover
style: |
  section {
    background: #fafafa;
    color: #242a33;
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-size: 30px;
    line-height: 1.38;
    letter-spacing: 0;
    padding: 48px 64px 82px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    text-align: left;
  }
  h1, h2, h3 { color: #244c68; letter-spacing: 0; }
  h1 { font-size: 58px; line-height: 1.15; }
  h2 { font-size: 42px; line-height: 1.2; margin: 0 0 28px; }
  h3 { font-size: 32px; margin: 12px 0; }
  p { margin: 0 0 18px; }
  ul, ol { margin: 0 0 18px; padding-left: 1.25em; }
  li { margin: 8px 0; }
  strong { color: #244c68; }
  table { width: 100%; font-size: 27px; border-collapse: collapse; margin: 10px 0 20px; }
  th, td { padding: 14px 16px; text-align: left; border-bottom: 1px solid #bac5cd; }
  th { background: #eaf0f4; color: #244c68; }
  section.title { justify-content: center; text-align: center; }
  section.title h1 { margin-bottom: 28px; }
  section.title h2 { font-size: 52px; }
  section.definition { justify-content: center; text-align: center; }
  section.definition h2 { font-size: 52px; margin-bottom: 40px; }
  section.definition p { font-size: 40px; line-height: 1.45; max-width: 1000px; margin: 0 auto; }
  section.compact { font-size: 28px; }
  section.compact table { font-size: 26px; }
  section.compact th, section.compact td { padding: 9px 14px; }
  section footer {
    position: absolute; left: 64px; bottom: 25px;
    width: auto; padding: 0; margin: 0;
    font-size: 17px; color: #66737f; text-align: left;
  }
  section::after {
    content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
    position: absolute; right: 64px; bottom: 25px;
    padding: 0; font-size: 17px; color: #66737f;
    background: none; text-shadow: none;
  }
  pre { font-size: 27px; line-height: 1.35; padding: 20px 24px; margin: 10px 0 22px; background: #edf1f4; border-radius: 0; box-shadow: none; text-align: left; }
  code { font-family: "DejaVu Sans Mono", monospace; letter-spacing: 0; }
  section.reveal table { font-size: 25px; }
  section.reveal th, section.reveal td { padding: 11px 12px; }
  section.reveal td:first-child { white-space: nowrap; }
  section footer { font-size: 16px; }
  section.expression tbody tr:nth-child(3) { background: #e0ebf2; }
  section.reveal table { font-size: 24px; }
  section.reveal th, section.reveal td { padding: 8px 10px; }

---

<!-- _class: title -->
## Függvények és hatókör

---

## Függvények a matematikában

A függvény az **értelmezési tartomány minden eleméhez pontosan egy értéket rendel**.

$$f(x) = 2x + 1$$

| Bemenet: $x$ | Hozzárendelt érték: $f(x)$ |
| --- | --- |
| $0$ | $1$ |
| $2$ | $5$ |
| $5$ | $11$ |

Ugyanahhoz a bemenethez mindig ugyanaz az érték tartozik.

---

## Függvények más területeken

- **Geometria:** a kör területe a sugár függvényében: $T(r)=\pi r^2$, ahol $r \geq 0$.
- **Fizika:** állandó sebességű mozgásnál a megtett út: $s(t)=v\cdot t$.
- **Vásárlás:** rögzített egységár mellett a fizetendő összeg: $F(n)=p\cdot n$.

A modellben rögzítjük a feltételeket és az állandó mennyiségeket.

A programozásban egy függvény ilyen összefüggést is kiszámíthat, de más feladatot, például kiírást is végezhet.

---

## Függvények a programozásban

A **függvény** meghívható, újrafelhasználható programegység egy részfeladat elvégzésére.

- Csökkenti a kód ismétlését.
- Nevet ad egy műveletnek, és részekre bontja a megoldást.
- Segíti az önálló ellenőrzést és újrafelhasználást.

---

## Definíció és hívás

```python
def koszont(nev):
    print(f"Szia, {nev}!")

koszont("Vin")
koszont("Kaladin")
```

A `def` létrehozza a függvényt. A függvénytörzs a **híváskor** hajtódik végre.

---

## Paraméter és argumentum

```python
def osszead(a, b):
    return a + b

eredmeny = osszead(3, 4)
```

- **Paraméter:** a definícióban szereplő név: `a`, `b`.
- **Argumentum:** a híváskor átadott érték: `3`, `4`.
- A paraméterek a hívás lokális nevei.

---

<!-- _class: compact -->
## Egy hívás lépései

```python
def osszead(a, b):
    return a + b

eredmeny = osszead(3, 4)
```

1. Az argumentumok értékei a paraméterekhez kerülnek.
2. Lefut a törzs: `a + b` értéke `7`.
3. A `return` visszaadja az eredményt a hívónak.
4. Az `eredmeny` névhez `7` kerül.

---

## Visszatérési érték

A függvényhívás **kifejezés**: az eredménye tovább használható.

```python
def feny_mennyiseg(gombok, egyseg):
    return gombok * egyseg

keszlet = feny_mennyiseg(5, 2.5)
print(keszlet)
print(feny_mennyiseg(2, 2.5) + 10)
```

A `return` önmagában nem ír ki semmit.

---

## Kiírás vagy visszatérés?

```python
def koszont(nev):
    print(f"Szia, {nev}!")

szoveg = koszont("Vin")
print(szoveg)
```

**Mit ír ki a program? Mi kerül a `szoveg` névhez?**

---

## Kiírás és visszatérés: megoldás

Az előző példa kiírja az üdvözlést, majd: `None`.

```python
def koszonto_szoveg(nev):
    return f"Szia, {nev}!"

szoveg = koszonto_szoveg("Vin")
print(szoveg)
```

**`print`:** megjelenítés. **`return`:** eredmény átadása.
Kifejezett visszatérés nélkül az eredmény `None`.

---

## A return befejezi a hívást

```python
def van_eleg_feny(keszlet, igeny):
    if keszlet >= igeny:
        return True
    return False
```

- A végrehajtott `return` lezárja az adott függvényhívást.
- A hívó program a hívás után folytatódik.
- A puszta `return` szintén `None`-t ad vissza.

---

## Ellenőrzés: minden esetet kezelünk?

```python
def van_eleg_feny(keszlet, igeny):
    if keszlet >= igeny:
        return True

print(van_eleg_feny(10, 3))
print(van_eleg_feny(2, 3))
```

**Mi lesz a két eredmény? Hol hiányzik egy eset?**

---

## Hiányzó visszatérés

Az eredmények: `True` és `None`.
Ha a feltétel hamis, elérjük a függvény végét.

```python
def van_eleg_feny(keszlet, igeny):
    return keszlet >= igeny
```

Ez a változat mindkét esetben logikai értéket ad vissza.

---

<!-- _class: compact -->
## Állapot, állapottér, hatókör

| Fogalom | Jelentés |
| --- | --- |
| **Állapot (state)** | Az aktuálisan tárolt és elérhető információ, valamint a végrehajtás helyzete. |
| **Állapottér (state space)** | A lehetséges állapotok halmaza. |
| **Hatókör (scope)** | Az a programrész, ahol egy név közvetlenül elérhető. |

---

## Lokális változók

```python
def maradek_feny(keszlet, felhasznalas):
    maradek = keszlet - felhasznalas
    return maradek

print(maradek_feny(10, 3))
# print(maradek)  # Itt nem érhető el.
```

A paraméterek és a `maradek` a hívás **lokális nevei**.
Két hívásnak külön lokális környezete van.

---

<!-- _class: compact -->
## Globális nevek olvasása

```python
MAX_KESZLET = 100

def szabad_hely(keszlet):
    return MAX_KESZLET - keszlet

print(szabad_hely(30))
```

A globális név itt a **modul szintjén** definiált név.
Olvasásához nem szükséges a `global` kulcsszó.

**Lehetőleg paraméterként adjuk át a szükséges adatokat.**
Kerüljük a változó globális állapottól való függést. A rögzített modulkonstansok használata bevett megoldás.

---

## Azonos név, eltérő hatókör

```python
keszlet = 10

def helyi_keszlet():
    keszlet = 5
    print(keszlet)

helyi_keszlet()
print(keszlet)
```

**Mi a két kiírt érték? Megváltozott a külső készlet?**

---

<!-- _class: compact -->
## Névelfedés

A kiírt értékek: **5**, majd **10**.

- A függvény lokális `keszlet` neve elfedi a globális nevet.
- A lokális értékadás nem módosítja a globális kötést.
- A lokális nevek kívülről nem érhetők el közvetlenül.

A lokális név és a hivatkozott objektum élettartama nem ugyanaz: egy visszaadott objektum tovább is használható.

---

<!-- _class: compact -->
## Globális értékadás: global

```python
keszlet = 10

def hasznal_fenyt():
    global keszlet
    keszlet = keszlet - 3

hasznal_fenyt()
print(keszlet)  # 7
```

A `global` jelzi: a függvény a globális névhez rendel új értéket.

**Lehetőleg kerüljük:** a hívás külső állapotot változtat.
Általában paramétert és visszatérési értéket használjunk helyette.

---

## Ugyanez paraméterrel és visszatéréssel

```python
def hasznal_fenyt(keszlet, mennyiseg):
    return keszlet - mennyiseg

keszlet = 10
keszlet = hasznal_fenyt(keszlet, 3)
```

- A bemenet és az eredmény látható a függvény felületén.
- A külső név értékadásáról a hívó dönt.
- A függvény különböző készletekkel is használható.

---

## Lokális és globális változók használata

- **Általában a lokális változókat részesítsük előnyben.** Így kisebb az adatok véletlen módosításának esélye, és könnyebb követni a működést.
- A paraméterek és a visszatérési értékek láthatóvá teszik az adatátadást.
- A változó globális állapotot több függvény is módosíthatja. Emiatt a működés a hívások sorrendjétől is függhet.
- Ez nagyobb programban nehezíti a hibakeresést és a karbantartást.

---

## Kapcsolat a specifikációval

```python
def hasznal_fenyt(keszlet, mennyiseg):
    return keszlet - mennyiseg
```

**Előfeltétel:** `0 <= mennyiseg <= keszlet`.

**Utófeltétel:** az eredmény `keszlet - mennyiseg`, ezért nemnegatív és legfeljebb `keszlet`.

A kikötést a függvény itt **nem ellenőrzi automatikusan**.

---

## Főhatás és mellékhatás

- **Főhatás:** a függvény eredményének előállítása és visszaadása a hívónak. A számító függvényeknél ezt a visszatérési érték képviseli.
- **Mellékhatás:** ezen túl megfigyelhető hatás, például kiírás, fájlírás vagy külső adat módosítása.

A lokális köztes számítás önmagában nem mellékhatás.

A kiírás ebben a szóhasználatban mellékhatás akkor is, ha éppen ez a függvény célja.

---

## Főhatás és mellékhatás: példa

```python
def hasznalat_jelentessel(keszlet, mennyiseg):
    maradek = keszlet - mennyiseg
    print(f"Megmaradt fény: {maradek}")
    return maradek

uj_keszlet = hasznalat_jelentessel(10, 3)
```

**Főhatás:** a maradék kiszámítása és visszaadása: `7`.
**Mellékhatás:** a szöveg megjelenik a kimeneten.

---

## Tiszta függvények

Egy tiszta függvény:

- azonos bemenetekre ugyanazt az eredményt adja;
- csak a főhatását fejti ki, nem okoz mellékhatást.

```python
def osszead(a, b):
    return a + b
```

A változó külső állapot olvasása is befolyásolhatja az eredményt — akkor is, ha a függvény nem módosít semmit.

---

## A mellékhatások tudatos kezelése

- A kiírás és a fájlmentés hasznos, gyakran szükséges.
- A számítást lehetőleg válasszuk külön a megjelenítéstől.
- Legyen világos, melyik függvény milyen adatot változtat.

```python
maradek = hasznal_fenyt(10, 3)
print(f"Megmaradt fény: {maradek}")
```

A tiszta számítás egyszerűbben ellenőrizhető önállóan.

---

## Pozicionális és kulcsszavas argumentumok

```python
def femkeszlet(nev, on, acel):
    return f"{nev}: ón={on}, acél={acel}"

print(femkeszlet("Vin", 3, 5))
print(femkeszlet(acel=5, nev="Vin", on=3))
```

- Pozicionálisan a **sorrend** számít.
- Kulcsszóval a **paraméter neve** azonosít.
- Vegyes hívásnál az itt használt pozicionális argumentumok kerülnek előre.

---

## Alapértelmezett paraméterérték

```python
def idez(nev="Syl"):
    return f"{nev} megidézve!"

print(idez())
print(idez("Pattern"))
```

Ha nem adjuk meg az argumentumot, az alapértéket használja.
A kötelező paraméterek az ilyen egyszerű definíciókban az alapértékesek előtt szerepelnek.

---

<!-- _class: compact -->
## Típusjelölések (type hints)

```python
def feny_mennyiseg(
    gombok: int, egyseg: float
) -> float:
    return gombok * egyseg
```

A jelölések a várt bemeneti és visszatérési típusokat írják le.

**A Python önmagában nem kényszeríti ki őket futásidőben.**
Dokumentációt és fejlesztői ellenőrző eszközöket segítenek.

---

<!-- _class: compact -->
## Több adat visszaadása: tuple

```python
def allomanta(nev, fem):
    return nev, fem

info = allomanta("Vin", "ón")
nev, fem = info
```

A függvény **egyetlen tuple-t** ad vissza: `("Vin", "ón")`.
A tuple több elemet összefogó, nem módosítható sorozat.
Az utolsó sor a két elemet **kicsomagolja**.

---

## Dokumentáció: docstring

```python
def maradek_feny(keszlet, mennyiseg):
    """Visszaadja a felhasználás utáni készletet.

    Előfeltétel: 0 <= mennyiseg <= keszlet.
    """
    return keszlet - mennyiseg

help(maradek_feny)
```

A docstring a függvény első utasításaként álló szöveg.
Írja le a célt, a bemeneteket és az eredményt.

---

<!-- _class: compact -->
## Programozási paradigmák

A paradigma a program felépítésének és leírásának szemlélete.

- **Imperatív:** utasításokkal alakítjuk az állapotot.
- **Strukturált:** szekvenciára, elágazásra és iterációra építünk.
- **Procedurális:** meghívható részprogramokba szervezünk.
- **Objektumorientált:** az adatokat és a hozzájuk kapcsolódó működést objektumok köré szervezzük.
- **Funkcionális:** függvényekre és azok összekapcsolására építünk; fontos szerepet kap a tisztaság.

---

<!-- _class: definition -->
## Ezek a szemléletek együtt is használhatók

Egy program lehet egyszerre **imperatív, strukturált, procedurális és objektumorientált**.

A Python több paradigmát támogat.

