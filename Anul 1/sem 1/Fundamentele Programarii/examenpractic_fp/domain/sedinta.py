import datetime


class Sedinta:
    def __init__(self,data,ora,subiect,fel):
        """
        functie care creeaza o sedinta
        :param data: str
        :param ora: str
        :param subiect: str
        :param fel: str
        """
        self.__data = data
        self.__ora = ora
        self.__subiect = subiect
        self.__fel = fel

    def get_data(self):
        return self.__data

    def get_ora(self):
        return self.__ora

    def get_subiect(self):
        return self.__subiect

    def get_fel(self):
        return self.__fel

    def get_data_obj(self):
        return datetime.datetime.strptime(self.__data,"%d.%m")

    def get_data_zi(self):
        parti_data = self.__data.split(".")
        return datetime.datetime.strptime(parti_data[0],"%d")

    def get_data_luna(self):
        parti_data = self.__data.split(".")
        return datetime.datetime.strptime(parti_data[1],"%m")

    def __str__(self):
        return f"Data: {self.__data}, ora: {self.__ora}, subiectul:{self.__subiect}, felul:{self.__fel}"