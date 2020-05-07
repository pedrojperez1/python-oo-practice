from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Special case of WordFinder that ignores empty lines or lines starting with # comment"""
    
    def read_words(self, filepath):
        with open(filepath) as file:
            words = file.read().split('\n')
            return [w.strip() for w in words 
                    if w.strip() != '' and w[0] != '#']


    