#include "IteratorMultime.h"
#include "Multime.h"


IteratorMultime::IteratorMultime(const Multime& m) : multime(m){
	// BC = Theta(1)
	// WC = Theta(n)
	// AC = Theta(n)
	prim();
}


void IteratorMultime::prim() {
	// BC = Theta(1)
	// WC = Theta(n)
	// AC = Theta(n)
	this->poz = 0;
	while (this->poz < this->multime.capacitate && this->multime.elems[this->poz] == false) {
		this->poz++;
	}
}


void IteratorMultime::urmator() {
	// BC = Theta(1)
	// WC = Theta(n)
	// AC = Theta(n)
	this->poz++;
	while (this->poz < this->multime.capacitate && this->multime.elems[this->poz] == false) {
		this->poz++;
	}
}


TElem IteratorMultime::element() const {
	// BC = WC = AC = General = Theta(1)
	if (this->poz < this->multime.capacitate) {
		return this->poz + this->multime.minim;
	}
	return -1;
}

bool IteratorMultime::valid() const {
	// BC = WC = AC = General = Theta(1)
	if (this->poz < this->multime.capacitate && this->multime.elems[this->poz] == true) {
		return true;
	}
	return false;
}
