# Program name: Strange_Spencer_FinalProject.py
# Author: Spencer Strange
# Summary: Calculate a variety of useful information regarding candle making. How much wax and fragrance oil for a project, based on potency of fragrance desited
# Variables: 
#   welcome
#   weightType
#   waxName
#   specificGravity
#   pricePerWeightType
#   meltOrCandle
#   fragranceLoad
#   fragranceOil
#   
   
# https://armatagecandlecompany.com/blog/wax-per-candle/ 
# https://armatagecandlecompany.com/blog/fragrance-oil-calculations/ 
# https://armatagecandlecompany.com/blog/specific-gravity/ 
# Desktop > candle-math.pdf

def main():
    # init program, determine weight type
    welcome = str(input("Welcome to Strange Wickworks Wickworking Calcualtor. Would you like to begin? Y/N: "))
    while welcome.upper() != "Y" and welcome.upper() != "N":
        welcome = str(input("Error... You have entered an invalid command. Please enter Y or N: "))
    while welcome.upper() == "Y":
        weightType = str(input("Will you be using grams or ounces for your measurements? (Reminder to not use fluid ounces): "))
        while weightType.upper() != "GRAMS" and weightType.upper() != "OUNCES":
            weightType = str(input("ERROR... You have input an inproper weight type. Please enter a proper weight type: "))
        if weightType.upper() == "GRAMS":
            print("You have chosen grams.")
        if weightType.upper() == "OUNCES":
            print("You have chose ounces. Reminder to not use fluid ounces, as your measurments will not be accurate.")

        # choose from list of waxes to determine specific gravity as well as wax price
        waxName = str(input("Please select the type of wax you will be using: \n A. Paraffin wax \n B. Soy wax \n C. Beeswax  \n"))
        while waxName.upper() != "A" and waxName.upper() != "B" and waxName.upper() != "C":
            waxName = str(input("ERROR... Please enter a valid response: "))
        if waxName.upper() == "A":
            specificGravity = 0.92
            if weightType.upper() == "GRAMS":
                pricePerWeightType = float(input("What is the price of your wax per gram? "))
            else:
                pricePerWeightType = float(input("What is the price of your wax per ounce? "))
            
        if waxName.upper() == "B":
            specificGravity = 0.89
            if weightType.upper() == "GRAMS":
                pricePerWeightType = float(input("What is the price of your wax per gram? "))
            else:
                pricePerWeightType = float(input("What is the price of your wax per ounce? "))
            
        if waxName.upper() == "C":
            specificGravity = 0.95
            if weightType.upper() == "GRAMS":
                pricePerWeightType = float(input("What is the price of your wax per gram? "))
            else:
                pricePerWeightType = float(input("What is the price of your wax per ounce? "))
            
                

        # define container parameters
        containerName = str(input("What is the name of the container you'd like to use? "))
        meltOrCandle = str(input("Is this a wax melt or candle container? "))
        while meltOrCandle.upper() != "MELT" and meltOrCandle.upper() != "CANDLE":
            meltOrCandle = str(input("ERROR... You have entered an inproper response. Please respond with either '"'Melt'"' or '"'Candle'"': "))
        if meltOrCandle.upper() == "MELT" or meltOrCandle.upper() == "CANDLE":
            # determine information about desired fragrance throw and load, as well as price
            fragranceLoad = int(input("As a whole number between 3 and 12, please enter how strong you would like the product you are making to smell. "))
            while fragranceLoad > 12 or fragranceLoad < 3:
                fragranceLoad = int(input("ERROR... You have input an invalid number. Please enter a number between 3 and 12. "))
            if weightType.upper() == "GRAMS":
                fragrancePrice = float(input("How much does your fragrance oil cost per gram? "))
            else:
                fragrancePrice = float(input("How much does your fragrance oil cost per ounce? "))
        # measure container for amount of wax needed per container for project
        print("Your previously defined measurement unit is", weightType)
        emptyWeight = float(input("Measure the container while it is empty, and provide the weight in your previously defined unit: "))
        waterAndContWeight = float(input("Fill your container to the height you wish to fill it with wax. Include the container weight in your measurement. Provide this weight in your previously defined unit: "))
        # caluation of amount of wax and fragrance oil needed
        waterWeight = waterAndContWeight - emptyWeight
        totalWeight = waterWeight * specificGravity
        fragranceLoadPercent = fragranceLoad / 100
        waxWeight = totalWeight / (1 + fragranceLoadPercent)
        fragranceOil = totalWeight - waxWeight
        pricePerCont = float(input("What is the price of one container? "))
        
        # amount of wax and oil per num of containers, calcuation of prices of raw materials
        numOfCont = int(input("How many containers would you like to use? "))
        totalWax = waxWeight * numOfCont
        totalOil = fragranceOil * numOfCont
        priceOfConts = numOfCont * pricePerCont
        waxPrice = pricePerWeightType * totalWax
        totFragrancePrice = fragrancePrice * totalOil
        totalMaterialCost = priceOfConts + waxPrice + totFragrancePrice
        # profit calcuation
        profitInput = float(input("What percentage of profit would you like to make from your product? (Enter as a whole number): "))
        while profitInput < 0:
            profitInput = float(input("Error... Enter a valid amount that is at least 0: "))
        profitPercentage = profitInput / 100
        profitMultiplier = profitPercentage + 1
        totalSellForProfit = totalMaterialCost * profitMultiplier
        sellPricePerUnit = totalSellForProfit / numOfCont
        totalProfit = totalSellForProfit - totalMaterialCost
        # display caluated information
        print("In order to purchase all supplies needed, you will need to spend: $", format( totalMaterialCost, ".2f"))
        if weightType.upper() == "GRAMS":
            print("Amount of wax to purchase (in grams):", format( totalWax, ".2f"))
            print("Amount of fragrance oil to purchase (in grams):", format( totalOil, ".2f"))
        else:
            print("Amount of wax to purchase (in ounces):", format( totalWax, ".2f"))
            print("Amount of fragrance oil to purchase (in ounces):", format( totalOil, ".2f"))
        print("To make your desired amount of profit, you will need to sell each product for $", format(sellPricePerUnit, ".2f"))
        print("This will generate profits of $", format(totalProfit, ".2f"))
        welcome = str(input("Would you like to calculate again? Y/N: ")) 
    if welcome.upper() == "N":
        print("End of program. Thank you for using Strange Wickworks Wickworking Calculator.")
    
main()