# regeXML
A Python library to support parsing regeXML expressions.

Tired of trying to wrap your tiny brain around difficult-to-understand regular expressions like `<[a-z]+>.*</[a-z]+>`?

What if you had a human-readable method of expressing your regular expression?
```
<?xml version="1.0"?>
<expression type=regular" dialect="posix" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="regexml.xsd">
 <character encoding="utf-8" locale="en-US"><![CDATA[<]]></character>
 <repeat type="oneormore">
  <characterset>
   <startingcharacter encoding="utf-8" locale="en-US">a</startingcharacter>
   <endingcharacter encoding="utf-8" locale="en-US">z</endingcharacter>
  </characterset>
 </repeat>
 <character encoding="utf-8" locale="en-US"><![CDATA[>]]></character>
 <repeat type="zeroormore">
  <wildcard></wildcard>
 </repeat>
 <character encoding="utf-8" locale="en-US"><![CDATA[<]]></character>
 <character encoding="utf-8" locale="en-US">/</character>
 <repeat type="oneormore">
  <characterset>
   <startingcharacter encoding="utf-8" locale="en-US">a</startingcharacter>
   <endingcharacter encoding="utf-8" locale="en-US">z</endingcharacter>
  </characterset>
 </repeat>
 <character encoding="utf-8" locale="en-US"><![CDATA[>]]></character>
</expression>
```

Obviously, this example is much easier to read in regeXML format. It has the following additional benefits:
* Easier for a computer to read, parse, serialize and transmit.
* Is more extensible than standard regex syntax.
* Can be validated againt a schema to ensure correctness.
* Can be easily and safely embedded into other XML-based documents for composability.
