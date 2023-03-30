import StudentData


def sortFileID(inputFile):
    tempListData = []  # Create a list that will hold all the information.
    with open(inputFile, 'r') as file:  # Opens a file.
        for line in file.readlines():  # Reads each line in the file.
            tempInformation = line.split()
            # This creates a new student object for each line in the file.
            tempStudent = StudentData.Student(int(tempInformation[0]),
                                              tempInformation[1], tempInformation[2],
                                              tempInformation[3], tempInformation[4])
            tempListData.append(tempStudent)
        file.close()
        return tempListData
