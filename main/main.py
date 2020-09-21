# PHILIP ROBERTS 2020

import translate
import readWrite

userString = readWrite.fileToString("data.txt")

programOutput = translate.translateString(userString)

readWrite.stringToFile("output.txt", programOutput)

