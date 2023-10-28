class TrieNode:
    def __init__(self):
        self.children = {}  # Một từ điển (dictionary) để lưu trữ các con của nút hiện tại.
        self.is_end_of_word = False  # Đánh dấu xem nút hiện tại có phải là cuối của một từ hay không.

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Khởi tạo cây tiền tố với một nút gốc (root).

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Nếu ký tự char chưa tồn tại trong các con của nút hiện tại, thêm một nút con mới.
            node = node.children[char]  # Di chuyển đến nút con tương ứng với ký tự char.
        node.is_end_of_word = True  # Đánh dấu nút hiện tại là cuối của một từ.

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Nếu có ký tự không tồn tại trong cây, từ không tồn tại.
            node = node.children[char]
        return node.is_end_of_word  # Trả về True nếu nút hiện tại là cuối của một từ, tức là từ tồn tại.

def main():
    words_to_insert = ["the", "a", "an", "there", "answer", "any", "by", "bye", "their"]
    trie = Trie()  # Tạo một cây tiền tố mới.

    for word in words_to_insert:
        trie.insert(word)  # Chèn từng từ từ danh sách vào cây tiền tố.

    words_to_search = ["the", "answer", "hello", "by", "thermometer"]
    
    for word in words_to_search:
        if trie.search(word):
            print(f"'{word}' found in the trie.")  # Kiểm tra xem từ có tồn tại trong cây tiền tố không và in kết quả.

if __name__ == "__main__":
    main()
