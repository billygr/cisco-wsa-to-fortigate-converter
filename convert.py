# Cisco WSA to FortiGate converter
# wga_config element contains the actual needed configuration
# Custom categories are in the prox_acl_custom_category_abbrev element, prox_acl_custom_category_server and prox_acl_custom_category_regex_list

import sys
from lxml import etree
from collections import Counter
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="myFile", help="Open Cisco WSA xml file")
args = parser.parse_args()
if not any(vars(args).values()):
    parser.print_help()
    sys.exit()
    
myFile = args.myFile

# Parse the Cisco XML file
root = etree.parse(myFile)
tree = etree.parse(myFile)

categories_with_servers=0
# Iterate through each category and its servers/fqdn
for category in tree.xpath("//prox_acl_custom_category_abbrev"):
    category_name = category.text
    servers = category.xpath("following-sibling::prox_acl_custom_category_servers/prox_acl_custom_category_server")

    # Catch categories with empty regex
    if not len(category_name) == 0:
        categories_with_servers=categories_with_servers+1
        print(f"Category: {category_name}")
    for server in servers:
        print(f"  Server: {server.text}")

categories_with_regex=0
print("Regular Expection Categories and List")
# Iterate through each category and its regex_list
for category in tree.xpath("//prox_acl_custom_category_abbrev"):
    category_name = category.text
    category_regex = category.xpath("following-sibling::prox_acl_custom_category_regex_list/prox_acl_custom_category_regex")
    
    # Catch categories with empty regex
    if not len(category_regex) == 0:
        categories_with_regex=categories_with_regex+1
        print(f"Category: {category_name}")
    for regex in category_regex:
        print(f"  RegExp URL: {regex.text}")

print()
print("Summary")
print(f" Categories            : {categories_with_servers}")      
print(f" Categories with regex : {categories_with_regex}")