import os
import stdiomask
from time import sleep
import colorama
from colorama import Fore, Style

colorama.init()

'''password = os.environ.get('PASSWORD')'''
password = 'PCJPVTSPMRCCPOCBACS'
guess = ""
guess_count = 0
guess_limit = 3
guesses_left = 2
out_of_guesses = False

'''
print("You have 3 tries left")
guess = input("Enter password to access encryptor: ")
if guess == password:
    print("You may encrypt")
else:
'''
print("You have 3 tries")

while guess != password and not out_of_guesses:
    if guess_count < guess_limit:

        guess = stdiomask.getpass("Enter password to access encryptor: ")
        if guess == password:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.GREEN)
            print("ACCESS GRANTED" + Style.RESET_ALL)

        elif guess == "pila":
            print("Haha era o que tu querias na boca")

        else:
            if guesses_left != 1:
                print("Wrong, you have " + str(guesses_left) + " tries left")

            else:
                print("Wrong, you have " + str(guesses_left) + " try left")
            guess_count += 1
            guesses_left -= 1
    else:
        out_of_guesses = True
        if out_of_guesses:
            print(Fore.RED)
            print("ACCESS DENIED")
            sleep(1.5)
            print(
                "--:m-----:------------::::-------------------::::--------------------:-------------------------+d---")
            sleep(0.1)
            print(
                "--:m----:mNNh-:mNNh-smNNNNd+-+NNm:+NNN/----+dNNNNmo--mNNo-yNNd---yNNNN+--:mNNo-----dNNy--------+d---")
            sleep(0.1)
            print(
                "--:m-----yMMN:oMMM+oMMMyhMMN:oMMN:+MMM/---/NMMhyMMM+-MMMs-yMMm---mMMMMy--:NMMs-----mMMy--------+d---")
            sleep(0.1)
            print(
                "--:m-----:mMMohMMh-sMMN:+MMM/oMMN:+MMM/---/MMM+:dhy/-MMMs-yMMm--:MMNMMm--:NMMs-----mMMy--------+d---")
            sleep(0.1)
            print(
                "--:m------oMMdNMN:-oMMN:+MMM/oMMN:+MMM/---/NMMh+:----MMMs:hMMm--oMMhNMN:-:NMMs-----mMMy--------+d---")
            sleep(0.1)
            print(
                "--:m-------dMMMMs--oMMN:+MMM/oMMN:+MMM/----/ymMNms/--MMMNNNMMm--yMMsdMM+-:NMMs-----mMMy--------+d---")
            sleep(0.1)
            print(
                "--:m-------+MMMm:--sMMN:+MMM/oMMN:+MMM/------:+dMMN+-MMMdhmMMm--mMM+hMMs-:NMMs-----mMMy--------+d---")
            sleep(0.1)
            print(
                "--:m--------NMMy---oMMN:+MMM/oMMN:+MMM/---:shd//MMMo-MMMs-yMMm-:NMMydMMd-:NMMs-----mMMy--------+d---")
            sleep(0.1)
            print(
                "--:m--------NMMy---oMMN:+MMM/oMMN:+MMM/---/MMM+:MMMo-MMMs-yMMm-+MMMNNMMN::NMMs-----mMMy--------+d---")
            sleep(0.1)
            print(
                "--:m--------NMMy---+NMMhdMMm:+NMMhdMMN:---:NMMdhMMN/-MMMs-yMMm-yMMm/+MMM/:NMMNmmmo-mMMNmmmy----+d---")
            sleep(0.1)
            print(
                "--:m--------hddo----+hmmmdy/--+hmmmdy/:+---/ydmmdh+--dddo-sddh-yddy-:ddd+:dddddddo-hdddddds----+d---")
            sleep(0.1)
            print(
                "--:m-------------------------------------------------------------------------------------------+d---")
            sleep(0.1)
            print(
                "--:m----------ohh+--ohhy--:shddhs/-shhhhhhhy----/hhhhhyo/--:yhhhy---:oyhdhy+--:oyhdhy+---------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNm:-yNNN-:mNNmmNNN+hmNNNNNmd----/NNNmmNNm/-+NNNNN/--yNNNdNNNy-hNNNdNNNs--------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNNy-yNNN-/NNN+:NNNs:/+NNNo/:----/NNNo/NNNs-sNNNNNo--mNNh-hNmh:mNNy-dNmh--------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNNN+yNNN-/NNN+:NNNs--/NNN+------/NNN+:NNNs-hNNhNNy--mNNh:///::mNNh://::--------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNNNmhNNN-/NNN+:NNNs--/NNN+------/NNNo+NNNs-mNNoNNd--smNNds/---ymNNdo/----------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNNNNNNNN-/NNN+:NNNs--/NNN+------/NNNNNNNd//NNN/NNN:--:odNNNh+--/odNNNh/--------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNmyNNNNN-/NNN+:NNNs--/NNN+------/NNNyso+:-oNNm:mNN+--:::/mNNd--:::/mNNd--------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNm:dNNNN-/NNN+:NNNs--/NNN+------/NNN+-----yNNNdNNNs-hmNy-hNNd-hmNy-dNNd--------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNm-+NNNN-/NNNo:NNNs--/NNN+------/NNN+-----mNNmmNNNh-mNNy:hNNd:mNNy:dNNd--------+d---")
            sleep(0.1)
            print(
                "--:m----------hNNm--yNNN-:mNNmmNNN+--/NNN+------/NNN+----:NNNo-sNNm:yNNNdNNNy-hNNNdNNNs--------+d---")
            sleep(0.1)
            print(
                "--:m----------ohhs--:yhy--:shddhs/---:hhh/------:yhh/----/yhh/-+hhy:-+yhdhy+---oyhdhy+---------+d---")
            sleep(0.1)
            print("--:m-------------------------------------------------------------------------------------------+d--")
            sleep(2.5)
            exit()

VOWELS = [ord(c.upper()) for c in ["a", "e", "i", "o", "u"]]
CONSONANTS = [ord(c.upper()) for c in
              ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]]
# Salva o numero da letra maiúscula em ascii estupido

LOWER_CONST = 0x20
UPPER_MASK = 0xff ^ LOWER_CONST


def better_encryption(message: str, is_encrypt: bool):
    newMessage = ""
    ed = 1 if is_encrypt else -1

    for letter in message:
        res = None

        letter = ord(letter)  # convertes a letra para o número ascii paneleiro
        case = letter & LOWER_CONST  # salvas o sexto bit gay da merda
        letter &= UPPER_MASK  # mudas o sexto bit para 0 e deixas os outros iguais parvo

        if letter in VOWELS:
            newIndex = (VOWELS.index(letter) + ed) % len(VOWELS)
            res = VOWELS[newIndex]

        elif letter in CONSONANTS:
            newIndex = (CONSONANTS.index(letter) + ed) % len(CONSONANTS)
            res = CONSONANTS[newIndex]

        else:
            res = letter  # Não muda a letra caralho

        res |= case  # repoe o sexto bit da letra asno da merda
        newMessage += chr(res)  # Converte o res do numero correspondente ao ascii puta

    return newMessage


def main():
    while True:
        command = input("[E]ncrypt, [D]ecrypt or [P] to exit? ")

        if len(command) == 0:  # És tão gay que doi oh João
            continue

        if command[0].upper() == 'E':
            print(better_encryption(input("Message: "), True))  # encripta esta merda toda

        elif command[0].upper() == 'D':
            print(better_encryption(input("Message: "), False))  # desencripta esta merda toda


        elif command[0].upper() == 'P':
            print("Thank you for encrypting with us")
            print(Fore.RED)
            print(" __          __        _                _____                               ")
            sleep(0.5)
            print(" \ \        / /       | |              / ____|                              ")
            sleep(0.5)
            print("  \ \  /\  / /__  _ __| |_ ___ _ __   | (___   ___ _ __ ___  _ __  _ __ ___ ")
            sleep(0.5)
            print("   \ \/  \/ / _ \| '__| __/ _ \ '_ \   \___ \ / _ \ '_ ` _ \| '_ \| '__/ _ \ ")
            sleep(0.5)
            print("    \  /\  / (_) | |  | ||  __/ | | |  ____) |  __/ | | | | | |_) | | |  __/")
            sleep(0.5)
            print("     \/  \/ \___/|_|   \__\___|_| |_| |_____/ \___|_| |_| |_| .__/|_|  \___|")
            sleep(0.5)
            print("                                                            | |             ")
            sleep(0.2)
            print("                                                            |_|             ")
            sleep(3)
            exit()

        else:
            print("Invalid Command")


if __name__ == "__main__":
    main()
