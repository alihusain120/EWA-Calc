

def fuckingEWACalculator(listOfLengths):

    alphaErrors = []
    for alpha in [.3, .5, .8]:

        listOfPredErrors = []

        for listOfNums in listOfLengths:

            listOutput = [0]
            ewa = 0
            
            for c in listOfNums:
                ewa = (alpha*c) + ((1-alpha)*(listOutput[-1]))
                listOutput.append(ewa)

            listOutput.pop(0)
            print("EWA: Website " + str(listOfLengths.index(listOfNums)+1) + " alpha=" + str(alpha))
            print("Index |\t Length | C(n) | Pred. Err.")
            sumPredError = 0
            for i in range(len(listOutput)):
                predError = abs(listOutput[i]-listOfNums[i])
                sumPredError += predError
                print(str(i+1) + " \t " + str(listOfNums[i]) + " \t " +
                      str(listOutput[i]) + "\t\t" + str(predError))

            avgPredError = sumPredError/len(listOfNums)
            print("Avg. Pred. Error: " + str(avgPredError))
            print("")
            listOfPredErrors.append(avgPredError)

        print("")
        for i in range(len(listOfPredErrors)):
            print("Website " + str(i+1) + " Avg. Pred Error: " + str(listOfPredErrors[i]))

        overallAvgError = sum(listOfPredErrors)/len(listOfPredErrors)
        print("Overall Avg. Error: " + str(overallAvgError))
        alphaErrors.append(overallAvgError)


    print("")
    print("Alpha = 0.3, avg. pred. error: " + str(alphaErrors[0]))
    print("Alpha = 0.5, avg. pred. error: " + str(alphaErrors[1]))
    print("Alpha = 0.8, avg. pred. error: " + str(alphaErrors[2]))
    


def testEWACalc():
    lenss = [[3, 2, 4, 2, 2], [4, 5, 3, 2, 3, 4], [2, 3, 2, 1, 3, 2]]
    print("Input: " + str(lenss))
    print("------------EWA--------------")
    fuckingEWACalculator(lenss)
    


