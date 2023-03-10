#!/bin/bash

# Loop through each line in orderid.csv
while read order_id; do
    # Make a cURL request to update the order ID
    curl -X GET "localhost:1558/updateOrderId?id=${order_id}"
    
    # Sleep for 10ms
    usleep 10000
done < orderid.csv
