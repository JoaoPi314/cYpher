#include "../include/caesar.h"


Caesar::Caesar(int key, bool onlyAlpha) {
	this->setOnlyAlpha(onlyAlpha);
	this->keyRange = onlyAlpha ? 26 : 95;
	this->setKey(key);
}

int Caesar::getKey(){
	return this->key;
}

void Caesar::setKey(int key){
	this->key = key % this->getKeyRange();
}

int Caesar::getKeyRange(){
	return this->keyRange;
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
		bool isNotCapitalized = (clearMessage[i] > 96 && clearMessage[i] < 123);
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


