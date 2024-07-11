#This program will read flavors and their sales from a file and will produce output based on them.
PRICE = 1.99
def main():
    #Declare and initialize variables
    content = []
    flavors = []
    sales = []
    salesCopy = []
    highIndex = 0
    stripped_list = []
    bestFlavors = ""
    inFile = ""
    try:
        inFile = open("sales.txt", "r")
        content = inFile.readlines() #This reads the content of the file to a list
        inFile.close()
        #print(content)
        for item in content:
            stripped_list.append(item.rstrip('\n')) #This will strip the new line
        #print(stripped_list)
        for j in range(0, len(content), 2):
            flavors.append(content[j].rstrip("\n")) #This will append each flavor from the content list to a list called flavor
            sales.append(int(content[j + 1])) #This will append each sale from the content list to a list called sales
        #print(flavors)
        #print(sales)
        salesCopy = [] + sales #Create a copy of the sales list
        
        print("\n\t\t***********************")
        print("\t\t*TOP 5 SELLING FLAVORS*")
        print("\t\t***********************")
        print("\t{0:3s}{1:14s}{2:4s}{3:8s}{4:3s}{5:8s}".format("","FLAVOR","","#SOLD", "","SALES"))
        print("\t{0:3s}{1:0s}".format("","----------------------------------"))
        bestFlavors = FindBest(flavors, salesCopy)
        sameSales = FindSameSales(flavors, salesCopy, bestFlavors)
        FinalOutput(flavors, sales)



    except IOError:
        print("\n\tThe file is not available. Program terminates!")
        sys.exit()

def FindSameSales(flavors, salesCopy, bestFlavors):
    saleIndex = 0
    sameFlavor = ""
    sameSales = 0
    for i in range(len(salesCopy)): #This loop goes through the loop for the lenght of the salesCopy list
        if salesCopy[i] == bestFlavors:
            saleIndex = i 
            sameSales = salesCopy[saleIndex] #Find the index if the sale read is equal to the 5th best flavor
            sameFlavor = flavors[saleIndex] #Find the flavor associate with the sales found 
            print("\t{0:3s}{1:14s}{2:2s}{3:8,.2f}{4:4s}${5:,.2f}".format("",sameFlavor, "", sameSales, "", sameSales*PRICE))
    
def FindBest(flavors, salesCopy):
    highSale = 0
    highFlavor = ""
    highIndex = 0
    for g in range(0,5,1):
        highSale = max(salesCopy)
        highIndex = salesCopy.index(highSale) #Find the index of the highest sale each time through the loop
        highFlavor = flavors[highIndex] #Find the flavor associate with the sales found each time through the loop
        print("\t{0:3s}{1:14s}{2:2s}{3:8,.2f}{4:4s}${5:,.2f}".format("",highFlavor, "", highSale, "", highSale*PRICE))
        salesCopy[highIndex] = 0
    return highSale

def FinalOutput(flavors, sales):
    minIndex = sales.index(min(sales))
    print("\n\n{0:s} is the lowest flavor of sales for the month with {1:,d} sold.".format(flavors[minIndex],min(sales)))
    print("The total number of shakes sold for the month are: {0:,d}".format(sum(sales)))
    print("The average number of shakes sold for the month per flavor is: {0:,.1f}".format(sum(sales)/len(sales)))
    print("The total sales for the month are: ${0:,.2f}".format(sum(sales)*PRICE))
    print("The average sales for the month per flavor is: ${0:,.2f}".format(sum(sales)*PRICE/len(sales)))
    
    
    
    






main()
