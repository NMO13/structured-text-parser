from os import listdir
from os.path import isfile, join
from src.vector_generation import similarity_score, create_occurrence_list
st_path = "./st/"
onlyfiles = [join(st_path, f) for f in listdir(st_path) if isfile(join(st_path, f))]
print(onlyfiles)

from src.ast_builder import ASTBuilder
creator = ASTBuilder()
for file in onlyfiles:
    print("Parsing file {}".format(file))
    with open(file) as f:
        tokens = creator.parse(f.read())
        similarity_score(create_occurrence_list(tokens), create_occurrence_list(tokens))


