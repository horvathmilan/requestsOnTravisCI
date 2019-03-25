import customRequestMethods
import re
import helperMethods
import time
import lcdFunctions
from neopixel import *
import lcddriver

lcd = lcddriver.lcd()

LED_COUNT      = 16
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False

def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

if __name__ == '__main__':
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
  strip.begin()

  last_build_id = customRequestMethods.getLastBuildID()
  print('Last build ID: '+ str(last_build_id))
  last_status = customRequestMethods.getLastBuildStatusByID(last_build_id)
  log = customRequestMethods.getlog(last_build_id + 1)

  scenarios = helperMethods.getScenarioNumber(log)
  failedNumber = helperMethods.getFailedStepsNumber(log)
  passedNumber = helperMethods.getPassedStepsNumber(log)
  print(scenarios)
  print(failedNumber)
  print(passedNumber)

  scenarioNumber = helperMethods.getNumberFromString(scenarios)
  failed = helperMethods.getNumberFromString(failedNumber)
  passed = helperMethods.getNumberFromString(passedNumber)

  avg = float(passed)/float(scenarioNumber)
  print(avg)
  lcd.lcd_clear()
  if avg >= 0.5:
      colorWipe(strip, Color(255, 0, 0))
      lcd.lcd_display_string("Scenarios",1)
      lcd.lcd_display_string(scenarioNumber,2)
      time.sleep(3)
      lcd.lcd_clear()
      lcd.lcd_display_string("Passed",1)
      lcd.lcd_display_string(passed,2)
      time.sleep(3)
      lcd.lcd_display_string("Failed",1)
      lcd.lcd_display_string(failed,2)
      time.sleep(3)
      lcd.lcd_backlight("off")
  else:
      colorWipe(strip, Color(0, 255, 0))
