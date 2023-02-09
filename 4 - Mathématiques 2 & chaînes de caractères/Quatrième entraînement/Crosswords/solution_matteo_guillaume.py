class Trie:
    def __init__(self):
        self.links = {}
    
    def add_word(self, word):
        if word != '':
            self.links.setdefault(word[0], Trie()).add_word(word[1:])
    
    
rows, col_words_len = map(int, input().split())
cols, row_words_len = map(int, input().split())
    
col_words = Trie()
row_words = Trie()
    
for i in range(col_words_len):
    col_words.add_word(input())
    
for i in range(row_words_len):
    row_words.add_word(input())
    
    
def place_letter(row, col, col_ptrs, row_ptr):
    if col == cols:
        col = 0
        row_ptr = row_words
        row += 1
    
    if row == rows:
        return 1
    
    configs = 0
    
    for letter in row_ptr.links:
        if letter in col_ptrs[col].links:
            cur_col_ptrs = col_ptrs.copy()
            cur_col_ptrs[col] = cur_col_ptrs[col].links[letter]
    
            configs += place_letter(
                row, col + 1,
                cur_col_ptrs, row_ptr.links[letter]
            )
    
    return configs
    
    
print(place_letter(0, 0, [col_words] * cols, row_words)) 
