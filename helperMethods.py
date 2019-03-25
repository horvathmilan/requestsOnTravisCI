import re

def getScenarioNumber(log):
 fullMatch = re.search(r'(\d+ scenarios?).+(\d+ failed|\d+ passed)', log)
 if fullMatch is None:
  return 'There is no full match!'
  
 getScenarios = re.search(r'(\d+ scenarios?)', fullMatch.group())
 if getScenarios is None:
  return '0 scenario'
 else:
  return getScenarios.group()

def getFailedStepsNumber(log):
 fullMatch = re.search(r'(\d+ scenarios?).+(\d+ failed|\d+ passed)', log)
 if fullMatch is None:
  return 'There is no full match!'
  
 getFailedNumber = re.search(r'(\d+ failed)', fullMatch.group())
 if getFailedNumber is None:
  return '0 failed'
 else:
  return getFailedNumber.group()

def getPassedStepsNumber(log):
 fullMatch = re.search(r'(\d+ scenarios?).+(\d+ failed|\d+ passed)', log)
 if fullMatch is None:
  return 'There is no full match!'
  
 getPassedNumber = re.search(r'(\d+ passed)', fullMatch.group())
 if getPassedNumber is None:
  return '0 passed'
 else:
  return getPassedNumber.group()

def getNumberFromString(string):
 number = re.search(r'\d+', string)
 if number is None:
   return 'There is no number in the string'
 else:
   return number.group()
