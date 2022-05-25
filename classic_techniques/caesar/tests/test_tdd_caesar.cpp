#include <gtest/gtest.h>
#include <string>
#include "caesar.h"

/***
 * Tests if the Caesar Object can be created 
 ***/
TEST(TestTddCaesar, CanCreateCaesar) {
	Caesar caesar(5, 26, true);

	GTEST_ASSERT_EQ(5, caesar.getKey());
	GTEST_ASSERT_EQ(26, caesar.getKeyRange());
	GTEST_ASSERT_EQ(true, caesar.isOnlyAlpha());
}

/***
 * Tests if the key can be changed
 ***/
TEST(TestTddCaesar, CanChangeKey) {
	Caesar caesar(50, 26, true);

	caesar.setKey(20);
	GTEST_ASSERT_EQ(20, caesar.getKey());
}


/***
 * Tests if the keyRange can be changed.
 * The alpha boolean must be changed if range is greater than 26
 ***/
TEST(TestTddCaesar, CanChangeKeyRange) {
	Caesar caesar(50, 26, true);

	caesar.setKeyRange(50);
	GTEST_ASSERT_EQ(50, caesar.getKeyRange());
	GTEST_ASSERT_EQ(false, caesar.isOnlyAlpha());
}

/***
 * Tests if the alphabetic flag can be changed
 * The flag can be changed only if the range is
 * lesser or equal to 26.
 ***/
TEST(TestTddCaesar, InvalidAlphaFlag) {
	Caesar caesar(2, 45, false);

	caesar.setOnlyAlpha(true);
	GTEST_ASSERT_EQ(false, caesar.isOnlyAlpha());
}


TEST(TestTddCaesar, ValidAlphaFlag) {
	Caesar caesar(2, 26, false);

	caesar.setOnlyAlpha(true);
	GTEST_ASSERT_EQ(true, caesar.isOnlyAlpha());
}

/***
 * Tests if the Caesar can crypt a given message with alphabetic characteres
 * and with no overlap
 ***/
TEST(TestTddCaesar, CanCryptOnlyAlphaNoOverlap) {
	Caesar caesar(2, 26, true);

	string clearMessage = "Testing Caesar Method.";
	string cipherMessage = "Vguvkpi Ecguct Ogvjqf.";

	GTEST_ASSERT_EQ(cipherMessage, caesar.crypt(clearMessage));
}

/***
 * Tests if the Caesar can crypt a given message with alphabetic characteres
 * and with Overlap
 ***/
TEST(TestTddCaesar, CanCryptOnlyAlphaOverlap) {
	Caesar caesar(15, 26, true);

	string clearMessage = "This_will_overlap!";
	string cipherMessage = "Iwxh_lxaa_dktgape!";

	GTEST_ASSERT_EQ(cipherMessage, caesar.crypt(clearMessage));
}


/***
 * Tests if the Caesar can crypt a given message with all ASCII table characters
 ***/
TEST(TestTddCaesar, CanCryptGeneralASCII) {
	Caesar caesar(26, 95, false);

	string clearMessage = "The Definitive Test.";
	string cipherMessage = "n# :^ !$)$/$1 :n ./H";

	GTEST_ASSERT_EQ(cipherMessage, caesar.crypt(clearMessage));
}

/***
 * Tests if the Caesar can decrypt a given message with only alphabetic
 ***/
TEST(TestTddCaesar, CanDecryptAlpha) {
	Caesar caesar(15, 26, true);

	string cipherMessage = "Iwxh_lxaa_dktgape!";
	string clearMessage = "This_will_overlap!";

	GTEST_ASSERT_EQ(clearMessage, caesar.decrypt(cipherMessage));
}


/***
 * Tests if the Caesar can decrypt a given message with ASCII
 ***/
TEST(TestTddCaesar, CanDecryptASCII) {
	Caesar caesar(26, 95, false);

	string clearMessage = "The Definitive Test.";
	string cipherMessage = "n# :^ !$)$/$1 :n ./H";

	GTEST_ASSERT_EQ(clearMessage, caesar.decrypt(cipherMessage));
}

