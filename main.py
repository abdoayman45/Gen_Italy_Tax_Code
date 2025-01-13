import datetime
import random
import os
from sys import exit
from character_values import *
from comuni_codes import *
from countries_codes import *

def cls():
    """For clear the screen"""
    os.system('cls' if os.name=='nt' else 'clear')


is_random = True


is_random_input = input("Choose :\n1. Random Italian Tax Code.\n2. Check The Detils of one you have.\nEnter your choise (1/2) : ")
if is_random_input == "1":
    is_random = True
elif is_random_input == "2":
    cls()
    print("Enter Your detils :\n")
    is_random = False
else:
    print("Wrong Choice.Plz Try Again.")
    exit()



#The path of all files we will use in our project
current_directory = os.path.dirname(os.path.abspath(__file__))

men_file_path = os.path.join(current_directory, 'Men_Names.txt')
women_file_path = os.path.join(current_directory, 'Women_Names.txt')


def get_randm_name(file_path):
    """return random name"""
    with open(file_path, 'r', encoding='utf-8') as file:
        name = random.choice([line.strip() for line in file.readlines()])
        return name
    
def get_random_dob():
    """return random date of birth"""
    year_of_now = datetime.datetime.today().year
    random_year = random.choice((1900,year_of_now))

    random_month = random.randint(1,12)

    if random_month in (1, 3, 5, 7, 8, 10, 12):
        max_days =  31
    elif random_month in (4, 6, 9, 11):
        max_days =  30
    elif random_month == 2:
        max_days =  29 if (random_year % 4 == 0 and random_year % 100 != 0) or (random_year % 400 == 0) else 28

    random_day = random.randint(1,max_days)

    the_random_date = f"{random_day}-{random_month}-{random_year}"
    return the_random_date


def get_random_comune():
    """return random city of italy"""
    return random.choice([random['comune'] for random in comuni_codes])



def generate_codice_fiscale(l_name, f_name, UR_dob, UR_gener, country, is_italian):
    """This fun take all info
    and return the tax code"""

    def extract_consonants(s):
        """This fun take the name
        and return only consonant letters of the name"""
        return ''.join([n for n in s if n.isalpha() and n not in "AOUIE"])
        
    def extract_vowels(s):
        """This fun take the name
        and return only vowel letters of the name"""
        return ''.join([n for n in s if n.isalpha() and n in "AOUIE"])
    
    def process_name(s, is_surname=True):
        """This fun take name and make it a consonant and vowel letters
        and return the code of name of the tax code"""
        s = s.upper()
        consonants = extract_consonants(s)
        vowels = extract_vowels(s)
        combined = consonants + vowels
        if is_surname:
            result = (combined + "XXX")[:3]
        else:
            if len(consonants) >= 4:
                result = consonants[0] + consonants[2] + consonants[3]
            else:
                result = (combined + "XXX")[:3]
        return result
    
    def process_dob_gender(dob, gender):
        """This fun take the date of birth
        and return the code of date of the tax code"""
        try:
            birth_date = datetime.datetime.strptime(dob, '%d-%m-%Y')
            year = str(birth_date.year)[-2:]
            month_codes = "ABCDEHLMPRST"
            month = month_codes[birth_date.month -1]
            day = birth_date.day
            if gender == "F":
                day = day+40
            return f"{year}{month}{day:02d}"
        except ValueError:
            print("\nInvalid date format. The Next Time Use This Format : DD/MM/YYYY .\n")
            exit()

    def process_place_of_birth_code(the_country, italian=True):
        """This fun take the country or the city if the clint is italian or random clint
        and return the code of birth post of the tax code"""
        if italian:
            for i in comuni_codes:
                if i['comune'] == the_country:
                    return i['code']
            return False
                
        else:
            for i in countries_codes:
                if i['country'] == the_country:
                    return i['code']
            return False


    def compute_check_char(code):
        """This fun take the code of all of lastname and name and date and post of birth
        and return the last letter of the tax code"""
        def get_char(list_loop,char):
            for n in list_loop:
                if n['character'] == char :
                    return n['value']
            return 0
                    
        total_indiviual = 0
        total_even = 0
        
        for i,char in enumerate(code):
            if (i+1) % 2 == 0:
                total_even += get_char(even_position_values,char)
            if (i+1) % 2 != 0:
                total_indiviual += get_char(indiviual_position_values,char)

        total = (total_even + total_indiviual) % 26
        last_char = alpha_latin[total]
        return last_char
    
    # Generate each part of the tax code (codice fiscale)
    country_code = process_place_of_birth_code(country,True if is_italian=="y" else False)
    if not country_code:
        return "We Don't have your country. So we can't creat your tax code ."
    else:
        name_part = process_name(f_name, is_surname=False)
        surname_part = process_name(l_name)
        dob_gender_part = process_dob_gender(UR_dob,UR_gener)
        partial_code = surname_part+name_part+dob_gender_part+country_code
        check_char = compute_check_char(partial_code)
        return f"{partial_code}{check_char}"


def start():
    """This fun of start """
    if not is_random:
        is_italian = input("Are you Italian (Y/N) : ").strip().lower()
        while is_italian not in ("y","n"):
            print("You Must to write only (Y or N).")
            is_italian = input("Are you Italian (Y/N) : ").strip().lower()
        if is_italian == "y":
            country = input("Inserisci la Provincia in cui sei nato (in Italiano) : ").strip().upper()
        else:
            country = input("Enter your country (in English) : ").strip().capitalize()

        f_name = input("Enter your First Name : ").strip()
        while not f_name.isalpha():
            print("You Must write only alpha letters.")
            f_name = input("Enter your First Name : ").strip()

        l_name = input("Enter your Last Name : ").strip()
        while not l_name.isalpha():
            print("You Must write only alpha letters.")
            l_name = input("Enter your Last Name : ").strip()

        UR_gener = input("Enter your Gener (M/F) : ").upper().strip()
        while not UR_gener in ("M","F"):
            print("You Must write only (M or F). (M=Male),(F=Female) .")
            UR_gener = input("Enter your Gener (M/F) : ").upper().strip()

        UR_dob = input("Enter your Date of Birth (dd-mm-yyyy) : ").strip()
    
    else:
        UR_gener = random.choice(("M","f"))
        f_name = get_randm_name(men_file_path if UR_gener=="M" else women_file_path)
        l_name = get_randm_name(men_file_path)
        UR_dob = get_random_dob()
        is_italian = "y"
        country = get_random_comune()

    tax_code = generate_codice_fiscale(l_name, f_name, UR_dob, UR_gener, country, is_italian)

    cls()
    print("Your details :\n")
    print(f"First Name : {f_name.capitalize()}\n")
    print(f"Last Name : {l_name.capitalize()}\n")
    print(f"Gener : {UR_gener}\n")
    print(f"Date of Birthe : {UR_dob}\n")
    print(f"Was Born in : {country}\n")
    print("Your italian tax code is : ",tax_code)


start()