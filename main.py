if __name__ == '__main__':

    file_read = open('raw.odt', 'r')
    file_write = open('processed.odt', 'w')

    data = file_read.readline()
    data_dict = {}

    while data:
        data_list = data.split("\t", 1)
        data_dict[data_list[0]] = data_list[1].strip('\t')
        data = file_read.readline()

    list_keys = list(data_dict.keys())
    # list_values = data_list.values()
    for i in range(0, len(list_keys)):
        file_write.write(list_keys[i] + "\t\t" + data_dict[list_keys[i]] + "\n")
    file_read.close()
    file_write.close()
