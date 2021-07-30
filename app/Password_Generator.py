import random
import string
import secrets

print('Welcome to password generator application :)')

print('Dear User, \n you can select between 3 types of passwords: \n 1 - strong passwords, \n 2 - weak passwords, \n 3 - customizable passwords')
print('Below you can choose the option 1, 2 or 3')
print('For the first and second fucntion you will be asked to input only one value - length of your new password. \n In case of 3rd option you will need to provide number of letters, number of digits and number of punctuations respectively. \n In case of wrong input generated password will have 25 values (letters, digits and punctuations) ')
print('Drogi Uzytkowniku, \n mozesz wybrac pomiedzy 3 typami hasel: \n 1 - silne hasla, \n 2 - slabe hasla, \n 3 - konfigurowalne hasla')
print('Ponizej mozesz wybrac opcje 1, 2 lub 3')
print('W przypadku pierwszej i drugiej funkcji zostaniesz poproszony o wskazanie dlugosci hasla. \n Natomiast w przypadku trzeciej bedziesz musial wprowadzic kolejno liczbe liter, liczbe cyfr oraz liczbe znakow interpunkcyjnych. \n W przypadku blednie wybranej metody wygenerowanie zostanie 25-znakowe haslo. ')
method = input('Chosen option (wybrana opcja):')
print(method)




#Functions
possible_values = (string.ascii_letters + string.digits + string.punctuation)


def get_strong_password(length):
    result_password = ''.join(secrets.choice(possible_values) for i in range(length))
    print ('Random (strong) password of length:',length, 'is:', result_password)

def get_weak_password(length):
    letters = string.ascii_letters
    result_password = ''.join(random.choice(letters) for i in range(length))
    print ('Random (weak) password of length:',length, 'is:', result_password)

def get_password_constructed_of_defined_numbers_of_each_type_of_values(letters_count, digits_count, punctuation_count):
    letters = ''.join((secrets.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((secrets.choice(string.digits) for i in range(digits_count)))
    punctuation = ''.join((secrets.choice(string.punctuation) for i in range(punctuation_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits + punctuation)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    print('Random password with', letters_count, 'letters', 'and', digits_count, 'digits', punctuation_count, 'punctuations', 'is:', final_string)

if method == '1':
    get_strong_password(int(input('Length of your new password: ')))
elif method =='2':
    get_weak_password(int(input('Length of your new password: ')))
elif method =='3':
    get_password_constructed_of_defined_numbers_of_each_type_of_values(int(input('Number of letters in your password: ')), int(input('Number of digits in your password: ')), int(input('Number of punctuations in your password: ')))
else:
    get_strong_password(25)

input("Press enter to exit ;)")
