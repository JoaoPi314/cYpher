#ifndef CAESAR_H
#define CAESAR_H

#include <iostream>
#include <cstdint>
#include <string>

using namespace std;

class Caesar{
private:
	uint8_t key;
	uint8_t keyRange;
	bool onlyAlpha;

public:
	Caesar(uint8_t, uint8_t, bool);

	uint8_t getKey();
	void setKey(uint8_t);

	uint8_t getKeyRange();
	void setKeyRange(uint8_t);

	bool isOnlyAlpha();
	void setOnlyAlpha(bool);

	string crypt(string);
	string decrypt(string);

};



#endif