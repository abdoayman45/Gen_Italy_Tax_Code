# Rules for Italian Tax Code (Codice Fiscale)

The **Codice Fiscale** is a unique 16-character alphanumeric code used in Italy to identify individuals. Below are the rules that govern its structure and generation:

---

## 1. **Surname (3 letters):**
- The first three consonants of the surname are used.
- If there are fewer than three consonants, vowels are added to complete the three characters.
- If the surname has fewer than three letters, the code is completed with 'X'.
- For compound surnames, treat them as a single word.

---

## 2. **Name (3 letters):**
- The first, third, and fourth consonants of the name are used.
- If there are fewer than four consonants, the first three are taken.
- If there are fewer than three consonants, vowels are added to complete the three characters.
- If the name has fewer than three letters, 'X' is used to complete the three characters.

---

## 3. **Year of Birth (2 digits):**
- The last two digits of the birth year are used (e.g., 1985 becomes '85').

---

## 4. **Month of Birth (1 letter):**
- Each month is represented by a specific letter:

| Month     | Letter |
|-----------|--------|
| January   | A      |
| February  | B      |
| March     | C      |
| April     | D      |
| May       | E      |
| June      | H      |
| July      | L      |
| August    | M      |
| September | P      |
| October   | R      |
| November  | S      |
| December  | T      |

---

## 5. **Day of Birth and Gender (2 digits):**
- For males: the day of birth is used as is (e.g., 05 remains '05').
- For females: the day of birth is increased by 40 (e.g., 05 becomes '45').

---

## 6. **Place of Birth (4 characters):**
- A unique code representing the place of birth is used.
- Italian municipalities and foreign countries each have specific codes assigned by the Italian tax authorities.
- If the location is outside Italy, you will find the data for each country in a file named:
`countries_codes.py`
- If the location is inside Italy, you will find the data for each cumone in a file named:
`comuni_codes.py`


---

## 7. **Check Character (1 letter):**
- The final character is a control character calculated using an algorithm based on the previous 15 characters.
- This ensures the validity of the tax code.

---

### Reference
For more details, visit the original source: [Codice Fiscale Rules](https://www.alus.it/pubs/CodiceFiscale/index.php?lang=it).
