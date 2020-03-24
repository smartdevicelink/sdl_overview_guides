# RPC Spec Generator

The RPC Spec repository contains a parsing script that is used by the following platform's generator implementations:

- SDL Core
- SDL IOS
- SDL Java Suite
- SDL JavaScript

The RPC Spec repository is imported as a git submodule into each of the previously mentioned platforms. The RPC Spec parser reads the MOBILE_API.xml which is the specification for all RPC messages communicated between a proxy platform and SDL Core. Each platform contains a code generator for creating RPC classes and files. These generators greatly reduce the amount of effort for adding new RPC messages.

## Using the RPC Spec Generator

All developers who are using an SDL platform should run these commands in the SDL platform source directory to ensure the latest RPC spec and parser is being used in their builds:

```
git submodule init
git submodule update
```

Using the parser requires a minimum python version, 3.5. The rest of the dependencies for the generators can be installed via:

```
python3 -m pip install -r InterfaceParser/requirements.txt
```

Each platform has their own generator implementation but the instructions for generating their respective RPC code is the same. Refer to the following command line options for running a SDL platform generator script:

```
Mobile API Spec Generator

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         print the version and exit
  -xml SOURCE_XML, --source-xml SOURCE_XML, --input-file SOURCE_XML
                        should point to MOBILE_API.xml
  -xsd SOURCE_XSD, --source-xsd SOURCE_XSD
  -d OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        define the place where the generated output_directory
                        should be placed
  -r REGEX_PATTERN, --regex-pattern REGEX_PATTERN
                        only elements matched with defined regex pattern will
                        be parsed and generated
  --verbose             display additional details like logs etc
  -e, --enums           only specified elements will be generated, if present
  -s, --structs         only specified elements will be generated, if present
  -m, -f, --functions   only specified elements will be generated, if present
  -y, --overwrite       force overwriting of existing files in
                        output_directory file, ignore confirmation message
  -n, --skip            skip overwriting of existing files in output_directory
                        file, ignore confirmation message
```

## RPC Spec Structure

This section describes the structure of the `MOBILE_API.xml` and the elements and attributes that are required for code generation. Refer to the `MOBILE_API.xsd` for the full schema definition.

### interface
The root element is the `<interface>` tag. The `<interface>` tag contains any number of `<enum>`, `<struct>` and `<function>` tags.

Example:
```xml
<interface name="string" version="string" minVersion="string" date="string">
  <!--Zero or more repetitions:-->
  <enum/>
  <!--Zero or more repetitions:-->
  <struct/>
  <!--Zero or more repetitions:-->
  <function/>
</interface>
```

### enum
The `<enum>` element contains any number of `<element>` that represents a set of possible values. The `<enum>` has a required `name` attribute.

Example:
```xml
<enum deprecated="boolean" internal_scope="string" name="string" platform="string" since="string" until="string">
  <!--Zero or more repetitions:-->
  <description>string</description>
  <!--Zero or more repetitions:-->
 <element hexvalue="string" internal_name="string" name="string" rootscreen="boolean" since="string" value="integer">
    <!--Zero or more repetitions:-->
    <description>string</description>
    <!--Zero or more repetitions:-->
    <warning>string</warning>
  </element>
  <!--Optional:-->
  <history>
    <enum/>
  </history>
</enum>
```

SDL has two different enum types: `string` and `integer`. If `"hexvalue"` or `"value"` attribute exists, the enum type is `integer`, otherwise the enum type is `string`.

The `<element>` has a required `"name"` attribute. For `string` enums, the value of `"name"` attribute will be one of the possible values of the particular `<enum>`.  For `integer` enums, the value of `"value"` attribute will be one of the possible values. The `"hexvalue"` is just a hexadecimal representation of the `"value"` attribute and either hexvalue or value can be used.

`<element>` could also have an `"internal_name"` attribute. This attribute is not used in communication with SDL Core, but it describes the `<element>` developer facing elemtn value. For example refer to the `HMILevel` enum:

```xml
    <enum name="HMILevel" since="1.0">
        <description>Enumeration that describes current levels of HMI.</description>
        <element name="FULL" internal_name="HMI_FULL" />
        <element name="LIMITED" internal_name="HMI_LIMITED" />
        <element name="BACKGROUND" internal_name="HMI_BACKGROUND" />
        <element name="NONE" internal_name="HMI_NONE" />
    </enum>
```

The HMILevel communicated to the proxies from SDL Core will use the `name` value (`FULL`, `NONE`, etc). However the `HMILevel` enum usage in SDL Core's code will use the `internal_name` value (`HMI_FULL`, `HMI_NONE`, etc).

### struct
`<struct>` is a complex data type. `<struct>` contains any number of `<param>`. The `<struct>` has a required `"name"` attribute.

Example:
```xml
<struct deprecated="boolean" name="string" since="string" until="string">
  <!--Optional:-->
  <history>
    <struct/>
  </history>
  <!--Zero or more repetitions:-->
  <description>string</description>
  <!--Zero or more repetitions:-->
  <param array="boolean" defvalue="integer|decimal|boolean|string" deprecated="boolean" mandatory="boolean" maxlength="integer" maxsize="integer" maxvalue="decimal" minlength="integer" minsize="integer" minvalue="decimal" name="string" since="string" type="string" until="string">
    <!--Zero or more repetitions:-->
    <description>string</description>
    <!--Optional:-->
    <history>
      <param/>
    </history>
  </param>
</struct>
```

Each `<param>` requires `"name"`, `"type"` and `"mandatory"` attributes. The `"type"` attribute value should be one of `"Boolean"`, `"Float"`, `"Integer"`, `"String"` or one of the `<enum>`, `<struct>` names specified in the Mobile API.

`<param>` could have `"array"` attribute to represent an array of values or objects of the described type. Attributes `"maxsize"` and `"minsize"` provide additional restrictions to an array.

Numeric types can be restricted using `"minvalue"` and `"maxvalue"`. 

The `"defvalue"` attribute contains default value with different type, depends on `<param>` type, note: this attribute is not allowed for `<struct>` type.

### function
The `<function>` element represents a specific RPC and message type of the Mobile API. It contains any number of `<param>`. The `<function>` has a required `"name"`, `"messagetype"`, `"functionID"` attributes.

Example:
```xml

<function deprecated="boolean" functionID="string" messagetype="string" name="string" since="string" until="string">
  <!--Optional:-->
  <history>
    <function/>
  </history>
  <!--Zero or more repetitions:-->
  <description>string</description>
  <!--Zero or more repetitions:-->
  <param array="boolean" defvalue="integer|decimal|boolean|string" deprecated="boolean" mandatory="boolean" maxlength="integer" maxsize="integer" maxvalue="decimal" minlength="integer" minsize="integer" minvalue="decimal" name="string" platform="string" since="string" type="string" until="string">
    <!--Zero or more repetitions:-->
    <description>string</description>
    <!--Optional:-->
    <history>
      <param/>
    </history>
    <!--Zero or more repetitions:-->
    <todo>string</todo>
    <!--Zero or more repetitions:-->
    <element name="string">
      <!--Optional:-->
      <description>string</description>
    </element>
  </param>
</function>
```
The `"messagetype"` attribute value should be either `"request"`, `"response"`, or `"notification"`. 

The `"functionID"` attribute value should match the `"name`" attribute of one `<element>` from the `"FunctionID"` `<enum>`.

Just like `<param>` elements in `<struct>`, each `<param>` has required `"name"`, `"type"`, and `"mandatory"` attributes. The `"type"` attribute value should be one of `"Boolean"`, `"Float"`, `"Integer"`, `"String"` or the one of `<enum>`, `<struct>` name exists in XML.

`<param>` could have `"array"` attribute which means the param represents array of described types. Attributes `"max*"` and `"min*"` provide additional restrictions. 

The `"defvalue"` attribute contains default value with different type, depends on `<param>` type, note: this attribute is not allowed for `<struct>` type.

### RPC Spec Versioning
Any element, param, function, or struct can use following xml attributes to express what RPC spec version an item was added, removed, deprecated, or changed.

- `since` - The first version a change was made to an item (added, deprecated, removed)
- `until` - Used with the `since` attribute to determine the range of versions a modification applied to an item was relevant.
- `removed` - A boolean value to describe that an item has been removed from the RPC Spec. Should only be specified if `removed=true`.
- `deprecated` - A boolean value to describe that an item has been deprecated from the RPC Spec. Should only be specified if `deprecated=true`.
- `history` - An array of history items that contains all previous RPC Spec definitions for an item. The most recent version is not included in this history array.
