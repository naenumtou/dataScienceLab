
/*Import dataset*/
proc import out = dataset
datafile= "C:\Users\Sasiwut.Chaiyadecha\Desktop\Python\Input\Bayesian_model.csv"
DBMS = csv
replace;
getnames = yes;
quit;

/*Rename variable*/
data dataset;
set dataset;
rename ï__y = y;
run;

/*Check number of observation*/
proc sql;
select count(*)
into: count
from dataset;
quit;

/*Results dataset*/
data TimeSplit_results;
set _null_;
run;

/*Macro to create time series split*/
%macro timeSplit(data, n);

%do i = 1 %to &n;

%let trainSize = %sysevalf(&i * %sysevalf(&count / (&n + 1), floor) + %sysfunc(mod(&count, (&n + 1))));
%let testSize = %sysevalf(&count / (&n + 1), floor);

/*Create rank order*/
data temp;
set &data;
retain rank 0;
rank = rank + 1;
run;

/*Train/Test Split*/
data train test;
set temp;
if rank <= &trainSize then output train;
if (&trainSize < rank <= &trainSize + &testSize) then output test;
run;

/*Linear regression*/
proc reg data = train OUTEST = coef OUTVIF;
model y = x1 x2 x3
/ stb adjrsq;
output out = out_train  r = residual p = phat;
quit;

data out_train;
set out_train;
r = residual ** 2;
run;

data score;
set coef;
keep _RSQ_ ;
rename _RSQ_ = RSquareTrain;
run;

proc sql;
create table out_train as select mean(r) as MSETraining
from out_train;
quit;

/*Testing set*/
proc score data = test score = coef out = stat_testing type = parms
nostd predict;
var y x1 x2 x3;
quit;

data score_testing;
set stat_testing;
r = (y - model1) ** 2;
run;

proc sql;
create table score_testing as select mean(r) as MSETesting
from score_testing;
quit;

data score;
merge score out_train score_testing;
run;

/*Append table*/
data TimeSplit_results;
set TimeSplit_results score;
run;

%end;
%mend;

/*Execute Time split macro*/
%timeSplit(dataset, 5);

/*Average score*/
proc sql;
create table avg_score as select mean(RSquareTrain) as RSquareTrain,
mean(MSETraining) as MSETraining,
mean(MSETesting) as MSETesting
from TimeSplit_results;
quit;

data TimeSplit_results;
set TimeSplit_results avg_score;
run;
