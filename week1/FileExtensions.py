def main():
    fileName = input('File Name: ')
    fileTypeCheck(fileName)
    
def fileTypeCheck(fileName):
    fileName = fileName.strip()
    ext = fileName.split('.')[1].casefold()
    if ext  == 'gif':
        print('image/gif')
    elif ext == 'jpg' or ext == 'jpeg':
        print('image/jpeg')
    elif ext == 'png':
        print('image/png')
    elif ext == 'pdf':
            print('application/pdf')
    elif ext == 'txt':
            print('text/plain')
    elif ext == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')
    
main()