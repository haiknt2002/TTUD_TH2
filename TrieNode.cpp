#include <iostream>
#include <unordered_map>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // Một unordered_map để lưu trữ các con của nút hiện tại.
    bool is_end_of_word;  // Đánh dấu xem nút hiện tại có phải là cuối của một từ hay không.

    TrieNode() : is_end_of_word(false) {}  // Khởi tạo một nút, mặc định không phải cuối của từ.
};

class Trie {
public:
    TrieNode* root;  // Gốc của cây tiền tố.

    Trie() {
        root = new TrieNode();  // Khởi tạo cây tiền tố với một nút gốc.
    }

    void insert(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                node->children[ch] = new TrieNode();  // Nếu ký tự ch chưa tồn tại trong các con của nút hiện tại, thêm một nút con mới.
            }
            node = node->children[ch];  // Di chuyển đến nút con tương ứng với ký tự ch.
        }
        node->is_end_of_word = true;  // Đánh dấu nút hiện tại là cuối của một từ.
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                return false;  // Nếu có ký tự không tồn tại trong cây, từ không tồn tại.
            }
            node = node->children[ch];
        }
        return node->is_end_of_word;  // Trả về true nếu nút hiện tại là cuối của một từ, tức là từ tồn tại.
    }
};

int main() {
    Trie trie;
    string words_to_insert[] = {"the", "a", "an", "there", "answer", "any", "by", "bye", "their"};

    for (const string& word : words_to_insert) {
        trie.insert(word);  // Chèn từng từ từ danh sách vào cây tiền tố.
    }

    string words_to_search[] = {"the", "answer", "hello", "by", "thermometer"};

    for (const string& word : words_to_search) {
        if (trie.search(word)) {
            cout << "'" << word << "' found in the trie." << endl;  // Kiểm tra xem từ có tồn tại trong cây tiền tố không và in kết quả.
        } else {
            cout << "'" << word << "' not found in the trie." << endl;
        }
    }

    return 0;
}
