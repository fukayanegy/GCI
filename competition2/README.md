# [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk)
## summary
与えられた様々な顧客データを元に各データが債務不履行になるかどうかを予測する
顧客のデータからその顧客が債務不履行(default)になる確率を予測してください。データセットのTARGETカラムが目的変数、それ以外が説明変数となります。TARGETカラムが1であれば支払い困難、0であればそれ以外を表しています。
Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders.

Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

While Home Credit is currently using various statistical and machine learning methods to make these predictions, they're challenging Kagglers to help them unlock the full potential of their data. Doing so will ensure that clients capable of repayment are not rejected and that loans are given with a principal, maturity, and repayment calendar that will empower their clients to be successful.

今回のコンペティションでは、テストデータに対して予測された確率と正解データとの間のROC曲線下の面積であるAUCを競っていただきます。

## column