def readData(filename):
    '''
    Lee datos del problema

    Parámetros:
    filename -- archivo
    '''
    data = []

    with open(filename, 'r') as data_file:
        number = int(data_file.readline().rstrip())
        for line in data_file:
            data_line = []
            l = line.rstrip()
            if l:
                for i in l.split():
                    data_line.append(int(i))
                data.append(data_line)

    if len(data) != number*2:
        rows = int((len(data)/2) / number) #numero de filas que componen una fila real

        distance,flow = [],[]
        for i in range(number):
            distance.append([item for sublist in data[:rows] for item in sublist])
            del data[:rows]

        for i in range(number):
            flow.append([item for sublist in data[:rows] for item in sublist])
            del data[:rows]

        return number, distance, flow

    return number, data[:number], data[number:]

def readSol(filename):
    '''
    Lee solucion del problema

    Parámetros:
    filename -- archivo
    '''
    data = []

    with open(filename, 'r') as data_file:
        first = data_file.readline().rstrip().split()

        data= []
        for line in data_file:
            l = line.rstrip()
            if l:
                for i in l.split():
                    data.append(int(i))

    return int(first[1]),data