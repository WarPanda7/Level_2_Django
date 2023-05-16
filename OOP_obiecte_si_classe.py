class Title:
    def __init__(self, text):
        self.text=text
    def __str__(self):
        return "-= "+ self.text.upper()+" =-"
t1=Title("Programing in Python 3")
print(t1)