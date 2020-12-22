"""
File: weather_master.py
-----------------------
This program will implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.

"""
EXIT = -1


def main():
    """
    This program asks weather data from user to compute the
    average, highest, lowest, cold days among the inputs.
    """
    print('stanCode "Weather Master 4.0"!')
    data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
    if data == EXIT:
        # No temperatures were entered.
        print('No temperatures were entered.')
    else:
        # The first data was entered.
        highest = data
        # The highest temperature.
        lowest = data
        # The lowest temperature.
        sum_temperature = data
        # The SUM of the temperatures.
        amount_of_data = 1
        # Pieces of data users input.
        average = float(sum_temperature / amount_of_data)
        # The average temperature.
        if data < 16:
            # Check whether the first data is a cold day.
            cold_day = 1
        else:
            cold_day = 0
        while True:
            # The program will keep the loop until users input "EXIT".
            data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
            if data == EXIT:
                # The user exited from the program.
                break
            else:
                if data > highest:
                    highest = data
                if data < lowest:
                    lowest = data
                if data < 16:
                    cold_day += 1
                sum_temperature += data
                amount_of_data += 1
                average = float(sum_temperature / amount_of_data)
        print('Highest temperature = ' + str(highest))
        print('Lowest temperature = ' + str(lowest))
        print('Average = ' + str(average))
        print(str(cold_day) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
