import unittest

from jm_tools.trie import JMTrie


class TestJMTrie(unittest.TestCase):
    def test_insert_and_search(self):
        trie = JMTrie()
        trie.insert("cat")
        trie.insert("car")
        self.assertTrue(trie.search("cat"))
        self.assertTrue(trie.search("car"))
        self.assertFalse(trie.search("ca"))
        self.assertFalse(trie.search("dog"))

    def test_starts_with(self):
        trie = JMTrie()
        trie.insert("hello")
        self.assertTrue(trie.starts_with("he"))
        self.assertFalse(trie.starts_with("hi"))

    def test_empty_string(self):
        trie = JMTrie()
        trie.insert("")
        self.assertTrue(trie.search(""))
        self.assertTrue(trie.starts_with(""))

    def test_insert_many(self):
        trie = JMTrie()
        trie.insert_many(["a", "ab", "abc"])
        self.assertTrue(trie.search("a"))
        self.assertTrue(trie.search("ab"))
        self.assertTrue(trie.search("abc"))

    def test_words_with_prefix(self):
        trie = JMTrie()
        trie.insert_many(["cat", "car", "cart", "dog"])
        words = trie.words_with_prefix("car")
        self.assertEqual(set(words), {"car", "cart"})

    def test_words_with_prefix_limit(self):
        trie = JMTrie()
        trie.insert_many(["cat", "car", "cart", "carbon"])
        words = trie.words_with_prefix("car", limit=2)
        self.assertEqual(len(words), 2)
        for word in words:
            self.assertTrue(word.startswith("car"))

    def test_contains(self):
        trie = JMTrie()
        trie.insert("foo")
        self.assertTrue("foo" in trie)
        self.assertFalse("bar" in trie)

    def test_type_validation(self):
        trie = JMTrie()
        with self.assertRaises(TypeError):
            trie.insert(123)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            trie.search(123)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            trie.starts_with(123)  # type: ignore[arg-type]

    def test_normalization_lowercases_words(self):
        trie = JMTrie()
        trie.insert("Hello")
        self.assertTrue(trie.search("hello"))
        self.assertTrue(trie.search("HELLO"))
        self.assertTrue(trie.starts_with("he"))
        self.assertEqual(trie.words_with_prefix("He"), ["hello"])

    def test_frequency_ranking(self):
        trie = JMTrie()
        trie.insert("cat")
        trie.insert("car")
        trie.insert("cat")
        trie.insert("cart")
        trie.insert("cart")
        trie.insert("cat")
        words = trie.words_with_prefix("ca")
        self.assertEqual(words, ["cat", "cart", "car"])

    def test_frequency_ties_are_lexicographic(self):
        trie = JMTrie()
        trie.insert_many(["dog", "deer", "deal"])
        words = trie.words_with_prefix("d")
        self.assertEqual(words, ["deal", "deer", "dog"])

    def test_limit_respects_frequency_order(self):
        trie = JMTrie()
        trie.insert("cat")
        trie.insert("car")
        trie.insert("cat")
        trie.insert("cart")
        trie.insert("cart")
        trie.insert("cat")
        words = trie.words_with_prefix("ca", limit=2)
        self.assertEqual(words, ["cat", "cart"])

    def test_delete_removes_word_only(self):
        trie = JMTrie()
        trie.insert_many(["cat", "car", "cart"])
        self.assertTrue(trie.delete("car"))
        self.assertFalse(trie.search("car"))
        self.assertTrue(trie.search("cat"))
        self.assertTrue(trie.search("cart"))
        self.assertEqual(trie.words_with_prefix("ca"), ["cart", "cat"])

    def test_delete_missing_returns_false(self):
        trie = JMTrie()
        self.assertFalse(trie.delete("missing"))

    def test_update_sets_frequency(self):
        trie = JMTrie()
        trie.insert_many(["alpha", "beta", "gamma"])
        trie.update("beta", 5)
        trie.update("gamma", 2)
        words = trie.words_with_prefix("", limit=3)
        self.assertEqual(words, ["beta", "gamma", "alpha"])

    def test_update_zero_deletes(self):
        trie = JMTrie()
        trie.insert("cat")
        trie.update("cat", 0)
        self.assertFalse(trie.search("cat"))

    def test_record_selection_increments_frequency(self):
        trie = JMTrie()
        trie.insert_many(["cat", "car"])
        trie.record_selection("car")
        trie.record_selection("car")
        words = trie.words_with_prefix("ca", limit=1)
        self.assertEqual(words, ["car"])

    def test_compressed_trie_behaves_like_standard(self):
        trie = JMTrie(compress=True)
        trie.insert("Hello")
        trie.insert("helium")
        trie.insert("hello")

        self.assertTrue(trie.search("HELLO"))
        self.assertTrue(trie.starts_with("he"))
        self.assertEqual(trie.words_with_prefix("he", limit=2), ["hello", "helium"])

        trie.update("helium", 5)
        self.assertEqual(trie.words_with_prefix("he", limit=1), ["helium"])

        self.assertTrue(trie.delete("hello"))
        self.assertFalse(trie.search("hello"))

        trie.record_selection("hero")
        self.assertTrue(trie.search("hero"))

    def test_compressed_prefix_mid_edge(self):
        trie = JMTrie(compress=True)
        trie.insert_many(["cart", "carpet"])
        self.assertEqual(trie.words_with_prefix("ca"), ["carpet", "cart"])


if __name__ == "__main__":
    unittest.main()
