

class Node():
    __slots__ = ("children", "is_terminal", "frequency", "max_subtree_frequency")

    def __init__(self):
        self.children = {}
        self.is_terminal = False
        self.frequency = 0
        self.max_subtree_frequency = 0


class JMTrie():

    def __init__(self, compress: bool = False):
        self.root = Node()
        self._compress = compress

    @staticmethod
    def _normalize_word(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        return value.lower()

    @staticmethod
    def _common_prefix_length(left: str, right: str) -> int:
        limit = min(len(left), len(right))
        index = 0
        while index < limit and left[index] == right[index]:
            index += 1
        return index

    @staticmethod
    def _recompute_max(node) -> None:
        max_child_frequency = 0
        for child in node.children.values():
            if child.max_subtree_frequency > max_child_frequency:
                max_child_frequency = child.max_subtree_frequency
        own_frequency = node.frequency if node.is_terminal else 0
        node.max_subtree_frequency = max(own_frequency, max_child_frequency)

    def _recompute_path(self, path) -> None:
        for node in reversed(path):
            self._recompute_max(node)

    def _insert_standard(self, word: str, count: int) -> None:
        node = self.root
        path = [node]
        for letter in word:
            next_node = node.children.get(letter)
            if next_node is None:
                next_node = node.children[letter] = Node()
            node = next_node
            path.append(node)
        node.is_terminal = True
        node.frequency += count
        self._recompute_path(path)

    def _insert_radix(self, word: str, count: int) -> None:
        node = self.root
        path = [node]
        remaining = word
        while True:
            if remaining == "":
                node.is_terminal = True
                node.frequency += count
                self._recompute_path(path)
                return

            matched_full_edge = False
            for edge, child in list(node.children.items()):
                common_length = self._common_prefix_length(remaining, edge)
                if common_length == 0:
                    continue
                if common_length == len(edge):
                    node = child
                    path.append(node)
                    remaining = remaining[common_length:]
                    matched_full_edge = True
                    break

                common_prefix = edge[:common_length]
                edge_remainder = edge[common_length:]
                word_remainder = remaining[common_length:]

                intermediate = Node()
                intermediate.children[edge_remainder] = child
                del node.children[edge]
                node.children[common_prefix] = intermediate
                node = intermediate
                path.append(node)

                if word_remainder == "":
                    node.is_terminal = True
                    node.frequency += count
                    self._recompute_path(path)
                    return

                new_child = Node()
                new_child.is_terminal = True
                new_child.frequency = count
                node.children[word_remainder] = new_child
                path.append(new_child)
                self._recompute_path(path)
                return

            if matched_full_edge:
                continue

            new_child = Node()
            new_child.is_terminal = True
            new_child.frequency = count
            node.children[remaining] = new_child
            path.append(new_child)
            self._recompute_path(path)
            return

    def insert(self, word: str, count: int = 1) -> None:
        word = self._normalize_word(word)
        if not isinstance(count, int) or count <= 0:
            raise ValueError("count must be a positive integer")
        if self._compress:
            self._insert_radix(word, count)
        else:
            self._insert_standard(word, count)

    def _walk_standard(self, word: str):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return None
        return node

    def _walk_radix(self, word: str):
        node = self.root
        remaining = word
        while remaining:
            matched = False
            for edge, child in node.children.items():
                if remaining.startswith(edge):
                    remaining = remaining[len(edge):]
                    node = child
                    matched = True
                    break
            if not matched:
                return None
        return node

    def _walk(self, word: str):
        word = self._normalize_word(word)
        if self._compress:
            return self._walk_radix(word)
        return self._walk_standard(word)

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and node.is_terminal)

    def starts_with(self, prefix: str) -> bool:
        prefix = self._normalize_word(prefix)
        if not self._compress:
            return self._walk_standard(prefix) is not None

        node = self.root
        remaining = prefix
        while remaining:
            matched = False
            for edge, child in node.children.items():
                common_length = self._common_prefix_length(remaining, edge)
                if common_length == 0:
                    continue
                if common_length == len(remaining):
                    return True
                if common_length == len(edge):
                    remaining = remaining[common_length:]
                    node = child
                    matched = True
                    break
                return False
            if not matched:
                return False
        return True

    def insert_many(self, words) -> None:
        for word in words:
            self.insert(word)

    def update(self, word: str, frequency: int) -> bool:
        word = self._normalize_word(word)
        if not isinstance(frequency, int):
            raise ValueError("frequency must be an integer")
        if frequency <= 0:
            return self.delete(word)
        if self._compress:
            self._update_radix(word, frequency)
            return True
        node = self.root
        path = [node]
        for letter in word:
            next_node = node.children.get(letter)
            if next_node is None:
                next_node = node.children[letter] = Node()
            node = next_node
            path.append(node)
        node.is_terminal = True
        node.frequency = frequency
        self._recompute_path(path)
        return True

    def _update_radix(self, word: str, frequency: int) -> None:
        node = self.root
        path = [node]
        remaining = word
        while True:
            if remaining == "":
                node.is_terminal = True
                node.frequency = frequency
                self._recompute_path(path)
                return

            matched_full_edge = False
            for edge, child in list(node.children.items()):
                common_length = self._common_prefix_length(remaining, edge)
                if common_length == 0:
                    continue
                if common_length == len(edge):
                    node = child
                    path.append(node)
                    remaining = remaining[common_length:]
                    matched_full_edge = True
                    break

                common_prefix = edge[:common_length]
                edge_remainder = edge[common_length:]
                word_remainder = remaining[common_length:]

                intermediate = Node()
                intermediate.children[edge_remainder] = child
                del node.children[edge]
                node.children[common_prefix] = intermediate
                node = intermediate
                path.append(node)

                if word_remainder == "":
                    node.is_terminal = True
                    node.frequency = frequency
                    self._recompute_path(path)
                    return

                new_child = Node()
                new_child.is_terminal = True
                new_child.frequency = frequency
                node.children[word_remainder] = new_child
                path.append(new_child)
                self._recompute_path(path)
                return

            if matched_full_edge:
                continue

            new_child = Node()
            new_child.is_terminal = True
            new_child.frequency = frequency
            node.children[remaining] = new_child
            path.append(new_child)
            self._recompute_path(path)
            return

    def delete(self, word: str) -> bool:
        word = self._normalize_word(word)
        if self._compress:
            return self._delete_radix(word)
        node = self.root
        path = [node]
        stack = []
        for letter in word:
            next_node = node.children.get(letter)
            if next_node is None:
                return False
            stack.append((node, letter, next_node))
            node = next_node
            path.append(node)
        if not node.is_terminal:
            return False
        node.is_terminal = False
        node.frequency = 0

        for parent, letter, child in reversed(stack):
            if child.is_terminal or child.children:
                break
            del parent.children[letter]

        self._recompute_path(path)
        return True

    def _delete_radix(self, word: str) -> bool:
        node = self.root
        path = [node]
        stack = []
        remaining = word
        while remaining:
            matched = False
            for edge, child in node.children.items():
                if remaining.startswith(edge):
                    stack.append((node, edge, child))
                    node = child
                    path.append(node)
                    remaining = remaining[len(edge):]
                    matched = True
                    break
            if not matched:
                return False
        if not node.is_terminal:
            return False
        node.is_terminal = False
        node.frequency = 0

        for parent, edge, child in reversed(stack):
            if edge not in parent.children:
                continue
            child = parent.children[edge]
            if child.is_terminal or child.children:
                break
            del parent.children[edge]

        for parent, edge, child in reversed(stack):
            if edge not in parent.children:
                continue
            child = parent.children[edge]
            if child.is_terminal:
                continue
            if len(child.children) == 1:
                (grand_edge, grand_child), = child.children.items()
                new_edge = edge + grand_edge
                del parent.children[edge]
                parent.children[new_edge] = grand_child

        self._recompute_path(path)
        return True

    def record_selection(self, word: str, weight: int = 1) -> int:
        self.insert(word, count=weight)
        node = self._walk(word)
        return node.frequency if node is not None else 0

    @staticmethod
    def _is_better(candidate, worst) -> bool:
        candidate_word, candidate_frequency = candidate
        worst_word, worst_frequency = worst
        if candidate_frequency != worst_frequency:
            return candidate_frequency > worst_frequency
        return candidate_word < worst_word

    @staticmethod
    def _find_worst(results):
        worst_index = 0
        worst_word, worst_frequency = results[0]
        for index, (word, frequency) in enumerate(results[1:], start=1):
            if frequency < worst_frequency or (frequency == worst_frequency and word > worst_word):
                worst_index = index
                worst_word = word
                worst_frequency = frequency
        return (worst_word, worst_frequency), worst_index

    def _find_prefix_node_radix(self, prefix: str):
        node = self.root
        remaining = prefix
        base_prefix = ""
        if not remaining:
            return node, base_prefix
        while remaining:
            matched = False
            for edge, child in node.children.items():
                common_length = self._common_prefix_length(remaining, edge)
                if common_length == 0:
                    continue
                if common_length == len(remaining):
                    base_prefix += edge
                    return child, base_prefix
                if common_length == len(edge):
                    base_prefix += edge
                    remaining = remaining[common_length:]
                    node = child
                    matched = True
                    break
                return None
            if not matched:
                return None
        return node, base_prefix

    def _collect_all_words(self, start_node, base_prefix):
        results = []
        parts = [base_prefix] if base_prefix else []
        stack = [(start_node, iter(start_node.children.items()))]
        if start_node.is_terminal:
            results.append(("".join(parts), start_node.frequency))
        while stack:
            node, iterator = stack[-1]
            try:
                edge, child = next(iterator)
                parts.append(edge)
                if child.is_terminal:
                    results.append(("".join(parts), child.frequency))
                stack.append((child, iter(child.children.items())))
            except StopIteration:
                stack.pop()
                if parts:
                    parts.pop()
        return results

    def words_with_prefix(self, prefix: str, limit: int | None = None):
        prefix = self._normalize_word(prefix)
        if limit is not None and limit <= 0:
            return []
        if self._compress:
            found = self._find_prefix_node_radix(prefix)
            if found is None:
                return []
            node, base_prefix = found
        else:
            node = self._walk_standard(prefix)
            if node is None:
                return []
            base_prefix = prefix

        results = []
        if limit is None:
            results = self._collect_all_words(node, base_prefix)
            results.sort(key=lambda item: (-item[1], item[0]))
            return [word for word, _frequency in results]

        import heapq

        explore = [(-node.max_subtree_frequency, base_prefix, node)]
        worst = None
        worst_index = None

        while explore:
            neg_max_frequency, current_prefix, current_node = heapq.heappop(explore)
            max_frequency = -neg_max_frequency
            if worst is not None and max_frequency < worst[1]:
                break

            if current_node.is_terminal:
                candidate = (current_prefix, current_node.frequency)
                if len(results) < limit:
                    results.append(candidate)
                    if len(results) == limit:
                        worst, worst_index = self._find_worst(results)
                elif self._is_better(candidate, worst):
                    results[worst_index] = candidate
                    worst, worst_index = self._find_worst(results)

            for letter, next_node in current_node.children.items():
                heapq.heappush(
                    explore,
                    (-next_node.max_subtree_frequency, current_prefix + letter, next_node),
                )

        results.sort(key=lambda item: (-item[1], item[0]))
        return [word for word, _frequency in results]

    def __contains__(self, word: str) -> bool:
        return self.search(word)
