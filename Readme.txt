Fr question 1:(in folder name q1)
    Run: "python3 q1.py"
    Input: "input.txt"
          this should be in the same directory of that of the code.
          First line : n - number on test cases
          n-test cases:
              Next 12-lines: season,yr,mnth,hr,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed - each one of them in separate line.
    Output: "output.txt"
          each line contains the prediction of each test case in input file.
    Implementation:
        Implemented using RandomForestRegressor algorithm imported from sklearn. This provided an accuracy of 95.03564672% with default n_estimators=100.
Input columns(x): season,yr,mnth,hr,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed
Output Column(y): cnt (count of estimated bikes shared in that hour)
####################################################################################################################################################

For question 2:(in folder name q2)
    Run: "python3 q2.py"
    Input: "input.txt"
          this should be in the same directory of that of the code.
          First line : n - number on test cases
          n-test cases:
              Next 11-lines: season,yr,mnth,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed - each one of them in separate line.
    Output: "output.txt"
          each line contains the prediction of each test case in input file.
    Implementation:
        Implemented using RandomForestRegressor algorithm imported from sklearn. This provided an accuracy of 91.8339882% with default n_estimators=100.
Input columns(x): season,yr,mnth,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed
Output Column(y): cnt (count of estimated bikes shared in that whole day)
####################################################################################################################################################

For question 3:(in folder name q3)
    Run: "python3 q3.py"
    Input: "input.txt"
          this should be in the same directory of that of the code.
          First line : n - number on test cases
          n-test cases:
              Next 4-lines: Sepal Length(cm), Sepal wdith(cm), Petal Length(cm), Petal Width(cm) - each one of them in separate line.
    Output: "output.txt"
          each line contains the prediction of each test case in input file.
    Implementation:
        Implemented using KNearestNeighbors classifier algorithm imported from sklearn. This provided an accuracy of 96.6667%.
Input columns(x): Sepal Length(cm), Sepal wdith(cm), Petal Length(cm), Petal Width(cm)
Output Column(y): class of the flower.
