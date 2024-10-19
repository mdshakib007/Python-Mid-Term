

class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        if id in self.__seats:
            print(f"Show with ID {id} already exists!")
            return
        
        show = (id, movie_name, time)
        self.__show_list.append(show)
        
        seat_list = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        self.__seats[id] = seat_list
    
    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print("\tInvalid show ID!")
            return
        
        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"\tInvalid seat ({row}, {col})!")
                continue

            if self.__seats[id][row][col] == 1:
                print(f"\tSeat ({row}, {col}) is already booked!")
            else:
                self.__seats[id][row][col] = 1
                print(f"\tSeat ({row}, {col}) booked successfully!")
    
    def view_show_list(self):
        print("\n\tRunning shows: ")
        for show in self.__show_list:
            print(f"\t{show}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"\n\tNo show found with ID {id}")
            return
        
        print(f"\n\tAvailable seats for ID {id}:")
        for row in range(self.__rows):
            print("\t", end='')
            for col in range(self.__cols):
                print(self.__seats[id][row][col], end=" ")
            print()


cinema = Star_Cinema()

h1 = Hall(5, 5, "Hall-1")
cinema.entry_hall(h1)

h1.entry_show("101", "1 Takar Prem", "03/11/2024")
h1.entry_show("102", "Beder Meye Josna", "03/11/2024")
h1.entry_show("103", "No. 1 Shakib Khan", "03/11/2024")

while True:
    print("Navigate to:")
    print("1. View All Running Shows")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")
    
    op = input(">>> ")
    if op == "1":
        h1.view_show_list()
    
    elif op == "2":
        id = input("Enter movie id: ")
        h1.view_available_seats(id)

    elif op == "3":
        id = input("Enter movie id: ")
        tickets = int(input("How many tickets do you need: "))
        seat_list = []
        for i in range(tickets):
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            seat_list.append((row, col))
        h1.book_seats(id, seat_list)

    elif op == "4":
        break

    else:
        print("\n\tInvalid input!")
