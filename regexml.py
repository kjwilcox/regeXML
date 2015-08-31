import re
import xml.etree.ElementTree


_example = '''<?xml version="1.0" ?>
<expression type="regular" dialect="posix"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:noNamespaceSchemaLocation="regexml.xsd">
 <character encoding="utf-8" locale="en-US"><![CDATA[<]]></character>
 <repeat type="oneormore">
  <characterset>
   <character encoding="utf-8" locale="en-US">a</character>
   <character encoding="utf-8" locale="en-US">z</character>
  </characterset>
 </repeat>
 <character encoding="utf-8" locale="en-US"><![CDATA[>]]></character>
 <repeat type="zeroormore">
  <wildcard />
 </repeat>
 <character encoding="utf-8" locale="en-US"><![CDATA[<]]></character>
 <character encoding="utf-8" locale="en-US">/</character>
 <repeat type="oneormore">
  <characterset>
   <character encoding="utf-8" locale="en-US">a</character>
   <character encoding="utf-8" locale="en-US">z</character>
  </characterset>
 </repeat>
 <character encoding="utf-8" locale="en-US"><![CDATA[>]]></character>
</expression>
'''


_REPEAT_TYPE_TO_CHAR = {
    'oneormore': '+',
    'zeroormore': '*',
}


def emit_node(node):
    tag = node.tag

    if tag == 'expression':
        return ''.join(emit_node(child) for child in node)

    if tag == 'character':
        return node.text  #TODO: escape meta chars

    if tag == 'characterset':
        return '[' + emit_node(node[0]) + '-' + emit_node(node[1]) + ']'  #TODO: support more advanced ranges

    if tag == 'repeat':
        return ''.join(emit_node(child) for child in node) + _REPEAT_TYPE_TO_CHAR[node.attrib['type']]

    if tag == 'wildcard':
        return '.'

    return ''


def re_from_xml(xml_str):
    parse_tree = xml.etree.ElementTree.fromstring(xml_str)
    regex_string = emit_node(parse_tree)
    return re.compile(regex_string)  #TODO: return matches in XML


def main():
    print(re_from_xml(_example))


if __name__ == "__main__":
    main()
