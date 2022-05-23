#include "caesar.h"


Caesar::Caesar(uint8_t key, uint8_t keyRange, bool onlyAlpha) : keyRange(keyRange){
	this->setOnlyAlpha(onlyAlpha);
	this->setKey(key);
}

uint8_t Caesar::getKey(){
	return this->key;
}

void Caesar::setKey(uint8_t key){
	
	this->key = key % this->getKeyRange();
}

uint8_t Caesar::getKeyRange(){
	return this->keyRange;
}

void Caesar::setKeyRange(uint8_t keyRange){
	this->keyRange = keyRange;

	if (this->getKeyRange() > 26)
		this->setOnlyAlpha(false);
}


bool Caesar::isOnlyAlpha(){
	return this->onlyAlpha;
}

void Caesar::setOnlyAlpha(bool onlyAlpha){
	if(this->getKeyRange() > 26)
		this->onlyAlpha = false;
	else
		this->onlyAlpha = onlyAlpha;
}

string Caesar::crypt(string clearMessage){
	string cipherMessage = clearMessage;

	for(int i = 0; i < cipherMessage.length(); i++){
		bool isCapitalized = (cipherMessage[i] > 64 && cipherMessage[i] < 91);
		bool isNotCapitalized = (cipherMessage[i] > 96 && cipherMessage[i] < 122);
		bool overlapCapitalized = (isCapitalized && (cipherMessage[i] + this->getKey()) > 91);
		bool overlapNotCapitalized = (isNotCapitalized && (cipherMessage[i] + this->getKey()) > 122); 

		bool overlapASCII = (cipherMessage[i] + this->getKey() > 126);


		if (this->isOnlyAlpha() && (isCapitalized || isNotCapitalized)){
			cipherMessage[i] += this->getKey();
			if(overlapCapitalized || overlapNotCapitalized)
				cipherMessage[i] -= this->getKeyRange();	
		}
		else if (!this->isOnlyAlpha()){
			cipherMessage[i] += this->getKey();
				if(overlapASCII)
					cipherMessage[i] -= this->getKeyRange();		
		}
	}
	return cipherMessage;
}


string Caesar::decrypt(string cipherMessage){
	string clearMessage = cipherMessage;

	for(int i = 0; i < cipherMessage.length(); i++){
		bool isCapitalized = (clearMessage[i] > 64 && clearMessage[i] < 91);
		bool isNotCapitalized = (clearMessage[i] > 96 && clearMessage[i] < 122);
		bool overlapCapitalized = (isCapitalized && (clearMessage[i] - this->getKey()) < 65);
		bool overlapNotCapitalized = (isNotCapitalized && (clearMessage[i] - this->getKey()) < 97); 

		bool overlapASCII = (clearMessage[i] - this->getKey() < 32);

		if (this->isOnlyAlpha() && (isCapitalized || isNotCapitalized)){
			clearMessage[i] -= this->getKey();
			if(overlapCapitalized || overlapNotCapitalized)
				clearMessage[i] += this->getKeyRange();	
		}
		else if (!this->isOnlyAlpha()){
			clearMessage[i] -= this->getKey();
				if(overlapASCII)
					clearMessage[i] += this->getKeyRange();		
		}
	}
	return clearMessage;
}


