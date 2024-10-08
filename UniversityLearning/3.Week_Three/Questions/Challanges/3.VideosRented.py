#[textbook][3] Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals. The program should prompt the user for the number of each type of video and output the total cost. 

newVideoPrice = 3.00
oldVideoPrice = 2.00


numberOfNewVideos = int(input("Enter the number of new videos rented: "))
numberOfOldVideos = int(input("Enter the number of old videos rented: "))

TC = (numberOfNewVideos * newVideoPrice) + (numberOfOldVideos * oldVideoPrice)

print(f"Total rental cost is: $ {round(TC, 2)}")
 