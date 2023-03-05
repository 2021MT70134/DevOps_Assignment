import re
import importlib
import inspect

class MyClass:

    def inputField():
        out_data= dict()
        import temp as fileObj 
        for name, obj in inspect.getmembers(fileObj):
            # print(name,obj)
            if (isinstance(obj,str) or isinstance(obj,list) or isinstance(obj,dict) or isinstance(obj,int) )and not str(name).startswith('_'):
                out_data[str(name)]=obj
        return out_data

    # def fileRead():
        file=open("temp.py")
        variables = dict()
        multiline = False
        for each in file.readlines():
            each_line = each.strip()
            if each_line.startswith("#"):
                pass        
            elif not multiline and re.search("^['|\"]{3}", each_line):
                if re.search("['|\"]{3}$", each_line) and re.search("^['|\"]{3}", each_line).span() == re.search("['|\"]{3}$", each_line).span():
                    multiline = True
                elif not re.search("['|\"]{3}$", each_line):
                    multiline = True
            elif multiline:
                if re.search("['|\"]{3}$", each_line):
                    multiline = False
                else:
                    continue
            else:
                if not multiline and "=" in each_line:
                    temp = each_line.split("=")
                    variables[temp[0]] = str(temp[1])
                    if re.search("^['|\"]{3}", temp[1].strip()):
                        multiline = True
        return variables


class Requestclass:
    
    def __init__(self,ip,username,password) -> None:
        self._ip=ip
        self._username=username
        self._password=password

    def connect(self):
        import paramiko
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(self._ip, username=self._username, password=self._password)
        return client
