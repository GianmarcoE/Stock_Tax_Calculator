# Stock_Tax_Calculator
The application examines the Revolut report for stocks transactions and automatically calculates profits and losses, taxable income and tax due for the selected year (valid for Poland).
The rates are obtained from Narodowy Bank Polski through API requests.  


For correctness of the calculations, the following steps should be followed:  

1 - Positions that were not closed during the year in exam should be canceled from the report.  

2 - Positions that were already closed in the years preceding the one in exam, should also be canceled (those that were already object of a previous tax statement).  

3 - No blank lines between records.  

4 - No altering of the layout (columns, cells format...)
