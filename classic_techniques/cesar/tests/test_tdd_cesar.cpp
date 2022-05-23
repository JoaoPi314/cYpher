#include <gtest/gtest.h>
#include <string>
#include "cesar.h"

TEST(TestTddCesar, CanCreateCesar) {
	Cesar cesar(5, 26, true);

	GTEST_ASSERT_EQ(5, cesar.getKey());
	GTEST_ASSERT_EQ(26, cesar.getKeyRange());
	GTEST_ASSERT_EQ(true, cesar.isOnlyAlpha());

}
