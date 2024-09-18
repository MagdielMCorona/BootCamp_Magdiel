# The challenge involves creating a bidding system.
# HINT: Think about how you can use dictionaries to solve this problem.

# Import the required modules. These modules are provided to you.
from art import logo
import os


def clear():
    # Using os.system() to execute the clear command specific to the operating system.
    os.system('cls' if os.name == 'nt' else 'clear')

    # DOS and Windows('nt'): Microsoft's DOS had the cls command to clear the screen. Windows, which initially started as a graphical layer over DOS, maintained a lot of command-line compatibility with DOS for ease of transition and backward compatibility. So, when Windows NT(New Technology) came about, it kept the cls command for clearing the screen.
    # Unix and Unix-like Systems: Unix is an OS that dates back to the 1970s. The command-line interface for Unix used the clear command. Many modern OSes, including Linux and macOS, are derived or inspired by Unix, so they keep the clear command for compatibility and tradition.

clear()

# Start by printing the provided logo.
print(logo)

# Create a dictionary to hold the bids.
bids_dict = {}

seguir = input("¿Quieres hacer una puja? (Y/N) ")

while seguir == "Y":
        name = input("¿Cuál es el nombre del pujador? ")
        puja = int(input("¿Cuál es la cantidad de su puja? "))
        bids_dict[name] = puja
        print(bids_dict)
        seguir = input("¿Quieres hacer una puja? (Y/N) ")

# TODO: Set an initial state for the bidding process.

# TODO: Create a function to determine the highest bidder.

def find_highest_bidder(bidding_record):

    # Initialize the necessary variables to determine the winner.
    nombre_ganador = None
    valor_ganador = 0

    # Loop through the dictionary to determine the highest bid.
    for clave, valor in bids_dict.items():
         if valor > valor_ganador:
              valor_ganador = valor
              nombre_ganador = clave
        

    # Print out the highest bidder.
    return nombre_ganador, valor_ganador
    # TODO: Use a loop to continue receiving bids until there are no more bidders.

    # Remember to clear the console after each bid to keep the current bid private.

nombre_ganador_final, cantidad_ganador_final = find_highest_bidder(bids_dict)

print("El ganador de la subasta es ", nombre_ganador_final , "y su puja fue de ", cantidad_ganador_final)

