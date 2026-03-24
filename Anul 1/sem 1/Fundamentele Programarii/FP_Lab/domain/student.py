class Student:
    def __init__(self, id_student, nume, grup):
        """
        functie care creeaza un student
        :param id_student: int
        :param nume: str
        :param grup: int
        """
        self.__id_student = id_student
        self.__nume = nume
        self.__grup = grup

    def get_id_student(self):
        return self.__id_student

    def get_nume(self):
        return self.__nume

    def get_grup(self):
        return self.__grup

    def set_id(self, id_nou):
        self.__id_student = id_nou

    def set_nume(self, nume):
        self.__nume = nume

    def set_grup(self, grup):
        self.__grup = grup

    def __str__(self):
        return f"ID: {self.__id_student}, Nume: {self.__nume}, Grup: {self.__grup}"