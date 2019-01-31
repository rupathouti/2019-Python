import os

#each website u crawl is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.makedirs(directory)

# create_project_dir('thenewboston') #(To check till the above def working)

#create queue and crawled files(if not created)
def create_data_files(project_name,base_url):
    queue = project_name+ '/queue.txt'
    crawled = project_name+ '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url) #waiting list

    if not os.path.isfile(crawled):
        write_file(crawled, '')

#create a new file
def write_file(path,data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# create_data_files('thenewboston','https://thenewboston.com/') #(To check till the above def working)

# add data onto an existing file

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')


#delete the contents of a file
def delete_file_contents(path):
    with open(path,'w'):
        pass

#Data should not be duplicate as we cannot keep the duplicate data in the queue
#Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))#replace parameters are 1.what you want to replace and with 2.with what you are replacing
    return results

# Iterate through a set ,each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)