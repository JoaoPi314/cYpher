#include <gtest/gtest.h>
#include <string>
#include "cesar.h"

/***
 * Tests if the Cesar Object can be created 
 ***/

TEST(TestTddCesar, CanCreateCesar) {
	Cesar cesar(5, 26, true);

	GTEST_ASSERT_EQ(5, cesar.getKey());
	GTEST_ASSERT_EQ(26, cesar.getKeyRange());
	GTEST_ASSERT_EQ(true, cesar.isOnlyAlpha());

}


/***
 * Tests if the key can be changed
 ***/
TEST(TestTddCesar, CanChangeKey) {
	Cesar cesar(50, 26, true);

	cesar.setKey(20);
	GTEST_ASSERT_EQ(20, cesar.getKey());
}


/***
 * Tests if the keyRange can be changed.
 * The alpha boolean must be changed if range is greater than 26
 ***/
TEST(TestTddCesar, CanChangeKeyRange) {
	Cesar cesar(50, 26, true);

	cesar.setKeyRange(50);
	GTEST_ASSERT_EQ(50, cesar.getKey());
	GTEST_ASSERT_EQ(false, cesar.isOnlyAlpha());
}

/***
 * Tests if the alphabetic flag can be changed
 * The flag can be changed only if the range is
 * lesser or equal to 26.
 ***/

TEST(TestTddCesar, InvalidAlphaFlag) {
	Cesar cesar(2, 45, false);

	cesar.setOnlyAlpha(true);
	GTEST_ASSERT_EQ(false, cesar.isOnlyAlpha());
}


TEST(TestTddCesar, ValidAlphaFlag) {
	Cesar cesar(2, 26, false);

	cesar.setOnlyAlpha(true);
	GTEST_ASSERT_EQ(true, cesar.isOnlyAlpha());
}

