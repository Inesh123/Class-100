class Car(object):
    def __init__(self,model,color,company):
        self.color=color
        self.model=model
        self.company=company
    def start(self):
        print('started')
    def stop(self):
        print('stopped')
audi=Car('A8','black','audi')
print(audi.stop())