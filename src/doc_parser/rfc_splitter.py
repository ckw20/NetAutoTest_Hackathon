import re
import os
import argparse

import logging

logger = logging.getLogger(__name__)

class RFCNode():
    """
    RFC node class: includes sectionID, title, content, parent node, and child nodes. Represents the RFC file as a node tree.
    """
    def __init__(self, sectionID, title, parent, content=None):
        self.sectionID = sectionID  # Only save the current sectionID, the full ID is composed of the parent's ID and the current sectionID
        self.title = title
        self.content = content
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def get_curr_level(self):
        curr_level = [self.sectionID]
        parent = self.parent
        while parent:
            curr_level.append(parent.sectionID)
            parent = parent.parent
        curr_level.reverse()
        return curr_level[1:]

    def get_full_id(self):
        return '.'.join(self.get_curr_level())
    
    def get_full_page(self):
        # logger.debug(f"Getting full page: {self.get_full_id()}")    
        # logger.debug(f"{self.title}")
        # logger.debug(f"{self.content}")
        return self.get_full_id() + ' ' + self.title + '\n' + self.content.strip()
    
    def __str__(self):
        full_level = '.'.join(self.get_curr_level())
        return f"{full_level} {self.title}"
    
    def print_subtree(self):
        logger.info(self)
        # for child in self.children:
        #     logger.debug(child.sectionID)
        for child in self.children:
            child.print_subtree()

    def print_subtree_with_content(self):
        logger.info(self)
        if self.content:
            logger.info(self.content)
        for child in self.children:
            child.print_subtree_with_content()

    def get_subtree_content_table(self):
        """Get the content table of the subtree, including node ID, title, and content.

        Iterate through the child nodes of the current node, extract the ID, title, and content of each child node, and return them as a list.

        Returns:
            list[tuple]: The content table of the subtree, each element is a tuple containing the node ID, title, and content.
        """
        content_table = []
        for child in self.children:
            content_table.append((child.get_full_id(), child.title))
            content_table.extend(child.get_subtree_content_table())
        return content_table


    def get_subnode_by_id(self, id):
        """Find the corresponding child node based on the hierarchical ID list and return its content.

        Starting from the current node, traverse the id_list to find the matching child node.
        If the target node is found, return its content; otherwise, return None.

        Args:
            id_list (list[str]): The hierarchical ID list, e.g., 1.1.1.

        Returns:
            RFCNode: The target node.
        """
        logger.debug(f"Getting subnode by ID: {id}")
        id_list = [c for c in id.split('.') if c]
        logger.info(f"Getting subnode by ID: {id_list}")
        current_node = self
        for section_id in id_list:
            found_child = False
            for child in current_node.children:
                if child.sectionID == section_id:
                    current_node = child
                    found_child = True
                    break
            if not found_child:
                return None
        return current_node
    

def purify_hierarchical_id(id_str):
    id_str = id_str.strip()
    if id_str[-1] == '.':
        id_str = id_str[:-1]
    return id_str

def is_hierarchical_id(id_str):
    # Regular expression matching hierarchical ID
    # 1. Single letter or number, e.g., "A" or "1"
    # 2. Combination of numbers and dots, e.g., "16.1.1" or "16.1.1."
    pattern = r'^([A-Za-z]|\d+)(\.\d+)*\.?$'
    
    # Use regular expression for matching
    if re.match(pattern, id_str):
        return True
    else:
        return False


def add_node(id, title, rfc_root):
    """ For RFC node items parsed, add them to the tree at the appropriate position (build tree) """
    is_hierarchical = is_hierarchical_id(id)
    logger.debug(f"|{id}| |{title}|")
    
    if is_hierarchical:
        id_list = [c for c in id.split('.')]
        curr_level = 0
        curr_node = rfc_root
        
        # Find parent node
        while curr_level < len(id_list) - 1:
            found_child = False
            for child in curr_node.children:
                if child.sectionID == id_list[curr_level]:
                    curr_node = child
                    curr_level += 1
                    found_child = True
                    break
            if not found_child:
                # If parent node does not exist, create an empty node first
                new_node = RFCNode(id_list[curr_level], "", curr_node)
                curr_node.add_child(new_node)
                curr_node = new_node
                curr_level += 1
        
        # Add current node
        new_node = RFCNode(id_list[-1], title, curr_node)
        curr_node.add_child(new_node)
        logger.info(f'Add node at tree: {new_node} with parent {curr_node}')
        
    else:
        id = f"{id} {title}" if title else id
        id = id.lower()
        title = id
        new_node = RFCNode(id, title, rfc_root)
        rfc_root.add_child(new_node)
    


# def update_node_content(id, content, rfc_root):
#     """ For RFC content parsed, add it to the appropriate node in the tree (fill node) """
#     logger.info(f"Update node content: {id}")
#     pass

def update_node_content(id, content, rfc_root):
    """ For RFC content parsed, add it to the appropriate node in the tree (fill node) """
    id = purify_hierarchical_id(id)
    logger.debug(f"Update node content: {id}")
    
    # If id is hierarchical, we need to find the corresponding node
    if is_hierarchical_id(id):
        id_list = [c for c in id.split('.')]
        curr_level = 0
        curr_node = rfc_root
        
        # Find target node
        while curr_level < len(id_list):
            found_child = False
            for child in curr_node.children:
                if child.sectionID == id_list[curr_level]:
                    curr_node = child
                    curr_level += 1
                    found_child = True
                    break
            if not found_child:
                # If node does not exist, it means there is an error in the parsing process, record the error and return
                logger.error(f"Node with ID {id} not found in the tree.")
                return
        
        # After finding the node, update its content
        curr_node.set_content(content)
        logger.info(f'Updated node content: {curr_node}')
    
    else:
        # If id is not hierarchical, process it as a child node of the root node directly
        for child in rfc_root.children:
            if child.sectionID == id:
                child.set_content(content)
                logger.info(f'Updated node content: {child.sectionID}')
                return
        
        # If node not found, record error
        logger.error(f"Node with ID {id} not found in the tree.")

contents = []  # Directory, initially empty; filled with tuple(id, title) after parsing Table of Contents
contents_found = []

def build_rfc_tree(file_path) -> RFCNode:
    """ Parse RFC file and build a tree structure """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    rfc_headers = ['Abstract', 'Status of This Memo', 'Copyright Notice', 'Table of Contents', '1.  Introduction', 'PREFACE']  # '1.  Introduction' is used to determine the end of the table of contents
    rfc_headers = [header.lower() for header in rfc_headers]
    metadata = {}   # Store metadata, i.e., the content of the above headers except Introduction
    curr_title, curr_id = 'title_and_above', '1'
    curr_content = ''
    is_contents = False
    rfc_root = None
    for line in lines:
        # if not line.strip():  # Blank line, should not be skipped as it represents a paragraph
        #     continue

        if is_contents:    # Table of Contents has been parsed, start parsing the main text
            logger.debug(line)
            line_list = [c for c in line.strip().split(' ') if c]
            if not line_list:
                curr_content += line
                continue
            temp_id, temp_title = line_list[0], " ".join(line_list[1:])
            id_title = f"{temp_id} {temp_title}".strip().lower()
            if is_hierarchical_id(temp_id):         # Title with id
                logger.debug(f"Find hierarchical id: |{temp_id}| |{temp_title}|")
                content_tuple = (purify_hierarchical_id(temp_id), temp_title.lower())
                logger.debug(content_tuple)
                if content_tuple in contents:
                    contents_found.append(content_tuple)
                    logger.debug(f"Find content: {temp_id} {temp_title}")
                    update_node_content(curr_id, curr_content, rfc_root)
                    curr_title = line.strip()
                    curr_id = temp_id
                    curr_content = ''
                    continue
            elif (id_title, id_title) in contents:  # Title without id
                logger.debug(f"Find content (w/o id): {id_title}")
                contents_found.append((id_title, id_title))
                update_node_content(curr_id, curr_content, rfc_root)
                curr_title = line.strip()
                curr_id = id_title.lower()
                curr_content = ''
                continue
            
            curr_content += line    # Check if strip is needed
                    
                
        else:           # Table of Contents not parsed, continue parsing metadata
            if line.strip().lower() in rfc_headers:
                metadata[curr_title] = curr_content
                if curr_title == 'title_and_above':
                    title_and_above = [c for c in curr_content.split('\n') if c]
                    metadata['title'] = title_and_above[-1].strip()
                    rfc_root = RFCNode('0', metadata['title'], None, "")
                if curr_title.lower() == 'table of contents':
                    is_contents = True      # Table of Contents parsed
                curr_title = line.strip()
                curr_content = ''
            else:
                curr_content += line
                if curr_title.lower() == 'table of contents':  # Parse Table of Contents
                    line = line.strip()
                    if not line:
                        continue
                    line_list = [c for c in line.split(' ')[:-1] if c]
                    if '.' in line_list[-1]:
                        line_list = line_list[:-1]
                    add_node(line_list[0], ' '.join(line_list[1:]), rfc_root)
                    id, title = line_list[0], ' '.join(line_list[1:]).lower()
                    if is_hierarchical_id(id):  # id followed by two spaces, not normal spaces
                        contents.append((purify_hierarchical_id(id), title))
                    else:
                        id_title = f"{id} {title}".strip().lower()
                        contents.append((id_title, id_title))

                    
    # rfc_root.print_subtree()
    # logger.debug(contents)
    # logger.debug(len(contents))
    contents_left = []
    for content in contents:
        if content not in contents_found:
            contents_left.append(content)
    # logger.debug(contents_left)
    # logger.debug("##### TREE WITH CONTENT #####")
    # rfc_root.print_subtree_with_content()
    return rfc_root


if __name__ == '__main__':
    # # Test case
    # test_ids = ["A", "16.1.1", "1", "1.1.1.", "security", "16.1.1.1."]
    # for id_str in test_ids:
    #     print(f"{id_str}: {is_hierarchical_id(id_str)}")
    # exit()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)
    logger.info("Build RFC tree.")

    parser = argparse.ArgumentParser(description="Build RFC tree.")
    parser.add_argument("-i", "--input_file", type=str, default=None, help="The input RFC file.")
    args = parser.parse_args()
    file_path = args.input_file
    rfc_root = build_rfc_tree(file_path)

    rfc_root.print_subtree()

    sections_to_read = ['9.5', 'A.3.2', '4.5', 'A.2', '10.5']
    for id in sections_to_read:
        rfc_node = rfc_root.get_subnode_by_id(id)
        if rfc_node:
            logger.info(rfc_node.get_full_id())
            logger.info(rfc_node.title)
            logger.info(rfc_node.content) 
        else:
            logger.error(f"Node {id} not found.")
    # rfc_node = rfc_root.get_subnode_by_id("9.5")
    # if rfc_node:
    #     logger.info(rfc_node.get_full_id())
    #     logger.info(rfc_node.title)
    #     logger.info(rfc_node.content) 
    # else:
    #     logger.error("Node not found.")


# python rfc_splitter.py -i /root/NetAutoTest/data/raw_documents/rfc2328_cleaned.txt > rfc.log 2>&1