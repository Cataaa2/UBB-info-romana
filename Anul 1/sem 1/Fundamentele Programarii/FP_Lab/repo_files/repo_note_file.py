from exceptii.eroare_repo import EroareRepo


class RepositoryNoteFisier:

    def __init__(self,filename):
        # note = {id_student: {(nrlab,nrprob): nota}}
        self.__note = {}
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__filename,"r") as f:
            linii = f.readlines()
            for linie in linii:
                linie.strip()
                if linie != "":
                    parti = linie.split(",")
                    id_student = int(parti[0])
                    nrlab = int(parti[1])
                    nrprob = int(parti[2])
                    nota = None if parti[3].strip() == "None" else float(parti[3])
                    cheie = (nrlab,nrprob)
                    if id_student not in self.__note:
                        self.__note[id_student] = {}
                    self.__note[id_student][cheie] = nota

    def __save_to_file(self):
        with open(self.__filename,"w") as f:
            for id,laburi in self.__note.items():
                for cheie in laburi:
                    nota = laburi[cheie]
                    f.write(f"{id},{cheie[0]},{cheie[1]},{nota}\n")

    def asignare_laborator(self,id_student,nrlab,nrproblema):
        if id_student not in self.__note:
            self.__note[id_student]= {}
            self.__save_to_file()
        cheie = (nrlab,nrproblema)
        if cheie in self.__note[id_student]:
            raise EroareRepo("Laboratorul este deja asignat acestui student")
        self.__note[id_student][cheie] = None
        self.__save_to_file()

    def notare_laborator(self,id_student,nrlab,nrproblema,nota):
        if id_student not in self.__note:
            raise EroareRepo("studentul nu are acest laborator asignat")
        cheie = (nrlab,nrproblema)
        if cheie not in self.__note[id_student]:
            raise EroareRepo("studentul nu are acest laborator asignat")
        self.__note[id_student][cheie] = nota
        self.__save_to_file()

    def get_note_student(self, id_student):
        if id_student not in self.__note:
            return {}
        return self.__note[id_student]

    def actualizeaza_id_student(self, id_vechi, id_nou):
        if id_vechi in self.__note:
            self.__note[id_nou] = self.__note[id_vechi]
            del self.__note[id_vechi]
            self.__save_to_file()

    def actualizeaza_lab(self,lab_vechi,prob_vechie,lab_nou,prob_noua):
        cheie_veche = (lab_vechi,prob_vechie)
        cheie_noua = (lab_nou,prob_noua)
        for id_student,laburi in self.__note.items():
            if cheie_veche in laburi:
                laburi[cheie_noua] = laburi.pop(cheie_veche)
                self.__save_to_file()

    def sterge_student(self, id_student):
        if id_student in self.__note:
            del self.__note[id_student]
            self.__save_to_file()

    def sterge_problema(self, nrlab, nrproblema):
        cheie = (nrlab, nrproblema)
        for id_student, laburi in self.__note.items():
            if cheie in laburi:
                del laburi[cheie]
                self.__save_to_file()

    def get_medie_student(self,id_student):
        suma_note = 0.0
        numar_note = 0.0
        for nota in self.__note[id_student].values():
                if nota is not None:
                    suma_note += nota
                    numar_note += 1
        if numar_note == 0:
            return 0
        medie = suma_note / numar_note
        return medie

    def cea_mai_mare_medie(self):
        max = 0.0
        ids = {}
        for id in self.__note:
            medie = self.get_medie_student(id)
            if medie > max:
                max = medie
                ids.clear()
                ids[id] = max
            elif medie == max:
                ids[id] = medie
        return ids

    def medii_sub5(self):
        ids = {}
        for id_student in self.__note:
            medie = self.get_medie_student(id_student)
            if medie < 5:
                ids[id_student] = medie
        return ids

    def studenti_cu_problema_data(self,nrlab,nrprob):
        cheie = (nrlab,nrprob)
        ids = {}
        for id_student, laburi in self.__note.items():
            if cheie in laburi:
                if laburi[cheie] is not None:
                    ids[id_student] = laburi[cheie]
        return ids

    def get_all(self):
        return self.__note