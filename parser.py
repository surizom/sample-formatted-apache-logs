import datetime
import uuid
import csv

def parse_line(lineArray):

    infos = {}

    infos["id"] = uuid.uuid4().hex
    date = datetime.datetime.strptime(lineArray[0], '%a %b %d %H:%M:%S %Y')
    infos["timestamp"] = str(date.date()) + " " + str(date.time())
    if len(lineArray) < 4:
        infos["logLevel"] = lineArray[1]
        infos["logMessage"] = lineArray[2]
        infos["origin"] = ""
    else:
        infos["logLevel"] = lineArray[1]
        infos["logMessage"] = lineArray[3]
        infos["origin"] = lineArray[2].split(" ")[1]

    return infos


logs = open("Apache.log", "r")

output = open("sample.csv", "w")

writer = csv.writer(output)

writer.writerow(["id", "timestamp",
                     "logLevel", "origin", "logMessage"])

linesToWrite = []

for line in logs:

    lineArray = line.split("] ")
    for i in range(len(lineArray)):
        lineArray[i] = lineArray[i].replace("]", "")
        lineArray[i] = lineArray[i].replace("[", "")
        lineArray[i] = lineArray[i].replace("\n", "")
        lineArray[i] = lineArray[i].replace("\"", "")
    try:
        writeLine = parse_line(lineArray)
        linesToWrite.append(writeLine)
    except:
        print("cannot read line " + line)

for writeLine in linesToWrite:
    writer.writerow([writeLine["id"], writeLine["timestamp"],
                     writeLine["logLevel"], writeLine["origin"], writeLine["logMessage"]])

logs.close()
output.close()
