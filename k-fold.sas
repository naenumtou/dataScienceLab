
/*Import dataset*/
proc import out = dataset
datafile = "C:\Users\Sasiwut.Chaiyadecha\Desktop\Python\titanic.csv"
DBMS = csv
replace;
getnames = yes;
quit;

/*Keep only numberic variables*/
data dataset; 
set dataset;
keep
Survived
Pclass
Age
SibSp
Parch
Fare
;
run;

/*Fill missing values*/
proc stdize data = dataset reponly method = mean out = dataset;
var Age;
quit;

/*Results dataset*/
data KFold_results;
set _null_;
run;

/*Macro K-Fold Cross validation*/
%macro KFold(data, k);

proc surveyselect data = &data groups = &k out = fold;
quit;

%do i = 1 %to &k;

data train test;
set fold;
if groupid ne &i then output train;
if groupid eq &i then output test;
run;

/*Logistic model*/
proc logistic data = train descending;
model Survived =
Pclass
Age
SibSp
Parch
Fare;
roc;
ods output rocassociation = auc;
score data = test out = valset;
quit;

/*Model performance*/
data auc;
set auc;
where RocModel = "Model";
keep Area;
rename Area = AUCTrain;
run;

data auc;
set auc;
GINITrain = 2 * AUCTrain - 1;
run;

/*Testing set*/
proc npar1way wilcoxon data= valset;
class Survived;
var p_1;
ods output WilcoxonScores = WilcoxonScore;
quit;

data auc_test;
set WilcoxonScore;
if Class = 1 then absscore = abs(ExpectedSum - SumOfScores);
run;

proc sql;
create table auc_test as select  exp(sum(log(N))) as N, sum(absscore) as absscore
from auc_test;
quit;

data auc_test;
set auc_test;
d = absscore / N;
AUCTest = d + 0.5;
GINITest = d * 2;
keep AUCTest GINITest;
run;

data auc;
merge auc auc_test;
run;

/*Append table*/
data KFold_results;
set KFold_results auc;
run;

%end;
%mend;

/*Execute K-Fold Macro*/
%KFold(dataset, 5);
