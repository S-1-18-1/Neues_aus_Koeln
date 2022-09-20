import os
import re
import copy
from lxml import etree as ET

# empty corpus
corpus = {}

# Regex Builder:

# Regex used for matching week_days
week_day_names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
week_day_regex = []
for regex in week_day_names:
    week_day_regex.append(re.compile(regex, re.IGNORECASE))

# Regex used for matching uninteresting sub-categories
ignore_stories = [".*Heirat.", ".*Sterbefälle.*", ".*Geburten.*"]
ignore_stories_regex = []
for regex in ignore_stories:
    ignore_stories_regex.append(re.compile(regex, re.IGNORECASE))

# Regex for matching other categories than "Neues aus Köln" or "Locales"
other_categories = ["Aus Kölns Nachbarschaft\.", "Aus dem sozialen Leben\.", "Aus dem Geschäftsverkehr\.", "Unterhaltendes\.", "Aus der Arbeiterwelt\.", 
                    "Von Nah und Fern\.", "Mitteilungen\.", "Gerichts[-=]Verhandlungen\.", "Kirchliches\.", "Gesellschafts- und Vereinsleben\.", "Standesamt\.", 
                    "Was der .* bringt\.", "Kölner Local-Anzeiger", "Kauf[=-]Gesuche\.", "Arbeits[=-]Gesuche\.",  "zu verkaufen\.", "Miet[=-]Gesuche\.", 
                    "Offene Stellen\.", "Stellen[=-]Gesuche\.", "Zur Kurzweil\.", "Aus Vororten und Umgebung\.", "Standesamt.*", "Vermischtes\.", "der Stadt Köln\.",
                    "Vermischte Nachrichten\.", "Stimmen aus dem Leserkreis\.", "Was gibt es Neues?", "Vereinsnachrichten\.", "Feuilleton.*"]
other_categories_regex = []
for regex in other_categories:
    other_categories_regex.append(re.compile(regex, re.IGNORECASE))

# Regex used for matching common two char words, inspired from https://www.wort-suchen.de/wortspiele/woerter-mit-2-buchstaben/1676242
two_char_words = ["In", "Im", "An", "Ab", "Am", "Da", "Du", "Er", "Ja", "Wo", "Zu", "Es", "Um", "Je", "Eh", "Ob", "So", "\d(\.)*"] 
two_char_regex = []
for regex in two_char_words:
    two_char_regex.append(re.compile(regex, re.IGNORECASE))


def check_sentence_end(line_content:str):
    """ checks if the end of the line is also the end of a sentence

    :param line_content: string with the content of a line
    :type line_content: str
    :return: true, if the line ends with a typical char that shows the end of an sentence, false if not
    :rtype: bool
    """
    if len(line_content.strip()) > 0 and line_content.strip()[-1] not in [".", "!", "?", "—"]:
        return True
    else: 
        return False

def add_to_corpus(file_name:str, story_counter_number:int, line_content:str):
    """adds a story to the corpus, creates an element for the date if not already there

    :param file_name: name of the file, works as key
    :type file_name: str
    :param story_counter_number: number of the story for this newspaper volume
    :type story_counter_number: int
    :param line_content: content of the line that should be added to the corpus
    :type line_content: str
    """
    try: 
        corpus[str(file_name)].update({story_counter_number : line_content})
    except KeyError:
        corpus[str(file_name)]={story_counter_number : line_content}


def build_corpus(data_path:str, max_category_length:int, max_small_category_length:int, min_line_length:int):
    """builds the corpus through extracting lines from a collection of textfiles

    :param data_path: path to the text files
    :type data_path: str
    :param max_category_length: after matching the title of a category, this param indicates for how many lines it should be searched for matching stories
    :type max_category_length: int
    :param max_small_category_length: after matching the title of a small category, this param indicates for how many lines it should be searched for matching stories
    :type max_small_category_length: int
    :param min_line_length: indicates the minimum length of a line to be added to a story, reduces the number of broken text parts
    :type min_line_length: int
    :return: the full corpus
    :rtype: dict
    """
    for root, dir, files in os.walk(data_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # create a list with lines as elements
            with open (file_path, 'r', encoding="utf-8") as f:
                lines = []
                for line in f:
                    lines.append(line)
            '''
                right_rubric is 0 if you are not in a right rubric,
                is set to the max(_small)_categoy_length when entering a right rubric and counts down with every line
            '''
            right_rubric = 0  
            '''
                story_counter is -1 by default, counts up when starting to add stories to a specific volume of the newspaper
            '''
            story_counter = -1 
            '''
                add_next is False by default, is set to True when the current story is not finished and runs over several lines
            '''
            add_next = False

            for index, current_line in enumerate(lines):
                if right_rubric > 0:
                    right_rubric -= 1   #count down
                    if any(regex.match(current_line) for regex in other_categories_regex): 
                        # start of a new (wrong) category, therefore reset the right_rubric variable
                        right_rubric = 0
                    elif len(current_line) >= min_line_length and len(current_line.split(" ")[0]) < 3 and not any(regex.match(current_line.split(" ")[0]) for regex in two_char_regex) and not any(regex.match(current_line) for regex in ignore_stories_regex): 
                        # start of a new story, indicated by 1 or 2 chars that work at dividers, details in the paper 
                        if ".—" in current_line:
                            # sometimes the stories are split by ".—", so they need to be seperated
                            substories = current_line.split(".—")
                            for substory in substories:
                                story_counter +=1
                                add_to_corpus(file_name, story_counter, substory)              
                        else:
                            story_counter +=1
                            # delete the divider string at the beginning of the sentence and add the line to the corpus
                            add_to_corpus(file_name, story_counter, current_line.replace(current_line.split(" ")[0],"",1))

                        # if the line is not the end of a sentence, add_next is set to True so the next line can be added to the current story
                        add_next = check_sentence_end(current_line)

                    elif add_next==True and len(current_line) >= min_line_length:
                        # with add_next==True the line doesn't need to match the criteria to be an independent story and gets added to the last line
                        new_s = corpus[str(file_name)][story_counter] + current_line
                        corpus[str(file_name)][story_counter] = new_s
                        add_next = check_sentence_end(current_line)

                # these regex match if there is the start of the category "Locales" or "Neues aus Köln", then the right_rubric is set to the max_categoy_length
                elif re.match("\w*[TLk][oes][ce]a[lt]es($|\.)", current_line):
                    right_rubric = max_category_length
                elif re.match("aus [RKtA][öo][li](n|\.)", current_line) and re.match("[TNLn]eues", lines[index-1]):                
                    right_rubric = max_category_length
                elif re.match("(aus [RKtA][öo][li]n)(\.)?$", current_line) and ("Anzeiger" in lines[index-1] or any(name in lines[index-1] for name in week_day_names) or "Seite" in lines[index-1] or len(lines[index-1])<=7) and len(lines[index-1])<70:
                    right_rubric = max_category_length
                # this regex matches the smaller categories for news from a specific district (e.g. "Aus Köln-Ehrenfeld")
                elif re.match("[Aa]us [RKtA][öo][li]n-", current_line):
                    right_rubric = max_small_category_length

    return corpus


def save_corpus(corpus, template, output_name):
    parser = ET.XMLParser(remove_blank_text=True)

    #clean old files
    for file in os.scandir(output_name):
        os.remove(file.path)
    # build a xml tree structure for each newspaper volume 
    for ausgabe, stories_corpus in corpus.items():
        tree = ET.parse(template, parser)

        # add the metadata
        metadata = ausgabe.split("_")
        tree.find(".//year").text=metadata[0]
        tree.find(".//month").text=metadata[1]
        tree.find(".//day").text=metadata[2]
        tree.find(".//ID").text=metadata[3].split(".")[0]
        
        story_xml = tree.find(".//story")  
        count=len(stories_corpus)
        # for some volumes no stories were found 
        if count != 0: 
             # create as many story elements in the tree as there are stories in the corpus dict
            for i in range(0, count):
                if i > 0:
                    story_xml.addnext(copy.deepcopy(story_xml))
            all_stories=tree.findall(".//story")

            # fill in the story elements with the (cleaned up) stories from the corpus dict and the key
            for key, story_counter in stories_corpus.items():
                text_to_write = story_counter.replace("\n"," ").removeprefix(' ')
                all_stories[key].find(".//number").text=str(key)
                all_stories[key].find(".//text").text=text_to_write

        # write the tree as xml files into the output folder
        tree.write("%s/%s.xml" %(output_name, metadata[3].split(".")[0]), pretty_print=True, encoding='utf-8')        

if __name__ == '__main__':
    stories = build_corpus("data", 40, 5, 40)
    save_corpus(stories, "resources/template.xml", "test")
    