import os

#Each website you crawl is a seperate project (folder)
""" ye esm (STR) migire o folderi be on naam age nabashe misaze """
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project ' + directory )
        os.makedirs(directory)

# Create queue and crawled files (if not created)
""" nam proje (STR) & base url (STR) ro migireh 
    file haye queue.txt & crawled.txt ro misazeh"""
def create_data_files(project_name, base_url):
    queue = project_name + 'queue.txt'
    crawled = project_name + 'crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

# Create a new file
""" path (STR),data (STR) ro migireh
    ba hazf data haye ghabli path
    data ro toye path minevise """
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

# Add data onto an existing file
""" path (STR),data (STR) ro migireh
    bedon hazf data haye ghabli path
    data ro be path ezafe mikone """
def append_to_file(path,data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of a file
""" path (STR) ro migire
"""
def delete_file_contents(path):
    with open(path, 'w'):
        # do nothing
        pass

# Read a file and convert each line to set items
"""
    path (STR) ro migireh
    mohtaviate file ro mirize to SET va barmigardone
"""
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# Iterate through a set , each item will be a new line in the file
""" path (STR) & link (SET) ro migire
    mohtaviate path ro pak mikone 
    va mohtaviate links ro toye file minevise
"""
def set_fo_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)
