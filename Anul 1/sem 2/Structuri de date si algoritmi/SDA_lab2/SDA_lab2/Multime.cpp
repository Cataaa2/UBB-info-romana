#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>
#define INITIAL_CAPACITY 10

Multime::Multime() {
	// BC = WC = AC = General = Theta(1)
	this->capacitate = 0;
	this->lungime = 0;
	this->minim = 0;
	this->elems = NULL;
}


bool Multime::adauga(TElem elem) {
	// BC = Theta(1)
	// WC = Theta(n)
	// AC = Theta(n)
	if (this->capacitate == 0) {
		this->capacitate = INITIAL_CAPACITY;
		this->minim = elem;
		this->elems = new bool[this->capacitate]();
		this->elems[elem - minim] = true;
		this->lungime++;
		return true;
	}
	if (this->minim <= elem && elem <= this->minim + this->capacitate - 1) {
		if (this->elems[elem - minim] == false) {
			this->elems[elem - minim] = true;
			this->lungime++;
			return true;
		}
		else return false;
	}
	else
	{
		redim(elem);
		this->lungime++;
		this->elems[elem - minim] = true;
		return true;
	}
	return false;
}

void Multime::redim(TElem elem_nou) {
	// BC = WC = AC = General = Theta(n)
	int i, min = this->minim, max = this->minim + this->capacitate - 1, new_cap, val_veche, new_index;
	if (elem_nou < min) min = elem_nou;
	if (elem_nou > max) max = elem_nou;
	new_cap = max - min + 1;
	bool* new_elems = new bool[new_cap]();
	for (i = 0; i < this->capacitate; i++) {
		if (this->elems[i] == true) {
			val_veche = this->minim + i;
			new_index = val_veche - min;
			new_elems[new_index] = true;
		}
	}
	delete[] this->elems;
	this->minim = min;
	this->capacitate = new_cap;
	this->elems = new_elems;
}

bool Multime::sterge(TElem elem) {
	// BC = WC = AC = General = Theta(1)
	if (this->minim <= elem && elem <= this->minim + this->capacitate - 1) {
		int index = elem - minim;
		if (this->elems[index] == true) {
			this->elems[index] = false;
			this->lungime--;
			return true;
		}
	}
	return false;
}


bool Multime::cauta(TElem elem) const {
	// BC = WC = AC = General = Theta(1)
	if (this->minim <= elem && elem <= this->minim + this->capacitate - 1) {
		int index = elem - minim;
		return this->elems[index];
	}
	return false;
}


int Multime::dim() const {
	// BC = WC = AC = General = Theta(1)
	return this->lungime;
}

bool Multime::vida() const {
	// BC = WC = AC = General = Theta(1)
	return this->lungime == 0;
}


Multime::~Multime() {
	// BC = WC = AC = General = Theta(1)
	delete[] this->elems;
	this->elems = nullptr;
}



IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

