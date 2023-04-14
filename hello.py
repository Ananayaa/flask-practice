class person:
    def _init_(self,username,name,email,phoneno):
        self.username=username
        self.name=name
        self.email=email
        self.phoneno=phoneno
    
    def details(self):
        print(self.username)
        print(self.name)
        print(self.email)
        print(self.phoneno)

       
    a="this is my person class"
    print(a)