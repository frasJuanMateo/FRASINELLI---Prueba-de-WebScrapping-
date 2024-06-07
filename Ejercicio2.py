import requests
import os
import json

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


response = requests.get("https://jsonplaceholder.typicode.com/posts/")
response = list(map(dict, response.json()))

length = 0

while True:
    length = input("Que tan largo sera el JSON? : ")
    if length.isdecimal() == False:
        length == 0
    else:
        if int(length) >= 1 and int(length) <= 100:
            length = int(length)
            break
        else:
            length = 0

while True:
    keyWord = input("Ingresa la palabra que te gustaria filtrar: ")
    if keyWord.isalnum():
        keyWord = keyWord.lower()
        break

counter = 0
primeDict = []
notPrimeDict = []
wordCount = 0
tableData = []

for i in range(100):
    listOfWords = (" ".join(((response[i - counter]["title"] + " " + response[i - counter]["body"]).split("\n")))).split(" ")
    if response[i - counter]["id"] > length:
        del response[i - counter]
        counter += 1
    elif (not keyWord in listOfWords):
        del response[i - counter]
        counter += 1
    else:
        idWordCount = 0
        for word in (" ".join(((response[i - counter]["title"] + " " + response[i - counter]["body"]).split("\n")))).split(" "):
                
                if word == keyWord:
                    wordCount += 1
                    idWordCount += 1
        tableData.append((response[i - counter]["id"], idWordCount))

        if isPrime(response[i - counter]["id"]):
            primeDict.append(response[i - counter])
        else:
            notPrimeDict.append(response[i - counter])

if not os.path.exists("download"):
    os.mkdir("download")
os.chdir("download")

i = 1

while os.path.exists(f"dl{i}Primes.json"):
    i += 1

primeFile = open(f"dl{i}Primes.json", "w")
notPrimeFile = open(f"dl{i}NotPrimes.json", "w")
primeFile.write(json.dumps(primeDict, indent=4))
notPrimeFile.write(json.dumps(notPrimeDict, indent=4))
primeFile.close()
notPrimeFile.close()

print(f"POST ID     OCURRENCIAS DE '{keyWord}'")
for data in tableData:
    print(f"{data[0]}           {data[1]}")
print(f"Total ocurrencias de '{keyWord}':\n{wordCount}")