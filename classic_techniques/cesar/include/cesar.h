#ifndef CESAR_H
#define CESAR_H

#include <iostream>
#include <cstdint>
#include <string>

using namespace std;

class Cesar{
private:
	uint8_t key;
	uint8_t keyRange;
	bool onlyAlpha;

public:
	Cesar(uint8_t, uint8_t, bool);

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