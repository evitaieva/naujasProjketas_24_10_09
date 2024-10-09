# if 7:
#     print('phyton thinks its a true')
# else:
#     print('phyton thinks i know nothing')
#
# print('pradedu rink zaliu staskiukus')
import pathlib
import random
import re

from itertools import count
from logging import disable
from traceback import print_list

# print('hello')
# print("hello 9/24")

#
# print('prasau parasykite savo varda')
# name = input()
# print('koks Jusu amzius')
# age = int(input())
# if age < 18:
#     print(name + ', jus per jaunas')
# if age >= 18:
#     print(name + ' Jus galite balsuoti')

# print('prasau parasykite 4 skaicius')
# skai1 = int(input())
# skai2 = int(input())
# skai3 = int(input())
# skai4 = int(input())
# vidurkis = (skai1 + skai2 + skai3 + skai4) / 4
# print(vidurkis)
# if vidurkis >=5:
#     print('vidurkis teigiamas')
# if vidurkis <5:
#     print('vidurkis neigiamas')

# print('prasau parasykite skaiciu')
# number = int(input())
# isItGood = False
# if number % 5 ==0:
#     print(number * 1, '\n', number * 2, '\n', number * 3, '\n', number * 4, '\n', number * 5 )
#     isItGood = True
# if number % 2 ==0:
#     print(number,'\n', number * number, '\n', number / 2)
#     isItGood = True
# if number % 7 != 0:
#     print('prasau parasykite kita skaiciu')
#     number2 = int(input())
#     print( number2 + number2, '\n', number2 - number2, '\n', number2 * number2, '\n', number2 / number2)
#     isItGood = True
# if not isItGood:
#     print("message of dissapointment")
#
#
# if number % 5 ==0:
#     print(number * 1, '\n', number * 2, '\n', number * 3, '\n', number * 4, '\n', number * 5 )
# elif number % 2 ==0:
#     print(number,'\n', number * number, '\n', number / 2)
# elif number % 7 != 0:
#     print('prasau parasykite kita skaiciu')
#     number2 = int(input())
#     print( number2 + number2, '\n', number2 - number2, '\n', number2 * number2, '\n', number2 / number2)
# else:
#     print("message of dissapointment")

# file_format = pathlib.Path('main.py').suffix
# if file_format == '.py':
#     print('failas . py')
# else:
#     print('failas ne .py')

# failo_kelias = str(input("Iveskite failo kelia: "))
# if failo_kelias.endswith(".py"):
#     print("Tai yra Python failas")
# else:
#     print("Tai nėra Python failas")

# print('prasau parasykite skaiciu')
# number = int(input())
# if number % 2 ==0:
#     print('kintamasis yra lyginis')
# elif number % 5 ==0:
#     print('kintamasis dalijasi is 5')
# elif number ==3:
#     print('kintamasis yra 3')
# else:
#     print("message of dissapointment")

# print('prasau parasykite 3 skaicius')
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# if number1 - number2  ==0:
#     print('pirmi 2 skaiciai yra lygus')
# elif number1 - number3  ==0:
#     print('pirmas ir trecias skaiciai lygus')
# elif number3 > number1:
#     print('trecias yra didesnis uz pirma')
# elif number3 < number1:
#     print('trecias yra mazesnis uz pirma')
# elif number3 * 2 == number2:
#     print('trecias yra didesnis uz pirma')
# else:
#     print("message of dissapointment")

# print('prasau parasykite 3 skaicius')
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# if (number1 > number2) and (number1 > number3):
#     print('number1 yra didziausias')
# elif (number2 > number1) and (number2 > number3):
#     print('number2 yra yra didziausias')
# elif (number3 > number1) and (number3 > number2):
#     print('number3 yra yra didziausias')

# print('prasau parasykite 3 skaicius')
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# if (number1 < number2) and (number1 < number3):
#     print('number1 yra maziausias')
# elif (number2 < number1) and (number2 < number3):
#     print('number2 yra yra maziausias')
# elif (number3 < number1) and (number3 < number2):
#     print('number3 yra yra maziausias')

# print('ispausdinkite egzaminu rezultatus')
# rez1 = int(input())
# rez2 = int(input())
# rez3 = int(input())
# vidurkis = (rez1 + rez2 + rez3) / 3
# print(vidurkis)
# if (vidurkis > 8) and (vidurkis < 10):
#     print('vidurkis 8-10')
# elif (vidurkis > 5) and (vidurkis < 8):
#     print('vidurkis 5-8')
# elif (vidurkis < 5):
#     print('vidurkis < 5')

# print('prasau parasykite 2 skaicius')
# number1 = int(input())
# number2 = int(input())
#
# if (number1 > number2) and (number1 == 0):
#     print('number1 yra didesnis uz number2 arba =0')
# if (number2 > number1) and (number2 == 5):
#     print('number2 yra ura didesnis uz number1 arba =5')
# if (number1 > number2) and (number1 == 20):
#     print('number1 yra =20')
# if (number2 > number1) and (number1 < 100):
#     print('number2 yra >100')
# else:
#     print("message of dissapointment")


# print('prasau parasykite savo varda')
# name = (input())
# print('prasau parasykite savo pavarde')
# surname = (input())
# print('prasau parasykite savo gimimo metus')
# birthYear = int(input())
# age = 2024 - birthYear
#
# print(f' "As esu {name} {surname}. Man yra {age} metai(u)." ')



# random_num1 = random.randint(0,4)
# random_num2 = random.randint(0,4)
# random_num1 = 3
# random_num2 = 3
# print(random_num1)
# print(random_num2)
# if random_num1 > 0  and random_num2 > 0 and random_num1 > random_num2 and random_num1 != random_num2:
#     print( round(random_num1 / random_num2, 2))
# elif random_num1 > 0 and random_num2 > 0  and random_num1 < random_num2 and random_num1 != random_num2:
#     print( round(random_num2 / random_num1, 2))
# else:
#     print ('dalyba negalima')





# num1 = random.randint(0, 4)
# num2 = random.randint(0, 4)
# num1 = 4
# num2 = 3
# print(num1)
# print(num2)
# if num1 > num2:
#     print(num1 / num2)
# if num2 > num1:
#     print(num2 / num1)
# if num1 > 0 and num2 > 0:
#     print(num2 / num1)
# if num1 == 0 or num2 == 0:
#     print('nulis')
# else:
#     print('nesamone')


# num1 = random.randint(0, 25)
# num2 = random.randint(0, 25)
# num3 = random.randint(0, 25)
# print(num1)
# print(num2)
# print(num3)
# if num1 != num2 and num1 != num3 and num2 != num3:
#     if num1 > num2 and num1 < num3:
#         print(num1)
#     elif num2 > num1 and num2 < num3:
#         print(num2)
#     elif num3 > num1 and num3 < num2:
#         print(num3)
# else:
#     print('lygus')


# num1a = random.randint(0, 10)
# num2b = random.randint(0, 10)
# num3c = random.randint(0, 10)
# print(num1a)
# print(num2b)
# print(num3c)
# if num1a > num3c and num2b > num3c:
#     print('trikampisC')
# elif num1a > num2b and num3c > num2b:
#     print('trikampisB')
# elif num2b > num1a and num3c > num1a:
#     print('trikampisA')
# if (num1a > num3c and num2b > num3c) or (num1a > num2b and num3c > num2b) or (num2b > num1a and num3c > num1a):
#     print('trikampis')
# else:
#     print('klaida')

#
# num1 = random.randint(0, 2)
# num2 = random.randint(0, 2)
# num3 = random.randint(0, 2)
# num4 = random.randint(0, 2)
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# countZeros = 0
# countOnes = 0
# countTwos = 0
#
# if num1 == 0:
#     print("as esu num1 ir esu lygus nuliui")
#     countZeros += 1
# if num2 == 0:
#     print("as esu num2 ir esu lygus nuliui")
#     countZeros += 1
# if num3 == 0:
#     print("as esu num3 ir esu lygus nuliui")
#     countZeros += 1
# if num3 == 0:
#     print("as esu num4 ir esu lygus nuliui")
#     countZeros += 1
#     print("nuliu radau " + str(countZeros))
#
# if num1 == 1:
#     print("as esu num1 ir esu lygus vienetui")
#     countOnes += 1
# if num2 == 1:
#     print("as esu num2 ir esu lygus vienetui")
#     countOnes += 1
# if num3 == 1:
#     print("as esu num3 ir esu lygus vienetui")
#     countOnes += 1
# if num3 == 1:
#     print("as esu num4 ir esu lygus vienetui")
#     countOnes += 1
#     print("vienetu radau " + str(countOnes))
#
# if num1 == 2:
#     print("as esu num1 ir esu lygus dvejetui")
#     countTwos += 1
# if num2 == 2:
#     print("as esu num2 ir esu lygus dvejetui")
#     countTwos += 1
# if num3 == 2:
#     print("as esu num3 ir esu lygus dvejetui")
#     countTwos += 1
# if num3 == 2:
#     print("as esu num4 ir esu lygus dvejetui")
#     countTwos += 1
# print("dvejetu radau " + str(countTwos))



#
# num1 = random.randint(-10, 10)
# num2 = random.randint(-10, 10)
# num3 = random.randint(-10, 10)
# print(num1)
# print(num2)
# print(num3)
#
#
# if num1 > 0:
#     print('[' + str(num1) + ']')
# if num1 == 0:
#     print('(' + str(num1) + ')')
# if num1 < 0:
#     print('{' + str(num1) + '}')
#
# if num2 > 0:
#     print('[' + str(num2) + ']')
# if num2 == 0:
#     print('(' + str(num2) + ')')
# if num2 < 0:
#     print('{' + str(num2) + '}')
#
# if num3 > 0:
#     print('[' + str(num3) + ']')
# if num3 == 0:
#     print('(' + str(num2) + ')')
# if num3 < 0:
#     print('{' + str(num3) + '}')


# print("parafino namai")
# ZvakiuSkaicius = random.randint(5, 3000)
# ZvakiuSkaicius = 2114
# print(ZvakiuSkaicius)
# kaina = 1
# if ZvakiuSkaicius < 1000:
#     print(ZvakiuSkaicius  * kaina)
# # if ZvakiuSkaicius >= 1000 and ZvakiuSkaicius < 2000:
# if 1000 < ZvakiuSkaicius < 2000:
#     print(ZvakiuSkaicius * kaina * 0.97)
# if ZvakiuSkaicius > 2000:
#     print(ZvakiuSkaicius * kaina * 0.96)

# num1 = random.randint(0, 100)
# num2 = random.randint(0, 100)
# num3 = random.randint(0, 100)
# print(num1)
# print(num2)
# print(num3)
#
# print(round((num1 + num2 + num3)/3))
#
# if num1 < 10:
#     print((num2 + num3) / 2)
# if num1 > 90:
#     print((num2 + num3)/2)
# if num2 < 10:
#     print((num1 + num3) / 2)
# if num2 > 90:
#     print((num1 + num3)/2)
# if num3 < 10:
#     print((num1 + num2) / 2)
# if num3 > 90:
#     print((num1 + num2)/2)


# name = 'Kevin'
# surname = 'Costner'
# if len(name) > len(surname):
#     print(surname)
# else:
#     print(name)

# print(str.upper(name), str.lower(surname))

# print(str.upper(name[0]) + str.upper(surname[0]))
# print(str.upper(name[2]) + str.upper(surname[2]))
# print(str.upper(name[3]) + str.upper(surname[3]))


# fraze ='An American in Paris'
# # updateFraze = fraze.replace('a' or 'A', '*') #lawer pasikeicia#
# updateFraze = fraze.replace('a' and 'A', '*') #upper pasikeicia#
# print(updateFraze)
#
# updateFraze = {"a": "*", "A": "*"}
# print(updateFraze)

# fraze = 'An American in Paris'
# updateFraze = fraze.replace("a", "").replace("A", "")
# print(updateFraze)

# fraze = 'An American in Paris'
# replaced = re.sub('[aA]', '*', fraze)
# print(replaced)


# fraze ='An American in Paris'
# vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
# result  = ''
#
# print("\n After removing Vowels:", result)

# phrase = 'An American in Paris'
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)

# phrase = "Breakfast at Tiffany's"
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)


# phrase = "2001: A Space Odyssey"
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)

# phrase = "It's a Wonderful Life"
# vowel_free_phrase = ''
# for char in phrase:
#     if char not in 'aeiouAEIOU':
#         vowel_free_phrase += char
#
# print(vowel_free_phrase)

# print('labas rytas')
# labas= input()
# print('kuri siandien diena?')
# diena= input()
# print('ar isgerei vitaminus?')
# vitaminai= input()
# if vitaminai == 'taip':
#     print('grazios dienos Princess')
# if vitaminai == 'ne':
#     print('mars isgerti vitaminu')


# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# regex2 = re.findall("Star Wars: Episode", starWars)
# print(regex2)
#
# epizodas = re.sub("Star Wars: Episode", "",  starWars)
# print(epizodas)
# epizodo_nr  = re.sub("- A New Hope", "", epizodas)
# print(epizodo_nr)
# epizodo_numeris = re.sub("Star Wars: Episode  | - A New Hope", "", starWars)
# print(epizodo_nr)

# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# print(starWars[-14:-13])
# print(re.sub(r'\D+', '', starWars ))

# Susikurkite list vardams saugoti ir užpildykite jį informacija. Išveskite visą
# šį list, tuomet pirmą narį iš jo, paskutinį narį, bei kiek narių jame yra.

# vardai = ['Asta', 'Naglis', 'Regimantas', 'Augustinas', 'Teresa', 'Darius', 'Arina', 'Gintaras', 'Monika', 'Alina',]
# # print(vardai [0])
# # print(vardai [5])
# print('pirmas vardas sarase:', vardai [0])
# print('nariu skaicius:', len(vardai))
# print('paskutinis vardas sarase:',  vardai[len(vardai)-1])

# Susikurkite list žmonių ūgiams saugoti ir užpildykite jį informacija.
# Išveskite viso šio list duomenis bei kiek ūgių turite.

# ugis = [169, 170, 215, 198, 154, 210, 214]
#
# print('ugiu sarasas:', ugis)
# print('ugis:', len(ugis))
# print('ugiu skaicius:',  len(ugis))

# Susikurkite list pažymiams saugoti. Pamėginkite sukurti programą, kur
# vartotojas galėtų suvesti norimą kiekį naujų duomenų. Galiausiai išveskite
# visus pažymius ir jų kiekį.

# pazimys = [10,7,9,8,9,8,8]
# print(pazimys)
# print('pazymiu skaicius:',  len(pazimys))
# suma = pazimys[0] + pazimys[1] +pazimys[2] +pazimys[3] +pazimys[4] +pazimys[5] +pazimys[6]
# print (suma)
# vidurkis = suma / len(pazimys)
# print('pazymiu vidurkis:', vidurkis)
# print('pazimiu vidurkis:', round(vidurkis, 2))

# Susikurkite miestų sąrašą. Į šį list pridėkite duomenų kurdami patį list.
# Toliau sukurkite galimybę vartotojui papildyti list. Išveskite tiek pradinį list,
# tiek papildytą duomenimis. Pamėginkite papildyti programą, kad
# vartotojas galėtų pasirinkti į kurią list vietą būtų įrašytas naujas miestas.

# city = ['Alytus', 'Klaipeda','Vilnius','Telsiai','Raseiniai','Kaunas']
# print(city)
# city.append('Marijampole')
# city.append('Zarasai')
# print(city)
# city.insert(1, 'Marijampole')
# print(city)

# Sukurkite pasirinktą list ir užpildykite jį duomenimis. Iš jo pašalinkite
# keletą įrašų, tiesiog parašant pop() funkciją. Taip pat, sukurkite, kad
# vartotojas galėtų pasirinkti kiek dar duomenų pašalinti ir pašalinkite iš list
# pasirinktą kiekį įrašų.

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# apygarda.pop()
# print(apygarda)
# apygarda.pop(0)
# apygarda.pop(5)
# print(apygarda)

# Sukurkite list su pasirinktais duomenimis. Patikrinkite ar sąraše yra
# daugiau nei 5 įrašai ir jeigu taip - jį išvalykite (clear funkcija).

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# apygarda.pop(5)
# print(apygarda)
# apygarda.clear()
# print(apygarda)

# Sukurkite list, kuriame būtų surašyti bet kokie žodžiai. Leiskite vartotojui
# atlikti paiešką tame sąraše - vartotojas įvestų norimą žodį ir programa
# pasakytų ar tame sąraše tas žodis yra ir jeigu yra, tai kurioje vietoje.

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# print('Alytus' in apygarda)
# print(apygarda.index('Dubiciu'))

# Sukurkite sąrašą, kuriame būtų surašyti studentų pažymiai. Galite
# padaryti taip, kad pasirinktą kiekį pažymių galėtų suvesti pats vartotojas.
# Programa turi pasakyti kiek dešimtukų studentas turi.
# studentuPazymiai = [10,6,7,8,4,8,3,10,10,4]
# print(studentuPazymiai)
# # print(studentuPazymiai.index(10))
# print(studentuPazymiai.index(10,0,10))
# print(studentuPazymiai.count(10))

# Susikurkite automobilių markių sąrašą ir užpildykite jį duomenimis
# (kuriantis sąrašą arba su vartotojo įvestimi). Išveskite turimus duomenis
# ekrane.
# Tuomet surikiuokite automobilių markes didėjimo tvarka ir
# išveskite.
# Taip pat, surikiuokite mažėjimo tvarka ir išveskite.

# marke = ['BMW', 'Opel', 'Volo','Audi', 'Porshe', 'Mercedes', 'Volswagen']
# # print(marke)
# # print(len(marke))
# # marke.sort()
# # print(marke)
# # marke.reverse()
# # print(marke)

# Susikurkite studento pažymių sąrašą ir užpildykite duomenimis. Išveskite
# tris didžiausius turimus pažymius.


# studentuPazymiai = [10,6,7,8,4,8,3,10,10,4]
# print(studentuPazymiai)
# studentuPazymiai.sort()
# print(studentuPazymiai)
# studentuPazymiai.reverse()
# print(studentuPazymiai)
# print(studentuPazymiai [:3])

# Susikurkite studentų pažymių sąrašą ir užpildykite duomenimis. Jeigu
# studentas turi neigiamų pažymių (1, 2, 3, arba 4), išveskite kiek tokių
# pažymių jis turi.

# studentuPazymiai = [10,6,7,8,4,8,3,10,10,4]
#
# print(studentuPazymiai.count(1) + studentuPazymiai.count(2) + studentuPazymiai.count(3) + studentuPazymiai.count(4))

# Susikurkite pasirinktą sąrašą su duomenimis. Pritaikykite list slicing tokiais
# būdais ir gautus atsakymus išveskite:
# 1. Paimkite pirmus tris narius.
# 2. Paimkite du narius, pradedant trečiu.
# 3. Paimkite paskutinius keturis narius.
# 4. Paimkite kas antrą narį, pradedant trečiu nariu.
# 5. Paimkite visus atbuline tvarka.

# apygarda = ['Puodziu', 'Zilinu', 'Dubiciu', 'Panociu', 'Kabeliu', 'Marcinkoniu','Kruminiu','Matuizu']
# print(apygarda)
# print(apygarda [:3])
# print(apygarda [3:5])
# print(apygarda [4:])
# print(apygarda [3::2])
# apygarda.reverse()
# print(apygarda)

# Susikurkite list studentų vidurkiams saugoti. Išsitraukite ir pasidėkite į
# atskirą list tris didžiausius pažymius (galite surikiuoti ir išsikirpti ką reikia).

# vidurkis = [4.5, 6.7, 8, 10, 6.9, 8.9]
# print(vidurkis)
# vidurkis.sort()
# print(vidurkis)
# vidurkis.reverse()
# print(vidurkis)
# print(vidurkis [:3])

# Pamėginkite sukurti žodžių žodyną. Šį žodyną turėtų užpildyti vartotojas,
# įvesdamas visus norimus žodžius. Po kiekvieno įvedimo jam turėtų būti
# parodomi visi žodžiai, tačiau surikiuoti, t.y. įdėjus žodį į sąrašą, jį
# surikiuokite iš naujo.
# auksoZodziai = ['Alaninas', 'Kabala','Piala', 'Marsala', 'Kupala']
# print(auksoZodziai)
#
#
# kopija = auksoZodziai[:]
# print(kopija)
# auksoZodziai[0] = 'naujas'
# print(auksoZodziai)
# print(kopija)

# Sukurkite sąrašą, kuriame saugotumėte sandėlio likučius. Į atskirą sąrašą
# persikelkite visus likučius kurių lieka mažai (mažiau nei 5 vnt. arba trijų
# prekių likučius, kurių likę mažiausiai). -

# Su for pagalba penkis kartus išveskite savo vardą.
# for sk in range(5):
#     print('Evita')

# Parašyti for, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10.
# for sk in range(11):
#     print('Evita' + str(sk))

# Parašyti for, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15.

# for sk in range(0, 16,2):
#     print('Evita' + str(sk))

# Parašyti for, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20.
# Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7]...

# for sk in range(1, 20,3):
#     print('Evita' + str([sk]))

# Parašyti for, kuris eitų pro kiekvieną skaičių nuo 1 iki 20. Jame apsirašyti if
# sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4, jei taip tai šį
# skaičių išvesti.

# for sk in range(1, 20):
#     if sk % 4 ==0:
#         print('dalinasi is 4' + '-' + str(sk))
#     else:
#         print('nesidalinas')

# Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis
# ar nelyginis skaičius. Pvz:
# 1 - nelyginis
# 2 - lyginis
# 3 - nelyginis

# for skaicius in range(1, 16):
#     if skaicius % 2==0:
#         print(f'skaicius {skaicius} yra lyginis')
#     else:
#         print(f'skaicius {skaicius} yra nelyginis')

# Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti.
# Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).
# Jei rėžiai tinkami, tuomet vykdyti for,
# --kuris atskirose eilutėse išvestų kiekvieną skaičių iš tų rėžių,
# --bei atskiriant tarpu - tų skaičių kvadratus.
# start = 1
# end = 9
# if start < end:
#    for skaicius in range(start, end):
#       print(str(skaicius) + " " + str(skaicius * skaicius))
# else:
#    print("lempiniai reziai")

# Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti.               V
# Patikrinkite kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).   V
# Jei rėžiai tinkami, tuomet vykdyti for,                                     V
# --kuris iš duotų skaičių išvestų visus nelyginius skaičius                  V
# --arba tuos, kurie dalinasi iš 8.                              V

# start = 1
# end = 9
# if start < end:
#    for skaicius in range(start, end):
#       if skaicius % 2 != 0 or skaicius %8 == 0:
#          print(skaicius)

# Leiskite vartotojui įvesti savo vardą.
# Ciklą for vykdykite tiek kartų kiek tame varde yra raidžių.
# Visais atvejais išveskite tą patį pasisveikinimą,
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus).

# vardas = 'Evita' #vietoj inputo
# for letter in vardas:
#    print('labas, ' + vardas)
# print("------------------------")
# for i in range(0,len(vardas)):
#    print(vardas)

# Susikurkite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai.


# for skaiciai in [88, 65, 21, 26, 47]:
#    if skaiciai  %2 ==0:
#       print(skaiciai)

# Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį.
# Taip pat, kokius skaičius jis nori matyti (lyginius ar nelyginius). Patikrinkite ar rėžiai tinkami,
# jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą
# žingsnį. Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius
# arba nelyginius).

# start = int(input('prasau iveskite pradzios skaiciu: '))
# end = int(input('prasau iveskite pabaigos skaiciu: '))
# step = int(input('prasau iveskite bet koki skaiciu: '))
# number = str(input('norite matyti lyginius ar nelyginius skaicius? '))
# isEven = number =="lyginius"
# if start < end:
#    for i in range(start, end + 1, step):
#       if isEven and i % 2 ==0:
#          print(i)
#       elif number == 'nelyginius' and i % 2 !=0:
#          print(i)
# else:
#    print('start is less then end')


# Su for pagalba, pamėginkite išvesti tokią eglutę:
# *
# **
# ***
# ****
# *****
# (papildomai) leiskite vartotojui pasirinkti kokio dydžio eglutė turėtų būti
# išvesta.

# s = '*'
# howHigh = 25
# for i in range(0,howHigh + 1):
#    print(s * i)

# Leiskite vartotojui įvesti bet kokį žodį, bei pasirinkti po kiek kartų turėtų
# būti pakartojama kiekviena raidė. Su ciklo pagalba išveskite kiekvieną
# raidę iš žodžio atskiroje eilutėje, taip pat, tą raidę eilutėje kartokite tiek
# kartų kiek pasirinko vartotojas (16 pvz).

# word = input('prasau iveskite zodi: ')
# number = int(input('prasau iveskite skaiciu: '))
# for t in word:
#    print(t * number)

# Raskite visų skaičių nuo 1 iki 100 sumą.
# suma = 0
# for i in range(100):
#    suma += i
#    print(f'sum: {suma}')

# Raskite visų lyginių skaičių nuo 20 iki 50 sumą.
# suma = 0
# for i in range(20, 50):
#    if i % 2 == 0:
#       suma += i
#    print(f'lyginiu sum: {suma}')

# Raskite visų nelyginių skaičių nuo 30 iki 60 sumą.
# suma = 0
# for i in range(30, 60):
#    if i % 2 != 0:
#       suma += i
#    print(f'nelyginiu sum: {suma}')

# Rasti visų skaičių, žemesnių už 1000 ir kurie dalinasi iš 3 arba 5, sumą.
# Pavyzdys: Visi skaičiai mažesni už 10 ir kurie dalinasi iš 3 arba 5 yra: 3, 5, 6, 9.
# Šių skaičių suma yra 23. Turite gauti 233168 atsakymą.

# suma = 0
# for i in range(0, 1000):
#     if i % 3 == 0 or i % 5 == 0:
#         suma += i
# print(f'233168: {suma}')

# "Write a program that prints the numbers from 1 to 100.
# “Fizz” instead of the number and for the multiples of five
# print “Buzz”. For numbers which are multiples of both three and five print
# “FizzBuzz”."

# FizzBuzz = 0
# for i in range(1, 100):
#    if i % 3 ==0:
#       print('Fizz')
#       if i % 5 ==0:
#          print('Buzz')
#             if i % 3 ==0 and 5 ==0:
#                print('FizzBuzz')


# FizzBuzz = 0
# for i in range(1, 100):
#    if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#    elif i % 3 == 0:
#         print('Fizz')
#    elif i % 5 == 0:
#         print('Buzz')
#    else:
#        print(i)

# Išveskite visus skaičius nuo 1 iki 20.
#
# number = 0
# while number < 20:
#    number += 1
#    print(number)

# Išveskite visus skaičius nuo 1 iki 50. Prie kiekvieno lyginio skaičiaus
# parašykite žodį "lyginis", o prie kiekvieno nelyginio – "nelyginis".

# number = 0
# # while number <=50:
# #     if number %2 == 0:
# #       print(f'lyginis: {number}')
# #       number += 1
# #       if number %2 != 0:
# #          print(f'nelyginis: {number}')
# #          number += 1

# Išveskite visus skaičius nuo 25 iki 50. Vietoj skaičių, kurie dalinasi iš 3
# išveskite tekstą "dalinasi iš 3".
# pabaiga = 50
# number = 25
# while number < pabaiga:
#     if number % 3 == 0:
#         print('dalinasi iš 3')
#     else:
#         print(number)
#     number += 1
#
# pradzia, pabaiga = 25, 50
# number = 0
# while number < pradzia or number < pabaiga:
#     if number %3 == 0:
#       print(f'dalinasi iš 3 {number}')
#       number += 1

# Išveskite visus skaičius nuo 1 iki 100
# arba iki tol kol pasitaikys toks, kuris dalinasi iš 7.

# number = 0
# while number <= 100:
#     number += 1
#     print(number)
#     if number % 7 == 0:
#        break


# Išvedinėkite visus skaičius nuo 1 iki tol kol pasitaikys skaičius, kuris
# dalinasi iš 3 ir iš 5.

# number = 1
# while number > 0:
#     print(number)
#     if number % 3 == 0 and number % 5 == 0:
#         break
#     number += 1

# Vartotojas turi suvesti rėžių pradžią ir pabaigą. Tačiau jūs turite patikrinti
# ar nurodyti rėžiai yra geri (pradžia mažesnė už pabaigą). Liepkite
# vartotojui kartoti įvedimą tol, kol rėžiai jau bus įvesti tinkamai. Turint
# tinkamus rėžius, išveskite visus skaičius nuo rėžių pradžios iki pabaigos
# (šitam jau vietoj while galite naudoti for ciklą), šalia kiekvieno skaičiaus
# išvedant jo kvadratą, bei ar jis lyginis/nelyginis.

# while True:
#         print('prasau iveskite skaiciu')
#         number1 = int(input())
#         print('prasau iveskite skaiciu didesni uz pirmaji')
#         number2 = int(input())
#         if number1 < number2:
#             for number in range(number1, number2):
#                 if (number1 * number2) % 2 == 0:
#                     print(f'{number}, {(number1 * number2)} lyginis')
#                 else:
#                     print(f'{number} {(number1 * number2)} nelyginis')
#             break
#         else:
#             print('incorect numbers')


# Išveskite visus skaičius nuo 1 iki kol pasitaikys toks, kuris yra pirminis ir
# yra didesnis nei 20.


# number = 20
# while True:
#     number += 0
#     print(number)
#     if number / number == 20:
#        break



# 1. Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

# labas = 'labas'
# kiekKartu = 10
# while kiekKartu > 0:
#     print(labas)
#     kiekKartu -= 1

# 2. Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

# number = 0
# while number < 9:
#    number += 1
#    print(number)

# 3.Sukurkite masyvą iš dešimties augalų pavadinimų.
# augaluPavdinimai = 'Abrikosas', 'Agukas','Akišveitė', 'Aklė','Akmengrūdis', 'Aktinidija', 'Alangis', 'Alavijas', 'Alyvmediniai', 'Alyva'
#
# print(augaluPavdinimai)

# 4. Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
# print('Abrikosas \nAgukas \nAkišveitė \nAklė \nAkmengrūdis \nAktinidija \nAlangis \nAlavijas \nAlyvmediniai \nAlyva')

# 5.Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).

# augaluPavdinimai = ['Abrikosas', 'Agukas','Akišveitė', 'Aklė','Akmengrūdis', 'Aktinidija',
# 'Alangis', 'Alavijas', 'Alyvmediniai', 'Alyva']
# augaluPavdinimai.reverse()
# print(augaluPavdinimai)

# 6.Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

# number = 10
# while number < 50:
#     if number % 2 == 0:
#         print(number)
#     number += 1

# 7.Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkit
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

# number = 10
# while number < 50:
#     number += 1
#     if number % 10 ==0:
#         continue
#     if number % 2 == 0:
#         print(number)


# 8. Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
# number = 0
# while number < 20:
#     number +=1
#     if number % 2==0:
#         print(number)
# counter = 20
# for i in range(0,20):
#     if i % 2 == 0:
#         print(i)
#         counter = count(int(i))
#         print(counter)

# 9. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai,
# ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai) - NEISPRESTAS

# 10. Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais
# ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi
# būti atspausdinti skliausteliuose” [ ] “.

# numbers = [random.randint(0, 300)  for number in range(300)]
# countAbove_150 = len([number for number in numbers if number > 150])
# numbersAbove_275 =[number for number in numbers if number > 275]
#
# nums = [number if number not in numbersAbove_275 else f'[{number}]' for number in numbers]
#
# strNums = str(nums)
# spacedNums = strNums.replace(',', ' ').replace("'", '')
#
# print(f'numbers: {spacedNums[1:-1]}')

# 11.Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77
# be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

# numbers = [number for number in range(1, 3001) if number % 77 ==0]
# print(str(numbers)[1:-1])

# 13. Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# row = ['*' for element in range(25)]
#
# for column in range(25):
#     print(row)

# 14.Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu. -NEPADARYTA

# 15. Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas,
# o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir
# “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;

# h = 0
# S = 1
# metimai = []
# while True:
#     metimas = random.randint(0, 1)
#     metimai.append(metimas)
#     if metimas == h:
#         break

# h = 0
# s = 1
# metimai = []
# while True:
#     metimas = random.randint(0, 1)
#     metimai.append(metimas)
#     if metimai.count(0) == 3:
#         break
# print((str(metimai).replace(str(h), 'h').replace(str(s), 's')))
#
# print((str(metimai).replace(str(h), 'h').replace(str(s), 's')))


# h = 0
# s = 1
# metimai = []
# while True:
#     metimas = random.randint(0, 1)
#     metimai.append(metimas)
#     if metimai[-3:] == [0, 0, 0]:
#         break
# print((str(metimai).replace(str(h), 'h').replace(str(s), 's')))

# 16. Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20,
# Kazys surenka taškų kiekį nuo 5 iki 25. Vienoje eilutėje išvesti žaidėjų
# vardus su taškų kiekiu ir “Partiją laimėjo: ​laimėtojo vardas​”.
# Taškų kiekį generuokite funkcija ​random.randint(x,x)​. Žaidimą laimi tas,
# kas greičiau surenka 222 taškus. Partijas kartoti tol, kol kažkuris žaidėjas pirmas
# surenka 222 arba daugiau taškų.

# Petro = []
# Jono = []
# PTurn = 0
# JTurn = 0
#
# while True:
#
#     while PTurn == JTurn:
#         Petro.append(random.randint(10, 20))
#         PTurn += 1
#     while JTurn < PTurn:
#         Jono.append(random.randint(5, 25))
#         JTurn += 1
#
#     if sum(Petro) >=222:
#         Petras = True
#         break
#     elif sum(Jono) >= 222:
#         Petras = False
#         break
#
# if Petras == True:
#     print('Laimėjo Petras')
# else:
#     print('Laimėjo Jonas')
#
# print(f'Petro taškai: {sum(Petro)}. Jono taškai: {sum(Jono)}')

# 18.Susikurkite sąrašą projekto komandos narių vardams ir pavardėms
# saugoti. Išveskite tekstą "prie projekto dirba šie komandos nariai:" ir iškart
# po to kiekvieną komandos narį atskiroje eilutėje.

# team = ['Saulius', 'Vytautas', 'Edvinas']
# print('Prie projekto dirba: ')
# for member in team:
#     print(member)

# 19.Susikurkite sąrašą, kuriame būtų saugomos jau praeitos Python temos.
# Išveskite tekstą "mes jau mokėmės:". Ir iškart po to atskirose eilutėse
# visas temas, tačiau jas sunumeruokite "1-a tema:", "2-a tema:" ir t.t. Tai
# pamėginkite atlikti tiek su for ciklu, tiek su while ciklu.

# topic = ['ciklai', 'listai', 'stringai']
# print('Jau mokėmės: ')
# for top in topic:
#     print(top)

# 20.Susikurkite masyvą studijų programų pavadinimams saugoti. Užpildykite
# šį masyvą duomenimis. Išveskite kiekvieną studijų programą atskiroje
# eilutėje.

# studijos = ['charakternas', 'baletas', 'tautiniai', 'istoriniai']
# for pas in studijos:
#     print(pas)

# 21.Susikurkite masyvą šalių pavadinimams saugoti ir jį užpildykite
# duomenimis. Išveskite šalių pavadinimus atskirose eilutėse, su prierašu
# "šalis" ir tada nurodant šalį iš masyvo.
# country = ['France', 'Spain', 'Lithuania', 'Portugal', 'USA']
# for CName in country:
#     print(CName)
#     print(f'Šalis: {CName}')

# 22.Susikurkite sąrašą prekių krepšeliui saugoti. Išveskite kiek prekių
# krepšelyje yra narių. Tuomet išveskite visą prekių krepšelio informaciją,
# nurodant kelinta prekė, pvz "nr 1 pirkinys:", "nr 2 pirkinys:" ir t.t.

# prekes = ['pienas', 'obuoliai', 'miltai', 'arbuzas']
# print(f'Sąrašo ilgis: {len(prekes)}')
# for number, preke in enumerate(prekes):
#     print(f'Nr. {number + 1}: {prekes}')
#
# prekes = ['pienas', 'obuoliai', 'miltai', 'arbuzas']
# print(f'Sąrašo ilgis: {len(prekes)}')
# for number, preke in enumerate(prekes):
#     print(f'Nr. {number + 1}: {preke}')

# 23.Susikurkite pažymių sąrašą ir užpildykite jį informacija. Surikiuokite
# pažymius nuo didžiausio iki mažiausio. Išveskite visus turimus pažymius
# atskirose eilutėse. Prie kiekvieno pažymio taip pat prirašykite "puikiai",
# jeigu jis yra 10, "labai gerai", jeigu jis yra 9 ir t.t.

# pazymiai = [10, 9, 8, 5, 10, 5, 6]
# pazymiai.sort()
# pazymiai.reverse()
# for pazimys in pazymiai:
#     if pazimys == 10:
#         print(f'{pazimys}: puikiai')
#     elif pazimys == 9:
#         print(f'{pazimys}: labai gerai')
#     elif 7 <= pazimys <= 8:
#         print(f'{pazimys}: gerai')
#     elif 5 <= pazimys <= 6:
#         print(f'{pazimys}: vidutiniškai')
#     elif pazimys == 4:
#         print(f'{pazimys}: patenkinamai')
#     else:
#         print(f'{pazimys}: nepatenkinamai')
# 24.Susikurkite programą, kurioje vartotojas galėtų nusakyti kiek atsitiktinių
# skaičių turėtų būti sugeneruota. Tuomet programa turėtų būtent tokį kiekį
# atsitiktinių skaičių sugeneruoti ir sudėti į sąrašą. Išveskite visus šiuos
# skaičius ekrane. Tuomet tuos pačius skaičius išveskite ekrane dar kartą,
# tačiau viską spausdinkite atskirose eilutėse, eilutėje nurodant patį skaičių
# ir jo kvadratą.

# suvesti = int(input('Kiek skaičių suvesti: '))
# nums = []
#
# for num in range(suvesti):
#     nums.append(random.randint(0, 100))
# print(f'Skaičiai: {nums}')
#
# for num in nums:
#     print(f'{num}: {num**2}')

# 25.Susikurkite norimą sąrašą su duomenimis. Išsiveskite viso šio sąrašo
# informaciją. Pakeiskite trijų pasirinktų narių reikšmes į kitas. Išsiveskite
# pakeisto sąrašo informaciją.

# duomenys = list('statistika')
# print(duomenys)
#
# new = [1, 2, 3]
#
# for i in range(3):
#     duomenys[random.randint(0, len(duomenys) + 1)] = new[i]
#
# print(duomenys)

# 26.Susikurkite sąrašą ir jį užpildykite skaičiais (savarankiškai arba
# atsitiktiniais). Iš pradžių išveskite tekstą "lyginiai skaičiai" ir visus lyginius
# skaičius. Tuomet išveskite tekstą "visi nelyginiai skaičiai" ir visus nelyginius
# skaičius. Bei ant galo tekstą "visi skaičiai, kurie dalinasi iš 3" ir visus
# skaičius, kurie atitinka tokią sąlygą.

# numbers = []
# for i in range(random.randint(3, 10)):
#     numbers.append(random.randint(0, 20))
#
# print(numbers)
#
# even = [number for number in numbers if number % 2 == 0]
# odd = [number for number in numbers if number % 2 != 0]
# three = [number for number in numbers if number % 3 == 0]
#
# print(f'Lyginiai: {even}')
# print(f'Nelyginiai: {odd}')
# print(f'Dalinasi iš trijų: {three}')

# 27.Susikurkite sąrašą ir jį užpildykite atsitiktiniais skaičiais. Išveskite visus
# skaičius didesnius nei vidurkis.

# numbers = []
# for i in range(random.randint(3, 10)):
#     numbers.append(random.randint(0, 20))
#
# average = sum(numbers)/len(numbers)
#
# more = [number for number in numbers if number > average]
#
# print(f'Visi: {numbers}')
# print(f'Vidurkis: {average}')
# print(f'Daugiau negu vidurkis: {more}')

# 28.Susikurkite programą, kurioje būtų sukurtas sąrašas iš pasirinkto kiekio
# atsitiktinių skaičių. Raskite kiekvieno skaičiaus daliklius, pavyzdžiui:

# numbers = []
# for i in range(random.randint(3, 10)):
#     numbers.append(random.randint(0, 20))
#
# numbers.sort()
#
# print(f'Skaičiai: {str(numbers)[1:-1]}')
#
# numbers = list(dict.fromkeys(numbers))
# print(f'Unikalūs: {str(numbers)[1:-1]}')
#
#
#
# factors_total = []
# for number in numbers:
#     factors = []
#     for factor in range(1, number+1):
#         if number % factor == 0:
#             factors.append(factor)
#     factors_total.append(factors)
#
# for index, sk in enumerate(numbers):
#     if sk == 0:
#         print(f'Skaičius 0 dalinasi iš visų įmanomų skaičių')
#     else:
#         print(f'Skaičius {sk} dalinasi iš {str(factors_total[index])[1:-1]}')

# 29.Sukurkite programą, kurioje vartotojas galėtų įvesti norimą kiekį žodžių
# (pasirenka iš pradžių ir vykdomas for iki to kiekio skaičiaus, arba
# vykdomas while kol neįveda q ar kokio kito simbolio/žodžio). Išveskite
# visus šiuos žodžius ekrane.


# zodziai = []
# while True:
#     zodis = input('Naujas žodis. Baigus, spausti ENTER: ')
#     if zodis != '':
#         zodziai.append(word)
#     else:
#         break
# print(str(zodziai)[1:-1])

# 30.Susikurkite sąrašą iš pasirinktų žodžių. Atskirose eilutėse išveskite patį
# žodį, jo raidžių kiekį.

zodziai = []
while True:
    zodis = input('Naujas žodis. Baigus, spausti ENTER: ')
    if zodis != '':
        zodziai.append(zodis)
    else:
        break

for zodis in zodziai:
    print(f'{zodis}: {len(zodis)}')

print("hi")
print("hi")
print("hi")
print("hi")
print("hi")



