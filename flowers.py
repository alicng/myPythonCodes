flowers = ['Jasmine','Rose','Lily','Daisy','Tulip']
with open('write_test.txt',mode='w') as flower:
    for i in flowers:
        flower.writelines(i+'\n')
with open('write_test.txt',mode='r') as read_file:
    print(read_file.read()) 