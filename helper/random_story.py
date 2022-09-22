from random import randint
from lxml import etree as ET
import os

def get_random_stories(input, count, mode, output ="", already_annotated = True):
    """chooses random stories

    :param input: path to the corpus
    :type input: str
    :param count: count of random stories
    :type count: int
    :param mode: "print" for printing in output file, "return" for returning the list of random stories
    :type mode: str
    :param output: only needed for mode "print", path to the output file
    :type output: str
    :param already_annotated: True, if already annotated stories should be collected too
    :type output: bool
    :return: the list with random stories
    :rtype: list/none
    """

    stories = []
    rand_stories = []

    parser = ET.XMLParser(remove_blank_text=True)

    for root, dir, files in os.walk(input):
        for file_name in files:
            full_path = os.path.join(input, file_name)
            tree = ET.parse(full_path, parser)
            # select only stories with none empty texts
            if already_annotated == True:
                for story in tree.xpath(".//story[not(. = '')]"):
                    stories.append([story, file_name])
            elif already_annotated == False:
                for story in tree.xpath(".//story[not(. = '') and //exceptionalNormal[not(text())]]"):
                    stories.append([story, file_name])
    i = 0 
    while i < count:
        get_story = randint(0,len(stories))
        rand_stories.append(stories[get_story])
        i+=1
    if mode == "print":
        with open(output, "w") as f:
            for story in rand_stories:
                f.write( "%s: %s \n" %(story[1], story[0].find(".//text").text))
    elif mode =="return":
        return rand_stories


if __name__ == '__main__':
    get_random_stories("corpus", 100, mode="print", output="output/randomstories.txt", already_annotated = True)