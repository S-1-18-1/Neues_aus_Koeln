from helper.random_story import get_random_stories
from lxml import etree as ET
import os

parser = ET.XMLParser(remove_blank_text=True)


def get_count_of_existing_annotations(input_path):
    """counts the already existing annotations

    :param input_path: path to the corpus folder
    :type input_path: str
    :return: count of existing annotations
    :rtype: int
    """
    count=0
    for root, dir, files in os.walk(input_path):
        for file_name in files:
            full_path = os.path.join(input_path, file_name)
            tree = ET.parse(full_path, parser)
            count += tree.xpath("count(//exceptionalNormal[text()])")
    return count

def console_print(text):
    """manages the console out- and input

    :param text: Text to be displayed
    :type text: str
    :return: user input
    :rtype: str
    """
    print("%s \nExceptional Normal? [y/n/exit] " %text)
    user_answer = input().lower()
    if user_answer!="y" and user_answer!="n" and user_answer!="exit": 
        print("%s is not a valid value. Please choose between 'y' or 'n' or 'exit'" %user_answer)
        console_print(text)
    return user_answer


def annotate(input_path, story, log):
    """calls functions to annotate the story in the console and saves the annotation in the xml file

    :param input_path: path to the corpus
    :type input_path: str
    :param story: list with [lxml.etree._Element, str]
    :type story: list
    :param log: path for the logfile
    :type log: str
    :return: False, if the user inputs "exit"
    :rtype: bool/none
    """

    # get the original xml tree
    full_path = os.path.join(input_path, story[1])
    tree = ET.parse(full_path, parser)

    user_answer = console_print(story[0].find(".//text").text)
    if user_answer == "exit":
        # break condition
        return False
    else: 
        number = story[0].find(".//number").text

        # write the annotation result in the original xml
        tree.xpath('.//story[number="%s"]' %number)[0].find("./exceptionalNormal").text = user_answer
        tree.write("%s" %full_path, pretty_print=True, encoding='utf-8')  

        #log entry   
        with open(log, "a") as f:
            f.write("Added annotation for story number %s in %s \n" %(number, story[1]))   

    
if __name__ == '__main__':

    # paths
    input_path = "corpus"
    log = "output/annotation_log.txt"

    # how many annotations should be made
    desired_annotation_count = 300
    existing_annotation_count = get_count_of_existing_annotations(input_path)
    count= int(desired_annotation_count - existing_annotation_count)

    # get as many random stories as needed for the remaining files to annotate
    stories = get_random_stories(input_path, count, "return", already_annotated=False)
    for story in stories:
        existing_annotation_count = get_count_of_existing_annotations(input_path)
        count= int(desired_annotation_count - existing_annotation_count)
        print ("Remaining annotations: %s/%s" %(count, desired_annotation_count))
        if annotate(input_path, story, log) == False:
            break
    #if s
