class Car:
    def __init__(self, **kw) -> None:
        # self.name = kw['name']
        # self.model = kw['model']

        self.name = kw.get('name')
        self.model = kw.get('model')

        print(self.name)
        print(self.model)



car = Car(name='Toyota')