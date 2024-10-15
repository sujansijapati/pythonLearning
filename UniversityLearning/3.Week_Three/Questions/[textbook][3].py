#[textbook][3] Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals. The program should prompt the user for the number of each type of video and output the total cost. 

newVideo = 3.00
oldVideo = 2.00

RentalnewVideo = float(input("Enter the number of new video tapes that is in rent: "))
RentaloldVideo = float(input("Enter the number of old video tapes that is in rent: "))

TotalRentalnewVideo = newVideo * RentalnewVideo
TotalRentaloldVideo = oldVideo * RentaloldVideo

TotalCost = TotalRentalnewVideo + TotalRentaloldVideo

print(f"The total cost of video tape is {TotalCost} ")