const value
= {
  "type": "group",
  "id": "9a99988a-0123-4456-b89a-b1607f326fd8",
  "children1": {
    "a98ab9b9-cdef-4012-b456-71607f326fd9": {
      "type": "rule",
      "properties": {
        "field": "user.login",
        "operator": "equal",
        "value": [
          "Abhishek"
        ],
        "valueSrc": [
          "value"
        ],
        "valueType": [
          "text"
        ]
      }
    },
    "98a8a9ba-0123-4456-b89a-b16e721c8cd0": {
      "type": "rule",
      "properties": {
        "field": "datetime",
        "operator": "equal",
        "value": [
          "2024-01-17T14:30:00" // Example datetime value
        ],
        "valueSrc": [
          "value"
        ],
        "valueType": [
          "datetime"
        ]
      }
    },    
    "aabbab8a-cdef-4012-b456-716e85c65e9c": {
      "type": "rule",
      "properties": {
        "field": "acc_balance",
        "operator": "equal",
        "value": [
          4000
        ],
        "valueSrc": [
          "value"
        ],
        "valueType": [
          "number"
        ]
      }
    }
  },
  "properties": {
    "conjunction": "AND",
    "not": false
  }
};
export default value;
