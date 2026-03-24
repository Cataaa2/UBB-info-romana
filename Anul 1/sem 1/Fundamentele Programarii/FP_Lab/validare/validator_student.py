from exceptii.eroare_validator import EroareValidator


class ValidatorStudent:

    def valideaza_student(self,student):
        """
        functie care valideaza un student
        :param student: student cu id int, nume str si grup str
        :return: -, daca studentul e valid
                    eroare "id student invalid!\n" daca id student e <0
                    eroare "nume student invalid!\n" daca nue student e gol
                    eroare "grup student invalid!\n" daca grup <0
        """
        erori = ""
        if student.get_id_student() <0:
            erori += "id student invalid!\n"
        if student.get_nume() == "":
            erori += "nume student invalid!\n"
        if student.get_grup() <0:
            erori += "grup student invalid!\n"
        if len(erori) > 0:
            raise EroareValidator(erori)