from exceptii.eroare_repo import EroareRepo


class RepositoryStudenti:

    def __init__(self):
        self.__studenti = {}

    def __len__(self):
        return len(self.__studenti)

    def adauga_student(self, student):
        id_student = student.get_id_student()
        if id_student in self.__studenti:
            raise EroareRepo("id student existent!")
        self.__studenti[id_student] = student

    def sterge_student(self, id_student):
        if id_student not in self.__studenti:
            raise EroareRepo("id student inexistent!")
        del self.__studenti[id_student]

    def actualizeaza_student(self, id_student, id_nou, nume_nou, grup_nou):
        if id_student not in self.__studenti:
            raise EroareRepo("id student inexistent!")

        student = self.__studenti[id_student]
        # daca schimbam ID-ul
        if id_student != id_nou:
            if id_nou in self.__studenti:
                raise EroareRepo("id student nou existent!")
            del self.__studenti[id_student]
            student.set_id(id_nou)
            self.__studenti[id_nou] = student

        student.set_nume(nume_nou)
        student.set_grup(grup_nou)

    def get_all(self):
        return list(self.__studenti.values())

    def get_student_dupa_id(self, id_student):
        if id_student in self.__studenti:
            return self.__studenti[id_student]
        raise EroareRepo("id student inexistent!")