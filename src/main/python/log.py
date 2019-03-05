#Trace and log, via console and .log file.

def startLogging():
    with open("GBAPM.log", 'w') as f:
        f.write("//GBAPM LOG file. Debug purpouses.\n")
        f.close()

def trace(title_, content_):
    title = str(title_)
    content = str(content_)
    
    print("#" + title + ": " + content)
    with open("GBAPM.log", 'a') as f:
        f.write("#" + title + ": " + content + "\n")
        f.close()