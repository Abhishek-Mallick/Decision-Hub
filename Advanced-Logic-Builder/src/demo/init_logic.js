const value 
= {
  "and": [
    {
      "==": [
        {
          "var": "user.login"
        },
        "Abhishek"
      ]
    },
    {
      "==": [
        {
          "var": "datetime"
        },
        false
      ]
    },
    {
      ">=": [
        {
          "var": "Account Balance"
        },
        1000
      ]
    }
  ]
};
export default value;
