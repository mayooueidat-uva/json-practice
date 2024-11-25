#!/bin/bash

curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

# now it's curled into a file called aviation.json. 

cat aviation.json | jq -r '.[0:6] | .[].receiptTime' 

# now we've parsed receiptTime specifically. 



