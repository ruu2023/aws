# 間違える問題

## 外部ベンダーが使用する資格情報は、そのベンダー専用に制限
- アクセスを委任するためには、クロスアカウントアクセス権限とIAMロールの設定が不可欠です。

## シンプルなSQLステートメントを用いてAmazon S3バケット内のオブジェクトをフィルタリング
- クエリ結果の保存先のS3バケットと入力データとなるS3バケットを設定したクエリエディタを作成

## セキュリティのAWS Foundational Security Best Practices (FSBP) 標準に準拠していないAWSアカウントが存在する場合、それを把握
- 既存アカウントがAWS Foundational Security Best Practices 標準から逸脱していないかを監査するためには、AWS Security Hub Cloud Security Posture Management (CSPM) を利用します。


## ニアリアルタイム
- 「一日中継続して数十〜数百のジョブが実行されること」と「ニアリアルタイムに処理すること」が求められています。これは「Amazon EMRクラスターの利用が最適となるケース」に合致します。


## AWS SAMを活用したCloudFormationテンプレートを作成し、Amazon S3バケットを利用してデプロイを実施
- CloudFormationテンプレート内でAWS::Serverless Transform設定において使用するAWS SAMのバージョンを指定することが求められます。


## 既存のWindowsアカウント情報を用いてAWS環境へのユーザー認証を行い、AWSマネジメントコンソールを利用できるようにする必要
- IAMダッシュボードとAWS Directory Service Connectを利用したシングルサインオン機能というものは存在しません


## このアプリケーションを東京リージョンから東南アジアに展開することになり、データ処理がシンガポールリージョンにも自動的に複製されるレプリケーション構成を実現する必要があります。
- DynamoDB Streamsを有効にする必要があります。これにより、東京リージョンのDynamoDBテーブルにおけるデータの更新が発生した際に、シンガポールリージョンのDynamoDBテーブルへと自動的にレプリケーションされます。



## AWSに移行するデータベースに対して、同一リージョン内でのできる限り高い可用性とスケーラビリティを確保する構成が求められています
- Amazon Auroraにおいて「マルチAZ配置を有効化する」という単一のチェックボックスやボタンといった操作は、標準的なRDS（MySQLやPostgreSQLなど）とは異なり、直接的には存在しません。



## WorkSpacesを利用するために新規にIAMユーザーを人数分設定するのは面倒
- AD Connectorは、簡易的にIAMとオンプレミスのMicrosoft Active Directoryとの統合を実現する機能です。AD ConnectorとMicrosoft Active Directoryが統合されるとMicrosoft Active Directoryユーザーに対するAWSサービス認証が可能となります。



## Simple AD, Microsoft Active Directory
- Microsoft Active Directory が本物。 simple AD は互換品
- **AD Connector：** 新しくは作らない。**「すでに社内にある本物」をそのままAWSから使う**


## CloudFormation スタックセット
- スタックセットを使うと、その面倒な「アカウントの切り替え作業」を**AWS（CloudFormation）側が裏で全自動でやってくれます。**


## 平均ゴール数や平均パス数など、さまざまなプレーに関する詳細なデータを収集し、レポートを作成して、サッカーのプレミアリーグファンやスポーツメディアに提供します。試合日には世界中のユーザーから20万件以上のクエリが発生する見込みです。
- CloudFrontによる配信を実施する。
- ElastiCacheはインメモリデータベースであり、高速なデータ処理を実現しますが、コンテンツ配信処理の機能は有していません。



## S3ゲートウェイエンドポイントを利用して、Amazon EC2インスタンスからS3バケットにアクセスする。
- 経路を作るのはVPCエンドポイント、それをS3側で受け入れる/制限するのがバケットポリシー
- S3用のゲートウェイ型VPCエンドポイント

![](assets/Pasted%20image%2020260627123141.png)


## AWS のEC2までの構図
![](assets/Pasted%20image%2020260627123111.png)


## Route53 
- 純粋なトラフィック配分なら加重ルーティング
- レイテンシーマルチリージョンで最速のリージョンへ
- フェイルオーバー障害時にバックアップへ切替
- シャッフルシャーディングはDDoSを防げるAWSの仕組みでRoute53の標準機能



## VPCサイト間接続
- EC2が `web.internal.example.com`、DBが `db.internal.example.com` だとします。このとき、オンプレのリゾルバーに `web...` と `db...` を個別に登録する必要はありません。共通の末尾である **`internal.example.com` というゾーンに対して1つだけ転送ルールを書けば、その配下は全部まとめてインバウンドエンドポイントに飛びます**。
![](assets/Pasted%20image%2020260627125538.png)


## SCPとIAM/OU
- アカウントをまとめる OU

![](assets/Pasted%20image%2020260627130702.png)

- SPC and IAMポリシー
![](assets/Pasted%20image%2020260627130737.png)
- AWS Organizations は、前回話した通り「**複数のAWSアカウントを組織として束ねる**」土台
- AWS Control Tower は、その上に乗る「**マルチアカウント環境を、ベストプラクティスに沿って自動でセットアップ・管理してくれる**」
- AWS Security Hub は、「**各アカウントのセキュリティ状態を一箇所に集めて、ベストプラクティスに沿っているか自動でチェック・採点する**」



## データへの高速アクセスを可能にすることが必要です。また、ゲームデータを維持するためには、アプリケーションを再起動後にもデータがディスクに永続化
- アプリケーションを再起動した後でもデータがディスクに永続化される必要があります。Amazon ElastiCache Redis OSSクラスターをデプロイ



## Amazon EC2インスタンスにホストされたActiveMQを用いてキューメッセージを送信し、その後、別のAmazon EC2インスタンス上で動作するコンシューマーアプリケーションがメッセージを処理
![](assets/Pasted%20image%2020260627132546.png)
- オンプレや既存システムを、コードを変えずにAWSへ移行(リフト&シフト)したいとき → MQ。
- ゼロからAWS上で新規に作るとき → SQS
![](assets/Pasted%20image%2020260627132533.png)
- なぜEBSではなくEFSなのかというと、EBS（普通のディスク）は1つのAZ・基本1つのEC2に紐づくのに対し、EFSは複数AZ・複数EC2から共有できるからです。「AZをまたいで同じデータを使いたい」要件には、EFSが向いています。
- EFSのデータ実体は「どのAZにも無い」のではなく、「AWSが裏で複数AZに冗長保存している」(だからデータ自体はAZ障害に強い)。それでもマルチAZで組むのは、データのためではなく、**各AZのEC2がアクセスするための入り口(マウントターゲット)を、使う全AZに用意する必要があるから**。


## フェールオーバー
- 「アクティブ/アクティブ」ラウンドロビン
- 「アクティブ/パッシブ」フェイルオーバー



## Cognito
- Cognitoの出番ではありません。Cognitoは「アプリにログインする大勢の人間」を捌く
- アクセスしてくるのが「人間」ではなく「**別のシステム/アプリケーション**」ならIAMロールでこれが満たせる


## S3解析の早見
- EMR（Elastic MapReduce）は、ひとことで言うと **大量データを複数台のサーバーで分散処理するための「ビッグデータ処理基盤」をマネージドで提供するサービス**
![](assets/Pasted%20image%2020260627134641.png)


## 引っかけ

- 標準RDSの高可用性 → 「**マルチAZ配置を有効化**」（スタンバイを別AZに、機能としてオン）。
- Auroraの高可用性 → 「**別AZにAuroraレプリカを配置**」（レプリカを置く構成にする。ストレージは元々マルチAZ）。
- 選択肢を読むときのコツは、**「Aurora」なのに「マルチAZ配置を有効化する」というRDSの言い回しが出てきたら警戒する**ことです。
- 「**Auroraはストレージを手動で拡張する**」→ 誤り。Auroraのストレージは完全自動。手動拡張が要るのは通常のRDSの方（それもAuto Scaling設定できるが）。
- 「**DynamoDBのAuto Scalingはサーバー台数を増やす**」→ 誤り。増減するのはキャパシティ(RCU/WCU)。

## AWS FireWall Manager

## AWS 側にはアカウントがない
- AD Connectorを利用してオンプレミス環境のMicrosoft Active Directoryと連携することで、Microsoft Active Directoryユーザーに対してWorkSpacesを利用する権限を付与する。


## リザーブド
・EC2リザーブドインスタンス
・RDSリザーブドインスタンス
・ElastiCacheリザーブドキャッシュノード
・DynamoDBリザーブドキャパシティ
・Redshiftリザーブドノード


## ほぼStepFunction
- 複数のLambda関数を用いてデータ処理を行う必要があります。


## RAG
- Amazon OpenSearch Service Amazon S3 Vectors Amazon DocumentDB
![](assets/Pasted%20image%2020260627153508.png)


##  クレカの不正検出
![](assets/Pasted%20image%2020260627154242.png)

## リアルタイム保存
- Managed Flinkリアルタイム流れるデータをその場で処理・分析(気象データなど)



## EKS
- コントロールプレーンはAWSの範囲でユーザーは触らない
- インターフェースVPCエンドポイントを構成
![](assets/Pasted%20image%2020260627155610.png)

## Lake Formation
- EMRやAthenaでS3のデータを分析するとき、「このユーザーはこのテーブルのこの列だけ見ていい」
- ### AWS Data Exchange「**外部のデータプロバイダーが提供するデータセットを、AWSマーケットプレイス経由でサブスクライブして使えるサービス**」
![](assets/Pasted%20image%2020260627164151.png)


## KMS
- 「**KMSで暗号化されたリソース（SNS/SQS/S3など）にアクセスしたい**」という問題が出たら、**アクセスする側のIAMロールにKMS権限も必要**
![](assets/Pasted%20image%2020260627185950.png)


- Amazon TranscribeのPIIリダクション機能を活用します。この機能を有効化して、Amazon Transcribeの文字起こしジョブを設定することで、顧客個人を特定できる情報を自動的に除去する


## DynamoDBでは以下の2つのキャパシティモードが利用可能です。
・オンデマンド
・プロビジョンド (デフォルト、無料利用枠の対象
- 削除検知してstream firehose → s3移動でコスト下げられる
![](assets/Pasted%20image%2020260627191831.png)

- 「**定期実行・スケジュール**」というキーワードが出たら、**EventBridge**が必ずセット




![](assets/Pasted%20image%2020260627195704.png)



## EKS scale
![](assets/Pasted%20image%2020260627202303.png)


## 過程で複数のインスタンス間での通信が頻繁に行われます。このEC2インスタンスを用いた作業の効率化が求められています。
- 「インスタンス間通信が多い」というキーワードが出たらクラスタープレイスメントグループを思い出すと良いです。
- クラスタープレイスメントグループを設定した上で、M5インスタンス群を起動する。


**Savings Plansの種類は3つ**あり、その1つがEC2 Instance Savings Plans。
- **Compute Savings Plans** — 最も柔軟。インスタンスファミリー・リージョン・OS・テナンシー問わず適用。Fargate、Lambdaにも適用。割引率は最大66%。
- **EC2 Instance Savings Plans** — 特定リージョンの**特定インスタンスファミリー**にコミット。柔軟性は下がるが割引率が高い（最大72%）。
- **SageMaker Savings Plans** — SageMaker向け。


- secret manager は自動ローテーション対応
- 読み取りはレプリカ！作業量が要件でなければマルチAZのAuroraレプリカが最適
- lamdaは15分以内の処理だけ！
- サードパーティの証明書は基本手動
- Aのキーポリシー、Aのバケットポリシー、BのインスタンスIAMロール
- controll tower のデータレジデンシーガードレールでリージョン制限できる
- 最強はinstance saving(インスタンス指定ガチガチで72%)
- fargate lamda 節約ならcompute saving 年間コミット　
- S3 (PutObject) → EventBridge (ルール) → Step Functions (ステートマシン起動)
- AWSSysteManager=SSM そのなかの SessionManager.を使うことが踏み台が割の推奨
- pull 型ならSQS一択、注意すべきは何時間おきに取得するか書いてあるかだけ
- サードパーティならssm run command


## 総さらい

# 1

![](assets/Pasted%20image%2020260628115858.png)
![](assets/Pasted%20image%2020260628115907.png)

**決め手:** 「1TB超/日の大量データをS3に貯めて分析」→ S3上のデータをそのままSQLで分析する **Redshift Spectrum**（またはAthena）が定石。



![](assets/Pasted%20image%2020260628115928.png)
![](assets/Pasted%20image%2020260628120036.png)


![](assets/Pasted%20image%2020260628120102.png)
![](assets/Pasted%20image%2020260628120110.png)


![](assets/Pasted%20image%2020260628120122.png)
![](assets/Pasted%20image%2020260628120132.png)


![](assets/Pasted%20image%2020260628120157.png)
![](assets/Pasted%20image%2020260628120206.png)


![](assets/Pasted%20image%2020260628120236.png)
![](assets/Pasted%20image%2020260628120242.png)



![](assets/Pasted%20image%2020260628120254.png)
![](assets/Pasted%20image%2020260628120304.png)





![](assets/Pasted%20image%2020260628120318.png)
![](assets/Pasted%20image%2020260628120326.png)



![](assets/Pasted%20image%2020260628120337.png)
![](assets/Pasted%20image%2020260628120345.png)


![](assets/Pasted%20image%2020260628120356.png)![](assets/Pasted%20image%2020260628120402.png)



# 2
![](assets/Pasted%20image%2020260628120438.png)![](assets/Pasted%20image%2020260628120444.png)


![](assets/Pasted%20image%2020260628120458.png)
![](assets/Pasted%20image%2020260628120506.png)



![](assets/Pasted%20image%2020260628120518.png)![](assets/Pasted%20image%2020260628120525.png)



![](assets/Pasted%20image%2020260628120536.png)![](assets/Pasted%20image%2020260628120549.png)


![](assets/Pasted%20image%2020260628120558.png)![](assets/Pasted%20image%2020260628120603.png)


![](assets/Pasted%20image%2020260628120615.png)![](assets/Pasted%20image%2020260628120622.png)




![](assets/Pasted%20image%2020260628120637.png)
![](assets/Pasted%20image%2020260628120651.png)


![](assets/Pasted%20image%2020260628120704.png)![](assets/Pasted%20image%2020260628120710.png)


![](assets/Pasted%20image%2020260628120722.png)![](assets/Pasted%20image%2020260628120728.png)


![](assets/Pasted%20image%2020260628120738.png)![](assets/Pasted%20image%2020260628120746.png)


![](assets/Pasted%20image%2020260628120759.png)![](assets/Pasted%20image%2020260628120806.png)


![](assets/Pasted%20image%2020260628120818.png)![](assets/Pasted%20image%2020260628120825.png)



# 3
![](assets/Pasted%20image%2020260628120847.png)
![](assets/Pasted%20image%2020260628120855.png)


![](assets/Pasted%20image%2020260628120905.png)![](assets/Pasted%20image%2020260628120910.png)


![](assets/Pasted%20image%2020260628120921.png)![](assets/Pasted%20image%2020260628120927.png)




![](assets/Pasted%20image%2020260628120940.png)
![](assets/Pasted%20image%2020260628120947.png)


![](assets/Pasted%20image%2020260628120958.png)![](assets/Pasted%20image%2020260628121004.png)


![](assets/Pasted%20image%2020260628121016.png)![](assets/Pasted%20image%2020260628121024.png)


![](assets/Pasted%20image%2020260628121034.png)![](assets/Pasted%20image%2020260628121041.png)


![](assets/Pasted%20image%2020260628121054.png)
![](assets/Pasted%20image%2020260628121101.png)





![](assets/Pasted%20image%2020260628121111.png)
![](assets/Pasted%20image%2020260628121117.png)




![](assets/Pasted%20image%2020260628121128.png)![](assets/Pasted%20image%2020260628121136.png)



![](assets/Pasted%20image%2020260628121149.png)
![](assets/Pasted%20image%2020260628121202.png)


![](assets/Pasted%20image%2020260628121219.png)
![](assets/Pasted%20image%2020260628121230.png)




![](assets/Pasted%20image%2020260628121240.png)![](assets/Pasted%20image%2020260628121247.png)






# 4
![](assets/Pasted%20image%2020260628121309.png)![](assets/Pasted%20image%2020260628121318.png)


![](assets/Pasted%20image%2020260628121329.png)
![](assets/Pasted%20image%2020260628121335.png)



![](assets/Pasted%20image%2020260628121345.png)![](assets/Pasted%20image%2020260628121352.png)



![](assets/Pasted%20image%2020260628121402.png)
![](assets/Pasted%20image%2020260628121413.png)



![](assets/Pasted%20image%2020260628121424.png)![](assets/Pasted%20image%2020260628121437.png)


![](assets/Pasted%20image%2020260628121453.png)
![](assets/Pasted%20image%2020260628121500.png)

![](assets/Pasted%20image%2020260628121512.png)![](assets/Pasted%20image%2020260628121517.png)



![](assets/Pasted%20image%2020260628121526.png)![](assets/Pasted%20image%2020260628121532.png)




![](assets/Pasted%20image%2020260628121542.png)![](assets/Pasted%20image%2020260628121548.png)






# 5
![](assets/Pasted%20image%2020260628121611.png)![](assets/Pasted%20image%2020260628121618.png)





![](assets/Pasted%20image%2020260628121629.png)![](assets/Pasted%20image%2020260628121635.png)







![](assets/Pasted%20image%2020260628121644.png)![](assets/Pasted%20image%2020260628121652.png)








![](assets/Pasted%20image%2020260628121701.png)![](assets/Pasted%20image%2020260628121709.png)






![](assets/Pasted%20image%2020260628121718.png)![](assets/Pasted%20image%2020260628121726.png)







![](assets/Pasted%20image%2020260628121734.png)![](assets/Pasted%20image%2020260628121740.png)







![](assets/Pasted%20image%2020260628121747.png)![](assets/Pasted%20image%2020260628121754.png)






![](assets/Pasted%20image%2020260628121803.png)![](assets/Pasted%20image%2020260628121809.png)







![](assets/Pasted%20image%2020260628121817.png)![](assets/Pasted%20image%2020260628121823.png)









![](assets/Pasted%20image%2020260628121831.png)![](assets/Pasted%20image%2020260628121837.png)






![](assets/Pasted%20image%2020260628121845.png)![](assets/Pasted%20image%2020260628121851.png)









![](assets/Pasted%20image%2020260628121859.png)![](assets/Pasted%20image%2020260628121905.png)






# 6
![](assets/Pasted%20image%2020260628121935.png)![](assets/Pasted%20image%2020260628121942.png)



![](assets/Pasted%20image%2020260628121952.png)
![](assets/Pasted%20image%2020260628122010.png)





![](assets/Pasted%20image%2020260628122018.png)![](assets/Pasted%20image%2020260628122024.png)





![](assets/Pasted%20image%2020260628122031.png)![](assets/Pasted%20image%2020260628122037.png)









![](assets/Pasted%20image%2020260628122046.png)![](assets/Pasted%20image%2020260628122052.png)









![](assets/Pasted%20image%2020260628122100.png)![](assets/Pasted%20image%2020260628122107.png)






![](assets/Pasted%20image%2020260628122116.png)![](assets/Pasted%20image%2020260628122123.png)









![](assets/Pasted%20image%2020260628122132.png)![](assets/Pasted%20image%2020260628122139.png)






![](assets/Pasted%20image%2020260628122147.png)![](assets/Pasted%20image%2020260628122154.png)







![](assets/Pasted%20image%2020260628122203.png)![](assets/Pasted%20image%2020260628122210.png)







![](assets/Pasted%20image%2020260628122218.png)![](assets/Pasted%20image%2020260628122224.png)






![](assets/Pasted%20image%2020260628122232.png)![](assets/Pasted%20image%2020260628122238.png)






![](assets/Pasted%20image%2020260628122247.png)![](assets/Pasted%20image%2020260628122253.png)























































































