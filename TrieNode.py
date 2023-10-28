class TrieNode:
    def __init__(self):
        self.children = {}  # Một từ điển (dictionary) để lưu trữ chỉ số của các nút con.
        self.is_end_of_word = False  # Đánh dấu xem nút hiện tại có phải là cuối của một từ hay không.

class Trie:
    def __init__(self):
        self.nodes = [TrieNode()]  # Sử dụng một danh sách để lưu trữ các nút.

    def insert(self, word):
        node_index = 0  # Bắt đầu từ nút gốc.
        for char in word:
            if char not in self.nodes[node_index].children:
                new_node_index = len(self.nodes)
                self.nodes[node_index].children[char] = new_node_index  # Thêm chỉ số của nút con mới.
                self.nodes.append(TrieNode())  # Thêm một nút con mới vào danh sách.
            node_index = self.nodes[node_index].children[char]  # Di chuyển đến nút con tương ứng.
        self.nodes[node_index].is_end_of_word = True  # Đánh dấu nút hiện tại là cuối của một từ.

    def search(self, word):
        node_index = 0  # Bắt đầu từ nút gốc.
        for char in word:
            if char not in self.nodes[node_index].children:
                return False  # Nếu có ký tự không tồn tại trong cây, từ không tồn tại.
            node_index = self.nodes[node_index].children[char]
        return self.nodes[node_index].is_end_of_word  # Trả về True nếu nút hiện tại là cuối của một từ, tức là từ tồn tại.

def main():
    trie = Trie()
    words_to_insert = ["the", "a", "an", "there", "answer", "any", "by", "bye", "their"]

    for word in words_to_insert:
        trie.insert(word)  # Chèn từng từ từ danh sách vào cây tiền tố.

    words_to_search = ["the", "answer", "hello", "by", "thermometer"]

    for word in words_to_search:
        if trie.search(word):
            print(f"'{word}' found in the trie.")  # Kiểm tra xem từ có tồn tại trong cây tiền tố không và in kết quả.
        else:
            print(f"'{word}' not found in the trie.")

if __name__ == "__main__":
    main()
