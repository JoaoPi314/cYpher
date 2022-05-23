#include "cesar.h"


Cesar::Cesar(uint8_t key, uint8_t keyRange, bool onlyAlpha) : key(key), keyRange(keyRange){
	this->setOnlyAlpha(onlyAlpha);
}

uint8_t Cesar::getKey(){
	return this->key;
}

void Cesar::setKey(uint8_t key){
	this->key = key;
}

uint8_t Cesar::getKeyRange(){
	return this->keyRange;
}

void Cesar::setKeyRange(uint8_t keyRange){
	this->keyRange = keyRange;

	if (this->getKeyRange() > 26)
		this->setOnlyAlpha(false);
}


bool Cesar::isOnlyAlpha(){
	return this->onlyAlpha;
}

void Cesar::setOnlyAlpha(bool onlyAlpha){
	if(this->getKeyRange() > 26)
		this->onlyAlpha = false;
	else
		this->onlyAlpha = onlyAlpha;
}