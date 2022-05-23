#ifndef CAESAR_H
#define CAESAR_H

#include <iostream>
#include <cstdint>
#include <string>

using namespace std;

class Caesar{
private:
	int key;
	int keyRange;
	bool onlyAlpha;

public:
	Caesar(int, bool);

	int getKey();
	void setKey(int);

	int getKeyRange();

	bool isOnlyAlpha();
	void setOnlyAlpha(bool);

	string crypt(string);
	string decrypt(string);

};



#endif