def file(filename,data):
    file = open(filename, 'a+')
    file.write(data)
    file.close()
