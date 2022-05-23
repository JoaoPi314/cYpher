#include "cesar.h"


Cesar::Cesar(uint8_t key, uint8_t keyRange, bool onlyAlpha) : key(key), keyRange(keyRange), onlyAlpha(onlyAlpha){}


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
}


bool Cesar::isOnlyAlpha(){
	return this->onlyAlpha;
}

void Cesar::setOnlyAlpha(bool onlyAlpha){
	this->onlyAlpha = onlyAlpha;
}