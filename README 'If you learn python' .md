# For Python Learners: Understanding Key Concepts in the Code

If you're learning Python, this file provides explanations for some concepts you might not fully understand from the code.

---

## 1. Working with Dates: `import datetime`

The `datetime` module is a library for handling dates and times. In our project, we use the `datetime` class within it.

### Key Features:
- **Get Today's Date**:
  ```python
  datetime.datetime.today()
  ```
- **Convert Strings to Dates**:
  You can take numbers in a specific format and convert them into a date using:
  ```python
  datetime.datetime.strptime(string, format)
  ```

#### Example:
You have a date in string format:
```python
my_birthday = '10-10-2006'
```
To convert it into a date:
```python
date = datetime.datetime.strptime(my_birthday, "%d-%m-%Y")
```
Here:
1. The first argument is the string to convert (`my_birthday`).
2. The second argument is the format (`"%d-%m-%Y"`).

Formats like `%d-%m-%Y` specify the order of day, month, and year. Check the "formats.png" file in the program for details on formatting options.

---

## 2. Exiting a Program: `from sys import exit`

The `exit()` function terminates the program immediately when called.
Example:
```python
from sys import exit
exit()
```
Use it to stop the program at any point.

---

## 3. File Management: `import os`

The `os` module allows you to interact with the file system. In this project, we use:
```python
current_directory = os.path.dirname(os.path.abspath(__file__))
```
This stores the directory where the program is running.

Why is this useful? The program relies on additional files (e.g., name files), so knowing the current directory helps access them:
```python
current_directory/name_file
```
Each file path is stored as a variable.

---

## 4. Error Handling: `try` and `except ValueError`

These keywords handle exceptions. Use them to test a block of code and manage specific errors.

### Example:
A program that adds two numbers:
```python
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
print(Num1 + Num2)
```
If a user enters a letter instead of a number, it causes a `ValueError`. To handle this:
```python
try:
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
    print(Num1 + Num2)
except ValueError:
    print("You must enter only integers.")
```
This ensures the program displays a friendly message instead of crashing.

### In Our Code:
We ensure that if the user enters a date in the wrong format, the program shows an error message and exits.
For instance, the accepted format is `%d-%m-%Y` (e.g., `13-10-2006`). If the user enters `13/10/2006`, the program:
1. Detects the error.
2. Displays a message to use the correct format.
3. Exits so the user can restart and enter valid information.

---

Every function in the program is documented with its purpose, making it easier to understand.

---

Note:
The word "cumone" means "province" in Italian, and its plural form is:
"cumoni"

---
## بالعربي

لو بتتعلم بايثون دى شوية معلومات عن بعض الاشياء اللى ممكن متكونش فاهمها 'من اللى موجود فى الكود':

---

### 1. التعامل مع التواريخ: `import datetime`

مكتبة `datetime` خاصة بالتعامل مع التواريخ والأوقات. استخدمنا منها الكلاس `datetime`.

#### المميزات:
- **عرض تاريخ اليوم**:
  ```python
  datetime.datetime.today()
  ```
- **تحويل النصوص إلى تواريخ**:
  يمكنك تحويل الأرقام المكتوبة بشكل معين إلى تاريخ باستخدام:
  ```python
  datetime.datetime.strptime(string, format)
  ```

#### مثال:
عندك تاريخ مكتوب كالتالي:
```python
my_birthday = '10-10-2006'
```
لتحويله إلى تاريخ:
```python
date = datetime.datetime.strptime(my_birthday, "%d-%m-%Y")
```
1. المدخل الأول هو النص (`my_birthday`).
2. المدخل الثاني هو الشكل (`"%d-%m-%Y"`).

الشكل مثل `%d-%m-%Y` يحدد ترتيب اليوم والشهر والسنة. راجع ملف "formats.png" للتفاصيل.

---

### 2. إغلاق البرنامج: `from sys import exit`

دالة `exit()` تقفل البرنامج فورًا.
مثال:
```python
from sys import exit
exit()
```
استخدمها لإيقاف البرنامج عند أي نقطة.

---

### 3. إدارة الملفات: `import os`

مكتبة `os` تتيح التحكم في الملفات. في المشروع:
```python
current_directory = os.path.dirname(os.path.abspath(__file__))
```
هذا السطر يخزن مكان تشغيل البرنامج.

فايدته؟ البرنامج يحتاج ملفات إضافية (مثل ملفات الأسماء)، فبالتالي معرفة المسار الحالي يساعد في الوصول إليها:
```python
current_directory/name_file
```
كل ملف تم حفظ مساره كمتغير.

---

### 4. معالجة الأخطاء: `try` و `except ValueError`

هذه الكلمات تعالج الأخطاء. الهدف: تجربة كود معين والتعامل مع أخطاء محددة.

#### مثال:
برنامج لجمع رقمين:
```python
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
print(Num1 + Num2)
```
لو أدخل المستخدم حرف بدل رقم، يحصل `ValueError`. للتعامل مع هذا الخطأ:
```python
try:
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
    print(Num1 + Num2)
except ValueError:
    print("You must enter only integers.")
```
هذا يضمن عرض رسالة ودية بدلاً من تعطل البرنامج.

#### في الكود:
لو المستخدم أدخل التاريخ بتنسيق خطأ، البرنامج:
1. يكتشف الخطأ.
2. يعرض رسالة تطلب التنسيق الصحيح.
3. يقفل البرنامج ليبدأ المستخدم من جديد.

---

كل دالة مكتوب جنبها وظيفتها، لتسهيل الفهم.

---

ملحوظة:
كلمة "cumone" تعني "محافظة" بالإيطالي، وجمعها هو:
"cumoni"
