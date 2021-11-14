# Hadasim project

A class that receives a text file and issues a statistical report on it.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install word2number.
```bash
pip install word2number
```


## Usage
```python
file=File_details('./text.txt')

# returns 23
file.number_rows()

# returns 253
file.number_words()

# returns ['the']
file.popular_word()

# returns (14, 11)
file.max_and_average_len_sentence()

# returns 164
file.number_specific_words()

# returns 60
file.max_num()

# returns

#  enough that in the rough outhouses of some tillers of the heavy 
#  lands adjacent to Paris, there were sheltered from the weather 
#  that very day, rude carts, bespattered with rustic mire, snuffed 
#  about by pigs, and roosted in by poultry, which the Farmer, Death, 
#  had already set apart to be his tumbrils of the Revolution. 
#  But that Woodman and that Farmer, though they
file.max_sequence_words_not_contain_k()

```

