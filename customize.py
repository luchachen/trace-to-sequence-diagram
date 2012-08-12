"""
.. automodule:: config
   :platform: Windows
   :synopsis: Customize the regular expressions that map to different elements
              of the sequence diagram.

.. moduleauthor:: EventHelix.com Inc.

"""
from collections import OrderedDict


# The trace messages follow this high level format. The current regular expression
# assumes that all traces are of the format:
#
# [time][module.component][file]type body
#
# time:         The trace begins with time information in square brackets
#
# module:       Higher level entity that is generating the trace. Typically, modules
#               would contain components (see the next item).
#
# component:    Entity contained in the module that is generating this trace. Typically, a
#               group of classes that work together would be treated as a component.
#               Module and component level information will be used to generate higher
#               level diagrams that provide an overview of the feature, without going
#               down to the class level.
#
# file:         The next square bracket contains filename, line number information.
#
# type:         Defines the type of a trace. The type here is used to determine the
#               mapping to an FDL statement. Refer to the traceMapper dictionary in
#               fdl.py. This file maps the type to the a function that will handle
#               the parsing of the body.
#
# body:         This is the text following the type statement. Parsing of this text
#               depends upon the type of the trace. This file contains the regular
#               expression definitions for parsing of the body for different
#               trace types.

traceRegex = '\[(?P<time>.*)\]\s*\[(?P<module>.*)\.(?P<component>.*)\]\[(?P<file>.*)\]\s*(?P<type>\S+)\s+(?P<body>.*)'


# Add messages that need to be bookmarked in the PDF file. This is useful
# as it lets to quickly navigate through the sequence diagram output of
# a trace. PDF quick navigation bookmarks will be added whenever the messages
# listed below are seen in the trace message.
bookmarks = frozenset({
    'RandomAccessMessage',
    'RRCConnectionSetupComplete',
    'InitialUEMessage',
    'ReleaseConnection'
})

# FDL mapping template for the bookmarks
bookmarkTemplate = 'heading "{bookmark}"'

# Specifies how the per statement remark has to be generated. By default the
# FDL remark contains the time and the file information (refer to traceRegex
# defined above.
remarkTemplate = r'(* {time} {file} *)'

# Regular expression for parsing the trace body when a message is being received
messageRxRegex = '(?P<message>\w+)\s*(\((?P<params>.*)\))?\s*from\s*(?P<source>\w+)'

# Regular expression for parsing the trace body when a message is being sent
messageTxRegex = '(?P<message>\w+)\s*(\((?P<params>.*)\))?\s*to\s*(?P<destination>\w+)'

# FDL mapping template for messages (received and sent messages)
messageTemplate = '{message} {params} :{source} -> {destination}'

# Regular expression for parsing the function/method entry trace body
invokeRegex = '(?P<called>\w+)(\.|::)(?P<method>\w+)\s*(\((?P<params>\w+)\))?'

# FDL mapping template for function/method entry
invokeTemplate = '{method} {params} :{caller} -> {called}'

# Regular expression for parsing the function/method exit trace body
returnRegex = '(\((?P<params>.*)\))?\s*from\s*(?P<called>\w+)(\.|::)(?P<method>\w+)'

# FDL mapping template for function/method exit
returnTemplate = 'return {params}:{called} -> {caller}'

# Regular expression for parsing the object creation trace body
createRegex = '(?P<created>\w+)\s*(\((?P<params>.*)\))?'

# FDL mapping template for object creation
createTemplate = '{creator} creates {created}{params}'

# Regular expression for object deletion
deleteRegex = '(?P<deleted>\w+)'

# FDL mapping template for object deletion
deleteTemplate = '{deletor} deletes "{deleted}"'

# Any trace that does not map to a defined type is treated as an action trace.
# FDL mapping for action traces is defined here. The trace type is also
# included in the statement.
actionTemplate = '{actor} takes action "{actionType} {action}"'

# FDL mapping template for state change trace body
stateChangeTemplate = '{object} state = "{state}"'

# Regular expression for parsing the timer start, stop anmd expiry trace body.
timerRegex = '(?P<timer>\w+)'

# FDL mapping templates for time start, stop and expiry traces.
startTimerTemplate = '{object} starts {timer}'
stopTimerTemplate = '{object} stops {timer}'
expiredTimerTemplate = 'timeout {timer}'

# FDL mapping for resource allocation and freeing traces.
allocateTemplate = '{object} allocates "{resource}"'
freeTemplate = '{object} frees "{resource}"'

# FDL mapping for action start and end traces.
beginActionTemplate = '{object} begins action "{action}"'
endActionTemplate = '{object} ends action "{action}"'

# Many statements contain parameters, They are parsed as attribute-value pairs.
# The attribute value pair separator and the attribute and value pair sepeator
# can be specifield here. The default settings work for parameters of the form:
# attribute1 = value1, attribute2 = value2 etc.
attributeValueSeparator = '='
avpairSeparator = ','
paramTemplate = '"{attribute}" = "{value}"'

defaultEntity = {
    'object':       'Object',
    'component':    'Component',
    'module':       'Module'
 }
