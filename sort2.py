class Number:
    def __init__(self, string):
        self.value = float(string)
        self.string = string

    def __str__(self):
        return self.string

    def __cmp__(self, other):
        return cmp(self.value, other.value) or cmp(self.string, other.string)


def segregated_sort(input_list):
    """Returns a sorted copy of the input list that maintains the same
    type of data at each index of the output as the type of data at that
    index in the input."""
    types = [type(datum) for datum in input_list]
    sorted_data_by_type = {
        t: iter(sorted(datum for datum in input_list if type(datum) == t))
        for t in set(types)
    }
    return [next(sorted_data_by_type[t]) for t in types]

def to_number_where_possible(words):
    """Returns a copy of the input list in which any word that looks
    numeric is converted to a Number."""
    def convert(word):
        try:
            return Number(word)
        except ValueError:
            return word
    return [convert(word) for word in words]

if __name__ == '__main__':
    split_input = raw_input().split()
    result = segregated_sort(to_number_where_possible(split_input))
    print(' '.join(str(r) for r in result))
