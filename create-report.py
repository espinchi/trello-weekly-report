#!/usr/bin/env python
import argparse
import json
from pprint import pprint

class TrelloReport():
    def display_all_cards(self, fileName):
	# Load the JSON file           
        fileHandler = open(fileName)
        data = json.load(fileHandler)
        fileHandler.close()
        
        for l in sorted(data['lists'], key=lambda l: l['pos']):
            cards = list(filter(lambda c: c['idList'] == l['id'], data['cards']))
            print(l['name'])
            self._print_cards(cards)

    def _print_cards(self, cards):
        if cards:
                for c in cards:
                    print(" %s" % c['name'])

def main():
    args = parser.parse_args()
    trelloReport = TrelloReport()
    trelloReport.display_all_cards(args.fileName)

# use http://tools.arantius.com/tabifier to tabify the original json
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Reads a trello JSON dump.')
    parser.add_argument('-f', '--fileName', default='sample.json',
        help='Name of the JSON file')
    main()
