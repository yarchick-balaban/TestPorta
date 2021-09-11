FIRST_INPUT_FILE = 'file1'
SECOND_INPUT_FILE = 'file2'

USER_SEPARATOR = 'user:'


def getNameFromPair(pair):
    """Takes the first element because name contains there, pair like: user: Claudian.
    Args:
        pair (str): raw pairs (user: Any_names).
    Returns:
        user (str): prepared name.
    """
    user = pair.split(USER_SEPARATOR)[1]
    return user.strip()


def getUniqueNamesFromLine(line):
    """Takes unique names from a line.
    Args:
        line (str): line like: user: Claudian, tag: 933658,.
    Returns:
        line_unique_names (set): set of unique names.
    """
    line_unique_names = set()
    list_of_pairs = line.strip().split(',')
    for pair in list_of_pairs:
        if USER_SEPARATOR in pair:
            line_unique_names.add(getNameFromPair(pair))
    return line_unique_names


def getUniqueNamesFromFile(filename):
    """Takes a set of unique names.
    Args:
        filename (str): name of the file being processed.
    Returns:
        file_unique_names (set): set of unique names.
    """
    file_unique_names = set()
    with open(filename) as file:
        for line in file:
            file_unique_names.update(getUniqueNamesFromLine(line))
    return file_unique_names


if __name__ == "__main__":
    first_file_unique_names = getUniqueNamesFromFile(FIRST_INPUT_FILE)
    second_file_unique_names = getUniqueNamesFromFile(SECOND_INPUT_FILE)
    result_names = first_file_unique_names - second_file_unique_names
    print(*result_names, sep='\n')
