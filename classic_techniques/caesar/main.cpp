#include "include/caesar.h"


int main(int argc, char const *argv[])
{

	bool onlyAlpha = false;
	int key = 56;

	Caesar caesar(key, onlyAlpha);
	cout << "*********************************" << endl;
	cout << "* Caesar Cypher demonstration   *" << endl;
	cout << "*********************************" << endl;
	cout << endl;
	cout << "Secret Key: " << caesar.getKey() << endl;
	cout << "Character space to caesar cipher: " << caesar.getKeyRange() << endl;
	cout << ((onlyAlpha) ? "Using only the alphabet" : "Using all ASCII table") << endl;
	cout << endl;
	cout << endl;

	string clearText = "The key to enter the house is under the carpet.";

	cout << "*****************" << endl;
	cout << "* Clear text    *" << endl;
	cout << "*****************" << endl;
	cout << endl;
	cout << clearText << endl;
	cout << endl;
	cout << "*****************" << endl;
	cout << "* Cipher text   *" << endl;
	cout << "*****************" << endl;
	cout << endl;

	string cipherMessage = caesar.crypt(clearText);

	cout << cipherMessage << endl;
	cout << endl;
	cout << "Decrypting..." << endl;
	cout << endl;
	cout << "*****************" << endl;
	cout << "* Clear text   *" << endl;
	cout << "*****************" << endl;
	cout << endl;
	cout << caesar.decrypt(cipherMessage) << endl;


	return 0;
}