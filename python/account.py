class Account:
    id = int
    name = str
    document = str
    emial = str
    password = str

    def __init__(self, name, document):
        self.name = name
        self.document = document