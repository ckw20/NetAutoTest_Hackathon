"""
Purify RFCs to remove unnecessary information, such as headers, footers, and page numbers.
"""

import re
import os
import argparse

import logging

logger = logging.getLogger(__name__)


def purify_rfc(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f_in:
        content = f_in.read().strip()
    # pattern = r'\n{3}Moy*.*Standards Track.*\n.\nRFC.*1998\n{3}'    # Match header line, page break line, footer line, and surrounding blank lines (control the number of blank lines deleted to ensure no loss of paragraph information)
    pattern = r'\n{3}.*Standards Track.*\n.\nRFC.*\n{3}'    # Match header line, page break line, footer line, and surrounding blank lines (control the number of blank lines deleted to ensure no loss of paragraph information)
    pattern2 = r'\n{3}.*Standards Track.*\n.\n.*RFC.*\n{3}'    # Match header line, page break line, footer line, and surrounding blank lines (control the number of blank lines deleted to ensure no loss of paragraph information)
    # Replace the above content with a newline
    purified_text = re.sub(pattern, '', content, flags=re.MULTILINE)
    purified_text = re.sub(pattern2, '', purified_text, flags=re.MULTILINE)

    # curr_blanks = 0
    # purified_text_simpled = []
    # # Replace consecutive blank lines exceeding 3 in purified_text with 2 blank lines
    # for line in purified_text.split('\n'):
    #     if line.strip() == '':
    #         curr_blanks += 1
    #     else:
    #         for b in range(min(curr_blanks, 3)):
    #             purified_text_simpled.append('\n')
    #         curr_blanks = 0
    #         purified_text_simpled.append(line)

    if not output_file_path:
        output_file_path = input_file_path.replace('.txt', '_purified.txt')
    with open(output_file_path, 'w', encoding='utf-8') as f_out:
        f_out.writelines(purified_text)

def purify_tcp793(input_file, output_file, pre=1, post=5):
    # 包含  的前1行和后5行过滤掉，其他都保留
    with open(input_file, 'r', encoding='utf-8') as f_in:
        content = f_in.readlines()
    purified_text = []

    i = 0
    while i < len(content):
        if i + pre < len(content):
            if '' in content[i+1]:
                i += (pre + 1 + post)
                continue
        purified_text.append(content[i])
        i += 1

    curr_blanks = 0
    purified_text_simpled = []
    # 把 purified_text 中超过3行的连续空行都换成2行空行
    for line in purified_text:
        if line.strip() == '':
            curr_blanks += 1
        else:
            for b in range(min(curr_blanks, 3)):
                purified_text_simpled.append('\n')
            curr_blanks = 0
            purified_text_simpled.append(line)

    if not output_file:
        output_file = input_file.replace('.txt', '_purified.txt')
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(purified_text_simpled)
    logger.info(f"Purified RFC saved to {output_file}")



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Purify RFCs to remove unnecessary information.")
    parser.add_argument("-i", "--input_file", type=str, default=None, help="The input RFC file.")
    parser.add_argument("-o", "--output_file", type=str, default=None, help="The output file.")
    parser.add_argument("--pre", type=int, default=1, help="The number of lines to keep before the page break.")
    parser.add_argument("--post", type=int, default=5, help="The number of lines to keep after the page break.")
    parser.add_argument("--style", type=str, default="90", choices=["80", "90"], help="The style of purification.")
    args = parser.parse_args()
    if args.style == "80":
        purify_tcp793(args.input_file, args.output_file, args.pre, args.post)
    else:
        purify_rfc(args.input_file, args.output_file)